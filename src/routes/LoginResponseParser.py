import requests
from src.utils.config import get_settings, Settings

def send_login_request(email, password):
    app_settings = get_settings()
    url = app_settings.LOGIN_RESPONCE_ENDPOINT
    
    payload = {
        "email": email,
        "password": password
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def parse_response(response):
    if isinstance(response, str):  # Error occurred
        print(response)
        return None

    message = response.get('message')
    user_data = response.get('user', {})

    # Extract authentication information
    auth_data = user_data.get('authentication', {})
    password = auth_data.get('password')
    token = auth_data.get('token')
    verified = auth_data.get('verified')

    # Extract user information
    user_id = user_data.get('_id')
    name = user_data.get('name')
    signed_with = user_data.get('signedWith')
    email = user_data.get('email')
    gender = user_data.get('gender')
    age = user_data.get('age')
    weight = user_data.get('weight')
    height = user_data.get('height')
    goal = user_data.get('goal')
    experience = user_data.get('experience')
    body_fat_percentage = user_data.get('bodyFatPercentage')
    muscle_mass = user_data.get('muscleMass')
    workout_duration_preference = user_data.get('workoutDurationPreference')
    workout_frequency_preference = user_data.get('workoutFrequencyPreference')
    preferred_exercise_types = user_data.get('preferredExerciseTypes')
    training_environment_preference = user_data.get('trainingEnvironmentPreference')
    access_to_equipment = user_data.get('accessToEquipment')
    motivation_level = user_data.get('motivationLevel')
    stress_levels = user_data.get('stressLevels')
    version = user_data.get('__v')
    events_joined = user_data.get('eventsJoined')
    StrengthAssessment = user_data.get('StrengthAssessment')
    EnduranceAssessment = user_data.get('EnduranceAssessment')
    FlexibilityAssessment = user_data.get('FlexibilityAssessment')
    PowerAssessment = user_data.get('PowerAssessment')
    StabilizationAssessment = user_data.get('StabilizationAssessment')
    ExcersisAssessments = user_data.get('ExcersisAssessments')

 
    return {
        'user_id': user_id,
        'name': name,
        'email': email,
        'gender': gender,
        'age': age,
        'weight': weight,
        'height': height,
        'goal': goal,
        'experience': experience,
        'body_fat_percentage': body_fat_percentage,
        'muscle_mass': muscle_mass,
        'workout_duration_preference': workout_duration_preference,
        'workout_frequency_preference': workout_frequency_preference,
        'preferred_exercise_types': preferred_exercise_types,
        'training_environment_preference': training_environment_preference,
        'access_to_equipment': access_to_equipment,
        'motivation_level': motivation_level,
        'stress_levels': stress_levels,
        'token': token,
        'StrengthAssessment' :StrengthAssessment,
        'EnduranceAssessment' : EnduranceAssessment,
        'FlexibilityAssessment' : FlexibilityAssessment,
        'PowerAssessment' : PowerAssessment,
        'StabilizationAssessment' : StabilizationAssessment,
        'ExcersisAssessments' : ExcersisAssessments
    }

        

