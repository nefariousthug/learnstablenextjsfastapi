from fastapi import FastAPI, Response
from io import BytesIO
from fastapi.responses import FileResponse
import services as services
import base64
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials = True,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def read_root():
    return{"message": "welcome to fastable"}

@app.get("/generateimage")
def generateimage(prompt: str):
    image = services.generate_image(prompt)
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    imgstr = base64.b64encode(buffer.getvalue())
    return Response(content=imgstr, media_type="image/png")


