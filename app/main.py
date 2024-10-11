from fastapi import FastAPI
from app.routers import lender_upload, ask_question, loan_request

app = FastAPI()

# Including Routers
app.include_router(lender_upload.router)
app.include_router(ask_question.router)
app.include_router(loan_request.router)

@app.get('/')
def read_root():
    return {"message": "Welcome to Rater API!"}