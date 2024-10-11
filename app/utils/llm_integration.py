def generate_response(query: str, context: dict, kb_result: dict) -> str:
    # Combine the context with knowledge base result and query
    # Pass the combined information to LLM to generate a response
    # This is a placeholder for LLM interaction logic
    combined_context = f"Context: {context}, Knowledge: {kb_result}, Query: {query}"
    response = f"Generated response based on {combined_context}"
    return response

def generate_loan_request(project_details: dict) -> str:
    # Generate loan request details in markdown format
    loan_request_md = f"### Loan Request\n"
    for key, value in project_details.items():
        loan_request_md += f"- **{key}**: {value}\n"
    return loan_request_md
