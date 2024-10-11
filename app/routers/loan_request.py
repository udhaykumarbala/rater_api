from fastapi import APIRouter, HTTPException
import app.utils.validation as validation
import app.services.redis_session as redis_session
import app.utils.llm_integration as llm_integration

router = APIRouter(prefix='/loan', tags=['Loan Request'])

@router.post('/request')
async def loan_request(session_id: str, project_details: dict):
    # Validate project details
    valid_data = validation.validate_project_details(project_details)
    if not valid_data:
        raise HTTPException(status_code=400, detail='Invalid project details')
    
    # Store available details in Redis
    redis_session.store_session(session_id, project_details)
    
    # Generate loan request in markdown format
    loan_request_md = llm_integration.generate_loan_request(project_details)
    
    return {"session_id": session_id, "message": "Loan request details captured", "loan_request": loan_request_md}
