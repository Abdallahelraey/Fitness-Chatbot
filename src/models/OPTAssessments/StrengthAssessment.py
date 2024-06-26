

from src.models.OPTAssessments import OPTPhaseAssessment

class StrengthAssessment(OPTPhaseAssessment):
    def __init__(self, user_data):
        super().__init__(user_data)
        self.PUSHUP_TEST_CHART = {
            'male': {
                '17-19': [(56, float('inf'), 'Excellent'), (47, 56, 'Good'), (35, 47, 'Above Average'), (19, 35, 'Average'), (11, 19, 'Below Average'), (4, 11, 'Poor'), (0, 4, 'Very Poor')],
                '20-29': [(47, float('inf'), 'Excellent'), (39, 47, 'Good'), (30, 39, 'Above Average'), (17, 30, 'Average'), (10, 17, 'Below Average'), (4, 10, 'Poor'), (0, 4, 'Very Poor')],
                '30-39': [(41, float('inf'), 'Excellent'), (34, 41, 'Good'), (25, 34, 'Above Average'), (13, 25, 'Average'), (8, 13, 'Below Average'), (2, 8, 'Poor'), (0, 2, 'Very Poor')],
                '40-49': [(34, float('inf'), 'Excellent'), (28, 34, 'Good'), (21, 28, 'Above Average'), (11, 21, 'Average'), (6, 11, 'Below Average'), (1, 6, 'Poor'), (0, 1, 'Very Poor')],
                '50-59': [(31, float('inf'), 'Excellent'), (25, 31, 'Good'), (18, 25, 'Above Average'), (9, 18, 'Average'), (5, 9, 'Below Average'), (1, 5, 'Poor'), (0, 1, 'Very Poor')],
                '60-65': [(30, float('inf'), 'Excellent'), (24, 30, 'Good'), (17, 24, 'Above Average'), (6, 17, 'Average'), (3, 6, 'Below Average'), (1, 3, 'Poor'), (0, 1, 'Very Poor')]
            },
            'female': {
                '17-19': [(30, float('inf'), 'Excellent'), (22, 30, 'Good'), (11, 22, 'Above Average'), (7, 11, 'Average'), (4, 7, 'Below Average'), (1, 4, 'Poor'), (0, 1, 'Very Poor')],
                '20-29': [(32, float('inf'), 'Excellent'), (24, 32, 'Good'), (14, 24, 'Above Average'), (9, 14, 'Average'), (5, 9, 'Below Average'), (1, 5, 'Poor'), (0, 1, 'Very Poor')],
                '30-39': [(28, float('inf'), 'Excellent'), (21, 28, 'Good'), (13, 21, 'Above Average'), (7, 13, 'Average'), (3, 7, 'Below Average'), (1, 3, 'Poor'), (0, 1, 'Very Poor')],
                '40-49': [(20, float('inf'), 'Excellent'), (15, 20, 'Good'), (10, 15, 'Above Average'), (5, 10, 'Average'), (2, 5, 'Below Average'), (1, 2, 'Poor'), (0, 1, 'Very Poor')],
                '50-59': [(16, float('inf'), 'Excellent'), (13, 16, 'Good'), (9, 13, 'Above Average'), (4, 9, 'Average'), (2, 4, 'Below Average'), (1, 2, 'Poor'), (0, 1, 'Very Poor')],
                '60-65': [(12, float('inf'), 'Excellent'), (10, 12, 'Good'), (6, 10, 'Above Average'), (3, 6, 'Average'), (1, 3, 'Below Average'), (1, 1, 'Poor'), (0, 1, 'Very Poor')]
            }
        }
        
    def calculate_score(self):
        """
        Calculate the strength assessment score based on the recorded user data.
        """
        # Implement scoring algorithm for strength assessment
        pushups = self.assessment_data.get('pushups', 0)
        # squats = self.assessment_data.get('squats', 0)
        # bench_press = self.assessment_data.get('bench_press', 0)
        # deadlift = self.assessment_data.get('deadlift', 0)

        # Calculate strength score based on the recorded data
        strength_score = pushups 

        self.score = strength_score

    def calculate_level(self):
        """
        Calculate the strength level based on the number of pushups, gender, and age group.
        """
        gender = self.user_data.get('gender', '').lower()
        age = self.user_data.get('age', 0)
        pushups = self.score

        # Determine age group
        if 17 <= age <= 19:
            age_group = '17-19'
        elif 20 <= age <= 29:
            age_group = '20-29'
        elif 30 <= age <= 39:
            age_group = '30-39'
        elif 40 <= age <= 49:
            age_group = '40-49'
        elif 50 <= age <= 59:
            age_group = '50-59'
        elif 60 <= age <= 65:
            age_group = '60-65'
        else:
            self.level = "Age out of range for assessment"
            return

        # Determine level based on pushups
        if gender in self.PUSHUP_TEST_CHART and age_group in self.PUSHUP_TEST_CHART[gender]:
            for low, high, rating in self.PUSHUP_TEST_CHART[gender][age_group]:
                if low <= pushups < high:
                    self.level = rating
                    return
        
        # If no matching level is found
        self.level = "Invalid measurement"

    def run_assessment(self):
        """
        Execute the strength assessment phase.
        """
        print("Starting strength assessment...")

        # Collect user data for pushups
        pushups = int(input("Enter the number of pushups you completed: "))
        self.record_user_data({'pushups': pushups})

        # # Collect user data for squats
        # squats = int(input("Enter the number of squats you completed: "))
        # self.record_user_data({'squats': squats})

        # # Collect user data for bench press
        # bench_press = float(input("Enter the maximum weight (in lbs) you benched: "))
        # self.record_user_data({'bench_press': bench_press})

        # # Collect user data for deadlift
        # deadlift = float(input("Enter the maximum weight (in lbs) you deadlifted: "))
        # self.record_user_data({'deadlift': deadlift})

        # Calculate the strength score
        self.calculate_score()

        print(f"Your strength assessment score is: {self.get_score()}")
        
        # Calculate the strength level
        self.calculate_level()
        print(f"Your strength assessment level is: {self.get_level()}")