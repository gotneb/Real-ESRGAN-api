from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi import BackgroundTasks
from fastapi.responses import FileResponse

from PIL import Image
from io import BytesIO

from realesrgan.processing import run_model
from utils import save_image, get_timestamp, delete_file

ERROR_IMG_PATH = 'assets/error.png'

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# curl -X POST "http://127.0.0.1:8000/upscale/" -F "img=@filename.jpg" -o ~/Downloads/filename.jpg
@app.post('/upscale/')
async def upscale_image(img: UploadFile, background_tasks: BackgroundTasks):
    img_path = save_image(img.file, filename=get_timestamp())

    try:
        upscaled_img_path = run_model(img_path)
        print(f'Upscaled: {upscaled_img_path}')

        background_tasks.add_task(delete_file, img_path)
        background_tasks.add_task(delete_file, upscaled_img_path)

        return FileResponse(upscaled_img_path)
    except Exception as e:
        print(f'Error while trying upscaling image:\n{e}')
        return FileResponse(ERROR_IMG_PATH)