# Avatar Voice Assistant (v1)

A modular AI-powered avatar system that combines image generation, large language models, text-to-speech (TTS), and optional lip-sync animation to produce a responsive, lifelike digital assistant.

---

## Features

- **Conversational Intelligence**: Local or API-driven LLM integration (e.g., Mistral via LangChain)
- **Text-to-Speech**: Fast, natural-sounding voice synthesis using Coqui TTS or Bark
- **Image Rendering**: Dynamic avatar generation with Stable Diffusion or static fallback
- **Optional Lip Sync**: Realistic facial animation via [SadTalker](https://github.com/OpenTalker/SadTalker)
- **Web Interface**: Gradio-powered UI for local interaction
- **Modular Design**: Swappable components (TTS engine, model backends, image pipelines)

---

## Directory Structure

```bash
AVATAR_V1_TEST/
│
├── avatar_engine/        # Core engine modules
│   ├── avatar_renderer.py     # Image handling
│   ├── image_gen.py           # Image generation via model or static fallback
│   ├── llm_interface.py       # LLM pipeline (LangChain or local)
│   ├── stt.py                 # (Optional) Speech-to-text placeholder
│   ├── tts.py                 # Coqui TTS integration
│
├── ui/
│   └── gradio_interface.py    # GUI layer
│
├── SadTalker/             # Optional lip-sync animation engine
├── gfpgan/                # Optional face enhancement
├── results/               # Output videos/images/audio
├── session_output/        # Runtime outputs
│
├── assets/                # Avatar templates, background, etc.
├── settings.json          # Config file for persona, model, etc.
├── requirements.txt       # All Python dependencies
├── run.bat                # Windows launch script
├── main.py                # Entry point
└── test.py                # Local debug script
