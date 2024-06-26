

from src.models.OPTAssessments import OPTPhaseAssessment

class PowerAssessment(OPTPhaseAssessment):
    def __init__(self, user_data):
        super().__init__(user_data)
        self.POWER_TEST_CHART = {
            'male': [
                (70, float('inf'), 'excellent'),
                (61, 70, 'very good'),
                (51, 60, 'above average'),
                (41, 50, 'average'),
                (31, 40, 'below average'),
                (21, 30, 'poor'),
                (float('-inf'), 20, 'very poor')
            ],
            'female': [
                (60, float('inf'), 'excellent'),
                (51, 60, 'very good'),
                (41, 50, 'above average'),
                (31, 40, 'average'),
                (21, 30, 'below average'),
                (11, 20, 'poor'),
                (float('-inf'), 10, 'very poor')
            ]
        }

    def calculate_score(self):
        """
        Calculate the power assessment score based on the recorded user data.
        """
        # Implement scoring algorithm for power assessment
        vertical_jump = self.assessment_data.get('vertical_jump', 0)

        # Calculate power score based on the recorded data
        power_score = vertical_jump 

        self.score = power_score
        
        
    def calculate_level(self):
        gender = self.user_data.get('gender').lower()
        measurement = self.score
        for low, high, rating in self.POWER_TEST_CHART[gender]:
            if low <= measurement < high:
                self.level = rating
                return
        self.level = "Invalid measurement"


    def run_assessment(self):
        """
        Execute the power assessment phase.
        """
        print("Starting power assessment...")

        # Collect user data for vertical jump
        vertical_jump = float(input("Enter your vertical jump height (in Cm): "))
        self.record_user_data({'vertical_jump': vertical_jump})

        # Calculate the power score
        self.calculate_score()

        print(f"Your power assessment score is: {self.get_score()}")
                
        # Calculate the power level
        self.calculate_level()
        print(f"Your power assessment level is: {self.get_level()}")