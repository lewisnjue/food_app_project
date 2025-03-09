#!/bin/bash 
pip3 install -r /app/requirements.txt 
pip3 install torch  --index-url https://download.pytorch.org/whl/cpu

uvicorn src.main:app --host 0.0.0.0 --port 8000 
