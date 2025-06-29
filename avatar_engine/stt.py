# stt.py
import whisper

# Load base model (can be 'tiny', 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")  # will use CUDA automatically if available

def transcribe(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

# Example usage
if __name__ == "__main__":
    transcription = transcribe("path_to_your_audio_file.wav")
    print(transcription)
