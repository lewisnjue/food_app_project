from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from cassandra.cqlengine.management import sync_table 
from . import db 
from .model import pipe
from users.models import User 
app = FastAPI()
DB_SESSION = None 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)



@app.get('/')
async def home():
    return {"message": "hello world"}

@app.post("/predict/")
async def create_file(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Sorry, you need to upload an image.")

    try:
        contents = await file.read()

        image = Image.open(io.BytesIO(contents))
        image.verify()  

        image = Image.open(io.BytesIO(contents))

        prediction = pipe(image)

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "prediction": prediction
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail="Sorry, you need to upload a valid image.")

