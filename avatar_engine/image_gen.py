# image_gen.py
from diffusers import StableDiffusionPipeline
from gfpgan import GFPGANer
import cv2
import torch
import os

# Load better model for face generation
pipe = StableDiffusionPipeline.from_pretrained(
    "SG161222/Realistic_Vision_V5.1_noVAE", torch_dtype=torch.float16
).to("cuda")

def generate_face(prompt):
    print(f"[Image Gen] Generating avatar with prompt: {prompt}")

    result = pipe(prompt, num_inference_steps=50, guidance_scale=12.0)

    if not result or not hasattr(result, "images") or not result.images:
        raise RuntimeError("Stable Diffusion failed to produce any images.")

    image = result.images[0]

    # Absolute root path
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    raw_path = os.path.join(root_dir, "avatar_raw.jpg")
    output_path = os.path.join(root_dir, "avatar.jpg")

    # Save raw image temporarily
    image.save(raw_path)

    # Enhance face using GFPGAN
    print("[Image Gen] Enhancing face with GFPGAN...")
    gfpganer = GFPGANer(
        model_path=os.path.join(root_dir, "gfpgan/weights/GFPGANv1.4.pth"),
        upscale=2,
        arch='clean',
        channel_multiplier=2,
        bg_upsampler=None
)


    img = cv2.imread(raw_path, cv2.IMREAD_COLOR)
    _, _, enhanced_img = gfpganer.enhance(
        img,
        has_aligned=False,
        only_center_face=True,
        paste_back=True
    )

    # Save final enhanced image
    cv2.imwrite(output_path, enhanced_img)
    print(f"[Image Gen] Final avatar saved to: {output_path}")

    return output_path


generate_face("A friendly AI assistant avatar, a professional woman smiling, centered portrait, standing,corporate attire, warm and inviting, grocery store theme, high detail, professional look")
print("[Image Gen] Avatar generation complete.")
