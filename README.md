
# VoxEdit: Voice-based Image Editor   by Team_Tech_Odyssey

**VoxEdit** is a voice-controlled image editing application that allows users to modify images using natural speech commands. It integrates **Mistral AI** for speech-to-text transcription, **Qdrant** for session-aware memory retrieval, and **Rime API** for interactive voice responses, enabling a fast and conversational image editing workflow.

## ✨ Key Features

* **Voice-first editing** using direct microphone input
* **Mistral AI transcription** with editable command preview
* **Session-aware memory** powered by Qdrant vector embeddings
* **Interactive voice feedback** through Rime API
* **Streamlit-based interface** for image upload, editing, and preview

## 🛠️ Tech Stack

| Technology                 | Role                                    |
| -------------------------- | --------------------------------------- |
| **Python**                 | Core application logic                  |
| **Streamlit**              | User interface                          |
| **Pillow (PIL)**           | Image processing                        |
| **Mistral AI API**         | Speech-to-text transcription            |
| **Qdrant Vector Database** | Embedding storage and history retrieval |
| **Sentence Transformers**  | Text embeddings                         |
| **Rime API**               | Text-to-speech responses                |

## Architecture

1. Upload an image
2. Record a voice command
3. Transcribe speech using **Mistral AI**
4. Edit the transcription if required
5. Retrieve relevant session context from **Qdrant**
6. Generate and apply the image editing instruction
7. Respond with interactive audio using **Rime API**

## Screenshots

**Voice command interface and image editing workflow**

*Add screenshots here*

## Future Improvements

* Multi-turn conversational editing
* Real-time streaming voice interaction
* Undo/redo editing history

## Conclusion

VoxEdit demonstrates a practical **voice-driven image editing workflow** that combines AI transcription, vector-based memory retrieval, and conversational audio feedback to create an intuitive and context-aware editing experience.
