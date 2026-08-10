import streamlit as st
from PIL import Image
from io import BytesIO

from image_processor import execute_command
from speech_processing import speech_to_text, text_to_speech
from llm_router import route_command
from qdrant_memory import retrieve_similar, store_mapping
from streamlit_mic_recorder import mic_recorder

st.set_page_config(page_title="Speech based Image Editor", layout="wide")

st.title("Voice-Based AI Image Editor")
st.write(
"Speak naturally: 'Make the image warmer', 'Blur the background', 'Increase brightness by twenty percent'."
)
st.write("Available Edit Options:-- Brightness -- Saturation -- Blur -- Warmth -- Sharpness -- Enhance ")
uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    uploaded_name=uploaded.name
# Initialize only when a NEW image is uploaded
if (
    "original_image" not in st.session_state
    or st.session_state.get("uploaded_name") != uploaded_name
):
    st.session_state.uploaded_name = uploaded_name
    st.session_state.original_image = image
    st.session_state.current_image = image.copy()
    st.session_state.image_stack = [image.copy()]
    st.session_state.edit_history = []
    st.session_state.transcript = None

st.image(st.session_state.current_image, caption="Current Image", width=400)

st.subheader("Voice Command")
st.write("Press record, speak your image editing request, then stop recording.")

audio = mic_recorder(
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    just_once=True,
    use_container_width=True,
    key="voice_input"
)


if audio:
    st.audio(audio["bytes"], format="audio/wav")

    with st.spinner("Transcribing speech..."):
        transcript = speech_to_text(audio["bytes"])

    if transcript.startswith("["):
        st.error(transcript)
    else:
        st.session_state.transcript = transcript


if st.session_state.get("transcript"):

    st.subheader("Transcribed Speech")
    st.write("Review and correct the transcription before applying edits.")

    edited_text = st.text_area(
        "Edit transcription",
        value=st.session_state.transcript,
        height=120,
        key="editable_transcript"
    )

    with st.sidebar:
        st.header("Edit History")

        if st.session_state.edit_history:
            for i, item in enumerate(st.session_state.edit_history, 1):
                st.write(f"{i}. {item['text']}")
        else:
            st.write("No edits yet.")

    col1, col2 = st.columns(2)

    
    with col1:
        if st.button("Use This Command", use_container_width=True):

            try:
                with st.spinner("Searching memory..."):
                    command = retrieve_similar(edited_text)

                if command is None:
                    with st.spinner("Understanding request with Mistral..."):
                        command = route_command(edited_text)

                # Parse JSON string if needed
                if isinstance(command, str):
                    import json
                    command = json.loads(command)

                commands = command if isinstance(command, list) else [command]

                result = st.session_state.current_image

                with st.spinner("Applying image edits..."):
                    for cmd in commands:
                        result = execute_command(result, cmd)

                st.session_state.current_image = result
                st.session_state.image_stack.append(result.copy())

                # Store ONE history entry per user request
                st.session_state.edit_history.append({
                    "text": edited_text,
                    "commands": commands
                })

                store_mapping(edited_text, commands)

                actions = [cmd.get("action", "edit") for cmd in commands]
                response = (
                    "Done. I applied the following edits: "
                    + ", ".join(actions)
                    + "."
                )

                try:
                    audio_path = text_to_speech(response)
                    try:
                        st.audio(audio_path, format="audio/wav", autoplay=True)
                    except TypeError:
                        st.audio(audio_path)

                except Exception as e:
                    st.warning(f"TTS failed: {e}")

                st.success(response)
                st.rerun()

            except Exception as e:
                st.error(f"Image editing failed: {e}")

        if st.button("Undo Last Edit", use_container_width=True):

            if len(st.session_state.image_stack) > 1:

                st.session_state.image_stack.pop()
                st.session_state.current_image = (
                    st.session_state.image_stack[-1].copy()
                )

                if st.session_state.edit_history:
                    st.session_state.edit_history.pop()

                st.success("Last edit undone.")
                st.rerun()

            else:
                st.info("Nothing to undo.")

    with col2:
        if st.button("Re-record", use_container_width=True):
            st.session_state.pop("transcript", None)
            st.session_state.pop("editable_transcript", None)
            st.rerun()


st.subheader("Edited Image")
st.image(st.session_state.current_image, width=400)

buffer = BytesIO()
st.session_state.current_image.save(buffer, format="JPEG")

st.download_button(
    "Download Edited Image",
    data=buffer.getvalue(),
    file_name="edited_output.jpg",
    mime="image/jpeg"
)
