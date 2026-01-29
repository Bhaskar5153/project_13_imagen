from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from app.generate import generate_image
import os, uuid

app = FastAPI()

@app.post("/generate-image/")
async def generate_image_api(prompt: str = Form(...)):
    images_bytes = generate_image(prompt=prompt)

    #save the image in images folder
    os.makedirs("images", exist_ok=True)
    filename = f"images/{uuid.uuid4().hex}.png"
    with open(filename, mode='wb') as f:
        f.write(images_bytes)
    
    return {"file_path": filename}
