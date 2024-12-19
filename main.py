from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO

from realesrgan.processing import run_model
from utils import save_image, get_timestamp, delete_file

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# curl -X POST "http://127.0.0.1:8000/upscale/" -F "img=@input.jpg"
@app.post('/upscale/')
async def upscale_image(img: UploadFile):
    img_file = img.file
    filename = get_timestamp()
    img_path = save_image(img_file, filename=filename)

    try:
        run_model(img_path, filename=filename)
        return {"file_size": img_path}
    except Exception as e:
        return {"error": "Invalid image file", "message": str(e)}
    finally:
        # Add later 'outputs/'
        dirs = ['tmp/']
        for dir in dirs:
            delete_file(f'{dir}/{filename}.jpg')