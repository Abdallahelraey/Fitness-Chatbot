from src.routes.LoginResponseParser import parse_response
import requests
import json
from src.utils.config import get_settings, Settings

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
app_settings = get_settings()
endpoint_url = app_settings.ASSESMENT_ENDPOINT_URL
Authorization_tocken = app_settings.ASSESMENT_ENDPOINT_AUTHORIZATION_TOCKEN
headers = {
    'Authorization': Authorization_tocken,
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




