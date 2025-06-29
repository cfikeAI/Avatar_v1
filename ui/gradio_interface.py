# ui/gradio_interface.py
import gradio as gr
from avatar_engine import llm_interface, stt, tts, image_gen
from avatar_engine.avatar_renderer import generate_avatar
from avatar_engine.tts import text_to_audio
from avatar_engine.llm_interface import get_chain
import os

# Initialize conversation history
conversation_history = []
reply_count = 0  # Tracks how many replies have occurred

avatar_path = os.path.join("assets", "avatar.jpg")

def chat(audio_file_path, persona_text):
    global conversation_history, reply_count, avatar_path

    # Generate avatar ONCE at session start
    if avatar_path is None:
        avatar_path = image_gen.generate_face()

    # STT step: user speech to text
    user_input = stt.transcribe(audio_file_path)
    conversation_history.append({"role": "user", "content": user_input})

    # Rebuild chain dynamically from persona
    chain = get_chain(persona_text)

    # Construct prompt from conversation memory
    full_prompt = "\n".join([f"{m['role']}: {m['content']}" for m in conversation_history])

    # LLM reply
    reply = llm_interface.get_response(chain, full_prompt)
    conversation_history.append({"role": "assistant", "content": reply})

    # File paths
    reply_count += 1
    os.makedirs("session_output", exist_ok=True)
    audio_reply_path = f"session_output/reply_{reply_count}.wav"

    # TTS output
    tts.text_to_audio(reply, audio_reply_path)

    # Avatar generation
    video_path = generate_avatar(
        audio_path=audio_reply_path,
        image_path="avatar.jpg"
    )

    return avatar_path, reply, audio_reply_path, video_path

def pipeline(user_input):
    # Step 1: Text to speech
    audio_path = text_to_audio(user_input)  # Save as reply.wav

    # Step 2: Generate avatar video
    video_path = generate_avatar(audio_path=audio_path, image_path="avatar.jpg")

    return video_path  # Gradio Video output will play this

with gr.Blocks() as iface:
    with gr.Row():
        audio_input = gr.Audio(type="filepath", label="Speak or Upload Audio")
        persona_input = gr.Textbox(label="LLM Persona", lines=10, value="""Your name is Olivia Smith...
You work for FriendlySmiles Inc...
You're helpful, professional, etc.""")

    with gr.Row():
        avatar_img = gr.Image(label="Avatar")
        reply_txt = gr.Textbox(label="Assistant")
        reply_audio = gr.Audio(type="filepath", label="Reply Audio")
        reply_vid = gr.Video(label="Avatar Video")

    submit = gr.Button("Submit")

    submit.click(
        fn=chat,
        inputs=[audio_input, persona_input],
        outputs=[avatar_img, reply_txt, reply_audio, reply_vid]
    )

iface.launch()
