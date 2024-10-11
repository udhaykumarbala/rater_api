from fastapi import APIRouter, File, UploadFile, HTTPException
import app.services.aws_s3 as aws_s3
import app.services.redis_session as redis_session
import app.utils.text_extraction as text_extraction

router = APIRouter(prefix='/lender', tags=['Lender Upload'])

@router.post('/upload')
async def upload_lender_sheet(session_id: str, file: UploadFile = File(...)):
    # Validate and extract details from the uploaded file
    extracted_details = text_extraction.extract_details(file)
    if not extracted_details:
        raise HTTPException(status_code=400, detail='Invalid loan sheet')
    
    # Upload file to S3
    s3_url = aws_s3.upload_file(file)
    
    # Store context in Redis
    redis_session.store_session(session_id, extracted_details)
    
    return {"session_id": session_id, "message": "File processed and uploaded", "summary": extracted_details}
