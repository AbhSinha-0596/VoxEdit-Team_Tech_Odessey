
# VoxEdit: Voice-based Image Editor   by Team_Tech Odyssey

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

<img width="1621" height="866" alt="Screenshot 2026-08-11 092355" src="https://github.com/user-attachments/assets/f3f35eed-49d9-4a51-9cd6-50a0477050de" />

<img width="1626" height="873" alt="Screenshot 2026-08-11 092420" src="https://github.com/user-attachments/assets/6e3c03ab-20c6-4ad9-ae1e-576926720f45" />

<img width="1629" height="865" alt="Screenshot 2026-08-11 092444" src="https://github.com/user-attachments/assets/e98a1510-fe16-4b86-aa67-ddeb2b2c31b2" />

<img width="1628" height="855" alt="Screenshot 2026-08-11 092533" src="https://github.com/user-attachments/assets/7270ea01-45a7-45ca-808c-a4361f6b37e3" />

<img width="1624" height="861" alt="Screenshot 2026-08-11 092604" src="https://github.com/user-attachments/assets/6b7e82b5-7ce0-41e1-b43d-86d08b53a3e6" />

<img width="1623" height="866" alt="Screenshot 2026-08-11 092623" src="https://github.com/user-attachments/assets/f01c80e3-062d-4b73-885c-da4ba8c60c47" />

<img width="1625" height="867" alt="Screenshot 2026-08-11 092651" src="https://github.com/user-attachments/assets/99a9a0b7-24ca-4d2f-9caa-b21ceed54ee7" />









## Future Improvements

* Multi-turn conversational editing
* Real-time streaming voice interaction
* Undo/redo editing history

## Conclusion

VoxEdit demonstrates a practical **voice-driven image editing workflow** that combines AI transcription, vector-based memory retrieval, and conversational audio feedback to create an intuitive and context-aware editing experience.
