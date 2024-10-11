def validate_project_details(project_details: dict) -> bool:
    # Validate if the provided project details meet the criteria
    # This is a placeholder for validation logic
    required_fields = ["project_name", "amount_needed", "duration"]
    for field in required_fields:
        if field not in project_details:
            return False
    return True
