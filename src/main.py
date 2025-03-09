from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from .model import pipe 
app = FastAPI()



@app.get('/')
async def home():
    return {"messange":"hello world"}


@app.post('/predict')

async def predict_image():
    return {...}
    
