from TTS.api import TTS

# Use a male-friendly model with no espeak required
tts = TTS(model_name="tts_models/en/ljspeech/glow-tts", progress_bar=False, gpu=False)

def text_to_audio(text, output_path):
    print("[DEBUG] Using Glow-TTS Male Voice (No Phonemizer)")

    if len(text.strip()) < 10:
        text += " ...okay."

    tts.tts_to_file(
        text=text,
        file_path=output_path
    )