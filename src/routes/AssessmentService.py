from src.routes.LoginResponseParser import parse_response
import requests
import json


def get_assessment_data(assessment_manager):
    assessment_types = [
        "StrengthAssessment",
        "EnduranceAssessment",
        "FlexibilityAssessment",
        "PowerAssessment",
        "StabilizationAssessment"
    ]
    
    result = {}
    
    for assessment_type in assessment_types:
        result[assessment_type] = {
            "Score": assessment_manager.get_score_for_phase(assessment_type),
            "Level": assessment_manager.get_level_for_phase(assessment_type)
        }
    
    return result

# Endpoint URL and Authorization Token
endpoint_url = "https://x-fit-backend-graduation-project.onrender.com/api/v1/user/updateUserAssessment"
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOiI2NWZkOTllNDgwYWEwMzgzNDUwZjZlMjIiLCJuYW1lIjoiU2FhZCBIdXNzZWluIiwiZGF0ZSI6IldlZCBKdW4gMjYgMjAyNCAwODo0MzoyMSBHTVQrMDAwMCAoQ29vcmRpbmF0ZWQgVW5pdmVyc2FsIFRpbWUpIiwiaWF0IjoxNzE5MzkxNDAxfQ.cM5Fo5-Etaio5ecqmWa9EMuG0EjhR7brr2tl82rfdjc',
    'Content-Type': 'application/json'
}

# Function to send data to endpoint
def send_assessment_data(assessment_manager):
    assessment_data = get_assessment_data(assessment_manager)

    response = requests.post(endpoint_url, json=assessment_data, headers=headers)
    response = response.content
    response = response.decode('utf-8')  # Convert bytes to string
    response = json.loads(response)  # Parse JSON string
    parsed_response = parse_response(response)
    return parsed_response




