class UserProfile:
    def __init__(self, user_id: int, age: int, gender: str, name: str,
                 fitness_level: str, fitness_goals: str = "General Health",
                 workout_history: list[str] = None, preferences: dict[str, int] = None,
                 medical_conditions: list[str] = None, weight: float = None, height: float = None):
        self._user_id = user_id
        self._age = age
        self._gender = gender
        self._name = name
        self._weight = weight
        self._height = height
        self._fitness_level = fitness_level
        self._fitness_goals = fitness_goals
        self._workout_history = workout_history or []
        self._preferences = preferences or {}
        self._medical_conditions = medical_conditions or []
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
        if value not in ['male', 'female']:
            raise ValueError("Gender must be 'male' or 'female'")
        self._gender = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

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
            'age': self._age,
            'gender': self._gender,
            'name': self._name,
            'weight': self._weight,
            'height': self._height,
            'fitness_level': self._fitness_level,
            'fitness_goals': self._fitness_goals,
            'workout_history': self._workout_history,
            'preferences': self._preferences,
            'medical_conditions': self._medical_conditions,
            'bmr': self._bmr,
            'bmi': self._bmi
        }

    def __str__(self):
        return self.get_profile_info()

    def __repr__(self):
        return (f"UserProfile(user_id={self._user_id}, age={self._age}, gender={self._gender}, "
                f"name={self._name}, weight={self._weight}, height={self._height}, "
                f"fitness_level={self._fitness_level}, fitness_goals={self._fitness_goals}, "
                f"workout_history={self._workout_history}, preferences={self._preferences}, "
                f"medical_conditions={self._medical_conditions}, bmr={self._bmr}, bmi={self._bmi})")
