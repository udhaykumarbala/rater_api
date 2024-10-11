from typing import Optional
from PIL import Image
import pytesseract
import pdfplumber
import docx

def extract_details(file) -> Optional[dict]:
    # Extract details based on the file type
    if file.content_type == 'application/pdf':
        return extract_from_pdf(file)
    elif file.content_type == 'image/jpeg' or file.content_type == 'image/png':
        return extract_from_image(file)
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return extract_from_docx(file)
    # Add other formats as needed
    return None

def extract_from_pdf(file) -> Optional[dict]:
    try:
        with pdfplumber.open(file.file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return process_text(text)
    except:
        return None

def extract_from_image(file) -> Optional[dict]:
    try:
        image = Image.open(file.file)
        text = pytesseract.image_to_string(image)
        return process_text(text)
    except:
        return None

def extract_from_docx(file) -> Optional[dict]:
    try:
        doc = docx.Document(file.file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return process_text(text)
    except:
        return None

def process_text(text: str) -> Optional[dict]:
    # Process the extracted text to get details
    # This is just a placeholder for the actual processing logic
    if "loan" in text.lower():
        return {"organization": "Example Bank", "plans": [{"name": "Plan A", "details": "Loan up to $50000"}]}
    return None
