

from src.models.OPTAssessments import OPTPhaseAssessment

class FlexibilityAssessment(OPTPhaseAssessment):
    def __init__(self, user_data):
        super().__init__(user_data)
        self.FLEXIBILITY_TEST_CHART = {
        'male': [
            (27, float('inf'), 'super'),
            (17, 27, 'excellent'),
            (6, 16, 'good'),
            (0, 5, 'average'),
            (-8, -1, 'fair'),
            (-20, -9, 'poor'),
            (float('-inf'), -20, 'very poor')
        ],
        'female': [
            (30, float('inf'), 'super'),
            (21, 30, 'excellent'),
            (11, 20, 'good'),
            (1, 10, 'average'),
            (-7, 0, 'fair'),
            (-15, -8, 'poor'),
            (float('-inf'), -15, 'very poor')
        ]
    }



    def calculate_score(self):
        """
        Calculate the flexibility assessment score based on the recorded user data.
        """
        # Implement the sit_and_reach scoring algorithm for flexibility assessment
        sit_and_reach_distance = self.assessment_data.get('sit_and_reach_distance', 0)

        flexibility_score = sit_and_reach_distance 

        self.score = flexibility_score


    def calculate_level(self):
        gender = self.user_data.get('gender').lower()
        measurement = self.score
        for low, high, rating in self.FLEXIBILITY_TEST_CHART[gender]:
            if low <= measurement <= high:
                self.level = rating
        return "Invalid measurement"


    def run_assessment(self):
        """
        Execute the flexibility assessment phase.
        """
        print("Starting flexibility assessment...")

        # Collect user data for sit-and-reach exercise
        sit_and_reach_distance = float(input("Enter your reach_distance_from the feet (The distance reached by the tip of the fingers in centimeters) for the sit-and-reach test (- for before the feet +for what is after): "))
        self.record_user_data({'sit_and_reach_distance': sit_and_reach_distance})

        # Calculate the flexibility score
        self.calculate_score()

        print(f"Your flexibility assessment score is: {self.get_score()}")
        
        # Calculate the endurance level
        self.calculate_level()
        print(f"Your flexibility assessment level is: {self.get_level()}")
        
        