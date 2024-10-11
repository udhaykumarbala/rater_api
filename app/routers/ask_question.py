from fastapi import APIRouter, HTTPException
import app.services.pinecone_knowledge_base as pinecone_kb
import app.services.redis_session as redis_session
import app.utils.llm_integration as llm_integration

router = APIRouter(prefix='/ask', tags=['Ask Question'])

@router.get('/question')
async def ask_question(session_id: str, query: str):
    # Retrieve context from Redis
    context = redis_session.get_session(session_id)
    
    # Query knowledge base and integrate with LLM
    kb_result = pinecone_kb.query_knowledge_base(query)
    response = llm_integration.generate_response(query, context, kb_result)
    
    if not response:
        raise HTTPException(status_code=404, detail='No relevant information found')
    
    return {"session_id": session_id, "response": response}
