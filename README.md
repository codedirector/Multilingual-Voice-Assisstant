# 🎙️ AI Voice Assistant

> A multilingual AI-powered voice assistant that converts text to speech across Indian languages — featuring English, Hindi, Punjabi, and Marathi support with a stunning dark-mode voice interface.

---

## 📌 Overview

The **AI Voice Assistant** is a Python-based Text-to-Speech (TTS) application that uses AI to generate lifelike voice audio from text input. It features a sleek dark-mode web UI with a glowing microphone orb, real-time language switching, and both voice and text input modes.

---

## 🖼️ Interface Preview
<img width="1527" height="784" alt="image" src="https://github.com/user-attachments/assets/0fa102e6-6022-45c5-af6b-b3dc694902d7" />



> *The voice interface features a rainbow-glowing microphone orb on a dark background, with language switcher buttons (EN, HI, PA, MR) in the top-right corner and a "Type instead" fallback option at the bottom.*

---

## 🗂️ Project Structure

```
AI-Voice-Assistant/
├── main (8).py              # Core application logic & orchestration
├── tts_api (1).py           # TTS API integration & audio generation
├── hindi_simple.mp3         # Sample output — Hindi TTS audio
├── marathi_simple.mp3       # Sample output — Marathi TTS audio
└── tts_1762055475.mp3       # Generated TTS audio sample
```

---

## ✨ Features

- 🎤 **Tap-to-Speak Interface** — Click the glowing mic orb to start voice input instantly
- ⌨️ **Type Instead Mode** — Fallback text input for when voice isn't available
- 🌈 **Rainbow Glowing Orb UI** — Stunning animated dark-mode microphone interface
- 🌐 **Live Language Switching** — Toggle between EN / HI / PA / MR from the top bar
- 🗣️ **Text-to-Speech Output** — AI-generated natural voice responses in selected language
- 🎵 **MP3 Audio Output** — Saves generated speech as `.mp3` files
- 🔌 **Modular TTS API Layer** — Swap TTS providers without touching core logic

---

## 🔊 Audio Samples

Pre-generated sample outputs included in the repository:

| File | Language | Description |
|---|---|---|
| `hindi_simple.mp3` | Hindi (हिन्दी) | Simple Hindi TTS demo |
| `marathi_simple.mp3` | Marathi (मराठी) | Simple Marathi TTS demo |
| `tts_1762055475.mp3` | Auto-generated | Timestamped TTS output sample |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- A TTS API key (e.g., ElevenLabs, Google Cloud TTS, or similar)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayushi-mahariye/AI-Voice-Assistant.git
   cd AI-Voice-Assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   > If no `requirements.txt` is present, install common dependencies:
   > ```bash
   > pip install requests python-dotenv elevenlabs
   > ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```env
   TTS_API_KEY=your_tts_api_key_here
   TTS_MODEL=your_preferred_model
   OUTPUT_DIR=./output
   ```

4. **Run the assistant**
   ```bash
   python "main (8).py"
   ```

5. **Open in browser**

   Navigate to `http://localhost:PORT` to launch the voice interface.

---

## 🛠️ Usage

### Via the Web UI

1. Open the app in your browser
2. Select your language from the top-right switcher: **EN | HI | PA | MR**
3. Click the **glowing microphone orb** to start speaking
4. Or click **"Type instead"** to enter text manually
5. The assistant processes your input and responds with AI-generated speech

### Via Python API

```python
from tts_api import generate_audio

# English
generate_audio(text="Hello, how can I assist you?", language="en", output_file="out_en.mp3")

# Hindi
generate_audio(text="नमस्ते, मैं आपकी सहायता कर सकता हूँ।", language="hi", output_file="out_hi.mp3")

# Punjabi
generate_audio(text="ਸਤ ਸ੍ਰੀ ਅਕਾਲ, ਮੈਂ ਤੁਹਾਡੀ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ।", language="pa", output_file="out_pa.mp3")

# Marathi
generate_audio(text="नमस्कार, मी तुम्हाला मदत करू शकतो.", language="mr", output_file="out_mr.mp3")
```

---

## 🌐 Supported Languages

| Language | Code | Script | UI Toggle | Status |
|---|---|---|---|---|
| English | `en` | Latin | **EN** | ✅ Supported |
| Hindi | `hi` | Devanagari | **HI** | ✅ Supported |
| Punjabi | `pa` | Gurmukhi | **PA** | ✅ Supported |
| Marathi | `mr` | Devanagari | **MR** | ✅ Supported |
| Tamil | `ta` | Tamil | — | 🔜 Planned |
| Telugu | `te` | Telugu | — | 🔜 Planned |
| Bengali | `bn` | Bengali | — | 🔜 Planned |
| Gujarati | `gu` | Gujarati | — | 🔜 Planned |

---

## 🔌 TTS API Module

The `tts_api (1).py` module handles all communication with the TTS provider:

- Sends text and language parameters to the TTS API
- Streams and saves audio output as `.mp3`
- Supports configurable voice models and speaking rate
- Handles API errors and retries gracefully

---

## 🤝 Contributing

Contributions are welcome, especially for adding more Indian language support!

1. Fork the repository
2. Create a branch: `git checkout -b feature/add-tamil-support`
3. Commit changes: `git commit -m "Add Tamil TTS support"`
4. Push: `git push origin feature/add-tamil-support`
5. Open a Pull Request


