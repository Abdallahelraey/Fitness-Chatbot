class UserProfile:
    def __init__(self, user_id: int, name: str, age: int, gender: str, email: str, password: str,
                 height: float, weight: float, fitness_level: str, fitness_goals: str = "General Health",
                 workout_history: list[str] = None, preferences: dict[str, int] = None,
                 medical_conditions: list[str] = None, body_fat_percentage: float = None, 
                 muscle_mass: float = None, workout_duration_preference: str = None, 
                 workout_frequency_preference: str = None, preferred_exercise_types: str = None, 
                 training_environment_preference: str = None, access_to_equipment: str = None, 
                 motivation_level: str = None, stress_levels: int = None, 
                 endurance_assessment: dict[str, any] = None, strength_assessment: dict[str, any] = None, 
                 flexibility_assessment: dict[str, any] = None, power_assessment: dict[str, any] = None, 
                 stabilization_assessment: dict[str, any] = None, exercise_assessments: dict[str, dict[str, any]] = None):
        
        self._user_id = user_id
        self._name = name
        self._age = age
        self._gender = gender
        self._email = email
        self._password = password
        self._height = height
        self._weight = weight
        self._fitness_level = fitness_level
        self._fitness_goals = fitness_goals
        self._workout_history = workout_history or []
        self._preferences = preferences or {}
        self._medical_conditions = medical_conditions or []
        self._body_fat_percentage = body_fat_percentage
        self._muscle_mass = muscle_mass
        self._workout_duration_preference = workout_duration_preference
        self._workout_frequency_preference = workout_frequency_preference
        self._preferred_exercise_types = preferred_exercise_types
        self._training_environment_preference = training_environment_preference
        self._access_to_equipment = access_to_equipment
        self._motivation_level = motivation_level
        self._stress_levels = stress_levels
        self._endurance_assessment = endurance_assessment or {}
        self._strength_assessment = strength_assessment or {}
        self._flexibility_assessment = flexibility_assessment or {}
        self._power_assessment = power_assessment or {}
        self._stabilization_assessment = stabilization_assessment or {}
        self._exercise_assessments = exercise_assessments or {}

        self._bmr = self._calculate_bmr()
        self._bmi = self._calculate_bmi()

    def _calculate_bmr(self):
        if self._weight is not None and self._height is not None:
            if self._gender.lower() == 'male':
                return 88.362 + (13.397 * self._weight) + (4.799 * self._height) - (5.677 * self._age)
            elif self._gender.lower() == 'female':
                return 447.593 + (9.247 * self._weight) + (3.098 * self._height) - (4.330 * self._age)
        return None

    def _calculate_bmi(self):
        if self._weight is not None and self._height is not None:
            return self._weight / ((self._height / 100) ** 2)
        return None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if value < 0:
            raise ValueError("User ID must be a positive integer")
        self._user_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value.lower() not in ['male', 'female']:
            raise ValueError("Gender must be 'male' or 'female'")
        self._gender = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty")
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not value:
            raise ValueError("Password cannot be empty")
        self._password = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value is not None and value <= 0:
            raise ValueError("Height must be a positive number")
        self._height = value
        self._bmr = self._calculate_bmr()
        self._bmi = self._calculate_bmi()

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value is not None and value <= 0:
            raise ValueError("Weight must be a positive number")
        self._weight = value
        self._bmr = self._calculate_bmr()
        self._bmi = self._calculate_bmi()

    @property
    def fitness_level(self):
        return self._fitness_level

    @fitness_level.setter
    def fitness_level(self, value):
        if not value:
            raise ValueError("Fitness level cannot be empty")
        self._fitness_level = value

    @property
    def fitness_goals(self):
        return self._fitness_goals

    @fitness_goals.setter
    def fitness_goals(self, value):
        if not value:
            raise ValueError("Fitness goals cannot be empty")
        self._fitness_goals = value

    @property
    def workout_history(self):
        return self._workout_history

    @workout_history.setter
    def workout_history(self, value):
        if not isinstance(value, list):
            raise ValueError("Workout history must be a list")
        self._workout_history = value

    @property
    def preferences(self):
        return self._preferences

    @preferences.setter
    def preferences(self, value):
        if not isinstance(value, dict):
            raise ValueError("Preferences must be a dictionary")
        self._preferences = value

    @property
    def medical_conditions(self):
        return self._medical_conditions

    @medical_conditions.setter
    def medical_conditions(self, value):
        if not isinstance(value, list):
            raise ValueError("Medical conditions must be a list")
        self._medical_conditions = value

    @property
    def body_fat_percentage(self):
        return self._body_fat_percentage

    @body_fat_percentage.setter
    def body_fat_percentage(self, value):
        if value is not None and (value < 0 or value > 100):
            raise ValueError("Body fat percentage must be between 0 and 100")
        self._body_fat_percentage = value

    @property
    def muscle_mass(self):
        return self._muscle_mass

    @muscle_mass.setter
    def muscle_mass(self, value):
        if value is not None and value <= 0:
            raise ValueError("Muscle mass must be a positive number")
        self._muscle_mass = value

    @property
    def workout_duration_preference(self):
        return self._workout_duration_preference

    @workout_duration_preference.setter
    def workout_duration_preference(self, value):
        if not value:
            raise ValueError("Workout duration preference cannot be empty")
        self._workout_duration_preference = value

    @property
    def workout_frequency_preference(self):
        return self._workout_frequency_preference

    @workout_frequency_preference.setter
    def workout_frequency_preference(self, value):
        if not value:
            raise ValueError("Workout frequency preference cannot be empty")
        self._workout_frequency_preference = value

    @property
    def preferred_exercise_types(self):
        return self._preferred_exercise_types

    @preferred_exercise_types.setter
    def preferred_exercise_types(self, value):
        if not value:
            raise ValueError("Preferred exercise types cannot be empty")
        self._preferred_exercise_types = value

    @property
    def training_environment_preference(self):
        return self._training_environment_preference

    @training_environment_preference.setter
    def training_environment_preference(self, value):
        if not value:
            raise ValueError("Training environment preference cannot be empty")
        self._training_environment_preference = value

    @property
    def access_to_equipment(self):
        return self._access_to_equipment

    @access_to_equipment.setter
    def access_to_equipment(self, value):
        if not value:
            raise ValueError("Access to equipment cannot be empty")
        self._access_to_equipment = value

    @property
    def motivation_level(self):
        return self._motivation_level

    @motivation_level.setter
    def motivation_level(self, value):
        if not value:
            raise ValueError("Motivation level cannot be empty")
        self._motivation_level = value

    @property
    def stress_levels(self):
        return self._stress_levels

    @stress_levels.setter
    def stress_levels(self, value):
        if value is not None and (value < 0 or value > 10):
            raise ValueError("Stress levels must be between 0 and 10")
        self._stress_levels = value

    @property
    def endurance_assessment(self):
        return self._endurance_assessment

    @endurance_assessment.setter
    def endurance_assessment(self, value):
        if not isinstance(value, dict):
            raise ValueError("Endurance assessment must be a dictionary")
        self._endurance_assessment = value

    @property
    def strength_assessment(self):
        return self._strength_assessment

    @strength_assessment.setter
    def strength_assessment(self, value):
        if not isinstance(value, dict):
            raise ValueError("Strength assessment must be a dictionary")
        self._strength_assessment = value

    @property
    def flexibility_assessment(self):
        return self._flexibility_assessment

    @flexibility_assessment.setter
    def flexibility_assessment(self, value):
        if not isinstance(value, dict):
            raise ValueError("Flexibility assessment must be a dictionary")
        self._flexibility_assessment = value

    @property
    def power_assessment(self):
        return self._power_assessment

    @power_assessment.setter
    def power_assessment(self, value):
        if not isinstance(value, dict):
            raise ValueError("Power assessment must be a dictionary")
        self._power_assessment = value

    @property
    def stabilization_assessment(self):
        return self._stabilization_assessment

    @stabilization_assessment.setter
    def stabilization_assessment(self, value):
        if not isinstance(value, dict):
            raise ValueError("Stabilization assessment must be a dictionary")
        self._stabilization_assessment = value

    @property
    def exercise_assessments(self):
        return self._exercise_assessments

    @exercise_assessments.setter
    def exercise_assessments(self, value):
        if not isinstance(value, dict):
            raise ValueError("Exercise assessments must be a dictionary of dictionaries")
        self._exercise_assessments = value

    @property
    def bmr(self):
        return self._bmr

    @property
    def bmi(self):
        return self._bmi

    def assess_bmi_category(self):
        if self._age >= 18 and self._bmi is not None:
            if 18.5 <= self._bmi < 24.9:
                return "Normal"
            elif 25 <= self._bmi < 29.9:
                return "Overweight"
            elif self._bmi >= 30:
                return "Obese"
            else:
                return "Underweight"
        return "Assessment not applicable"

    def set_fitness_goals(self, fitness_goals: str):
        self.fitness_goals = fitness_goals

    def set_preferences(self, duration: int, intensity: int, frequency: int):
        self.preferences['duration'] = duration
        self.preferences['intensity'] = intensity
        self.preferences['frequency'] = frequency

    def get_profile_info(self):
        return (f"User Profile for {self._name}: Age: {self._age}, Gender: {self._gender}, "
                f"Fitness Goals: {self._fitness_goals}, BMR: {self._bmr:.2f}, BMI: {self._bmi:.2f}")

    def to_dict(self):
        return {
            'user_id': self._user_id,
            'name': self._name,
            'age': self._age,
            'gender': self._gender,
            'email': self._email,
            'password': self._password,
            'height': self._height,
            'weight': self._weight,
            'fitness_level': self._fitness_level,
            'fitness_goals': self._fitness_goals,
            'workout_history': self._workout_history,
            'preferences': self._preferences,
            'medical_conditions': self._medical_conditions,
            'body_fat_percentage': self._body_fat_percentage,
            'muscle_mass': self._muscle_mass,
            'workout_duration_preference': self._workout_duration_preference,
            'workout_frequency_preference': self._workout_frequency_preference,
            'preferred_exercise_types': self._preferred_exercise_types,
            'training_environment_preference': self._training_environment_preference,
            'access_to_equipment': self._access_to_equipment,
            'motivation_level': self._motivation_level,
            'stress_levels': self._stress_levels,
            'endurance_assessment': self._endurance_assessment,
            'strength_assessment': self._strength_assessment,
            'flexibility_assessment': self._flexibility_assessment,
            'power_assessment': self._power_assessment,
            'stabilization_assessment': self._stabilization_assessment,
            'exercise_assessments': self._exercise_assessments,
            'bmr': self._bmr,
            'bmi': self._bmi
        }

    def __str__(self):
        return self.get_profile_info()

    def __repr__(self):
        return (f"UserProfile(user_id={self._user_id}, name={self._name}, age={self._age}, gender={self._gender}, "
                f"email={self._email}, password={self._password}, height={self._height}, weight={self._weight}, "
                f"fitness_level={self._fitness_level}, fitness_goals={self._fitness_goals}, workout_history={self._workout_history}, "
                f"preferences={self._preferences}, medical_conditions={self._medical_conditions}, body_fat_percentage={self._body_fat_percentage}, "
                f"muscle_mass={self._muscle_mass}, workout_duration_preference={self._workout_duration_preference}, "
                f"workout_frequency_preference={self._workout_frequency_preference}, preferred_exercise_types={self._preferred_exercise_types}, "
                f"training_environment_preference={self._training_environment_preference}, access_to_equipment={self._access_to_equipment}, "
                f"motivation_level={self._motivation_level}, stress_levels={self._stress_levels}, endurance_assessment={self._endurance_assessment}, "
                f"strength_assessment={self._strength_assessment}, flexibility_assessment={self._flexibility_assessment}, "
                f"power_assessment={self._power_assessment}, stabilization_assessment={self._stabilization_assessment}, "
                f"exercise_assessments={self._exercise_assessments}, bmr={self._bmr}, bmi={self._bmi})")
