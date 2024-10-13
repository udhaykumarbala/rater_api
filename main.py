import io
import redis
from fastapi import FastAPI, UploadFile, File
from pdf2image import convert_from_bytes
from tesserocr import PyTessBaseAPI
from PIL import Image

# Initialize Redis connection
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

# Define the tessdata path (this is where tessdata is typically installed)
TESSDATA_PATH = "/usr/share/tesseract-ocr/5/tessdata"

app = FastAPI()

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Read the uploaded PDF file
    pdf_bytes = await file.read()

    # Convert PDF to images
    images = convert_from_bytes(pdf_bytes)

    # Initialize OCR
    extracted_text = ""
    with PyTessBaseAPI(path=TESSDATA_PATH) as api:
        for image in images:
            api.SetImage(image)
            extracted_text += api.GetUTF8Text() + "\n"

    # Store the extracted text in Redis
    redis_client.set(file.filename, extracted_text)

    return {"filename": file.filename, "message": "Text extracted and stored in Redis", "text":extracted_text}
