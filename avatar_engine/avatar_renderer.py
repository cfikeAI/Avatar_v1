import subprocess
import os
import sys
import shutil
import glob

def generate_avatar(audio_path, image_path, output_dir="results", reply_count=1):
    python_exe = sys.executable
    sadtalker_dir = os.path.join(os.getcwd(), "SadTalker")

    # Convert both to absolute paths
    audio_abs = os.path.abspath(audio_path)
    image_abs = os.path.abspath(image_path)

    # Ensure files exist
    if not os.path.exists(audio_abs):
        raise FileNotFoundError(f"Audio not found: {audio_abs}")
    if not os.path.exists(image_abs):
        raise FileNotFoundError(f"Image not found: {image_abs}")

    # Get paths relative to SadTalker dir
    audio_rel = os.path.relpath(audio_abs, sadtalker_dir)
    image_rel = os.path.relpath(image_abs, sadtalker_dir)

    cmd = [
        python_exe,
        "inference.py",
        "--driven_audio", audio_rel,
        "--source_image", image_rel,
        "--result_dir", output_dir,
        "--still",
        "--preprocess", "full"
    ]

    # Run inference from inside SadTalker/
    subprocess.run(cmd, cwd=sadtalker_dir, check=True)

    # Locate output
    results_dir = os.path.join(sadtalker_dir, output_dir)
    mp4_files = sorted(
        glob.glob(os.path.join(results_dir, "**", "*.mp4"), recursive=True),
        key=os.path.getmtime
    )

    if not mp4_files:
        raise FileNotFoundError("No video file was found in SadTalker's result directory.")

    latest_video = mp4_files[-1]

    # Copy to session_output
    os.makedirs("session_output", exist_ok=True)
    final_output_path = os.path.abspath(f"session_output/avatar_{reply_count}.mp4")
    shutil.copyfile(latest_video, final_output_path)

    return final_output_path
