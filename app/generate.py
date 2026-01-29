from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO

load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
CLIENT = genai.Client(vertexai=True)
MODEL_ID = "imagen-4.0-generate-001"

# prompt = """A robot is bargaining with vegitable vender to buy veggies.
# """

# # generate the image
# result = CLIENT.models.generate_images(
#     model=MODEL_ID,
#     prompt=prompt,
#     config=types.GenerateImagesConfig(
#         aspect_ratio="16:9",
#         number_of_images=1,
#         image_size="1k",
#     ),
# )

# for i, generated_images in enumerate(result.generated_images):
#     image = Image.open(BytesIO(generated_images.image.image_bytes))
#     image.show()


def generate_image(prompt: str, image_size: str = "1k", aspect_ratio: str = "16:9"):
    result = CLIENT.models.generate_images(
        model=MODEL_ID,
        prompt=prompt, 
        config=types.GenerateImagesConfig(
            aspect_ratio=aspect_ratio,
            number_of_images=1,
            image_size=image_size
        )
    )
    return result.generated_images[0].image.image_bytes




