

from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16)

pipe.to("cuda")

prompt_deafult = "a photograph of a nigga riding hellcat"

image = pipe(prompt_deafult).images[0]


def generate_image(prompt: str):
    Image = pipe(prompt).images[0]
    return Image 

