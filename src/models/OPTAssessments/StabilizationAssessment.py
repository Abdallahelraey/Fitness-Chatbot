

from src.models.OPTAssessments import OPTPhaseAssessment

class StabilizationAssessment(OPTPhaseAssessment):
    def __init__(self, user_data):
        super().__init__(user_data)
        self.STABILIZATION_TEST_CHART = [
            (360, float('inf'), 'Excellent'),
            (240, 360, 'Very Good'),
            (120, 240, 'Above Average'),
            (60, 120, 'Average'),
            (30, 60, 'Below Average'),
            (15, 30, 'Poor'),
            (0, 15, 'Very Poor')
        ]
        
        
    def calculate_score(self):
        """
        Calculate the stabilization assessment score based on the recorded user data.
        """
        # Implement scoring algorithm for stabilization assessment
        plank_time = self.assessment_data.get('plank_time', 0)
        # single_leg_balance_time = self.assessment_data.get('single_leg_balance_time', 0)
        # rotational_score = self.assessment_data.get('rotational_score', 0)

        # Calculate stabilization score based on the recorded data
        stabilization_score = plank_time

        self.score = stabilization_score

    def calculate_level(self):
        """
        Calculate the stabilization level based on the plank time.
        """
        plank_time = self.score
        for low, high, rating in self.STABILIZATION_TEST_CHART:
            if low <= plank_time < high:
                self.level = rating
                return
        self.level = "Invalid measurement"
              
    def run_assessment(self):
        """
        Execute the stabilization assessment phase.
        """
        print("Starting stabilization assessment...")

        # Collect user data for plank exercise
        plank_time = float(input("Enter the time (in min) you held the plank position: "))
        self.record_user_data({'plank_time': plank_time})

        # # Collect user data for single-leg balance exercise
        # single_leg_balance_time = float(input("Enter the time (in seconds) you held the single-leg balance: "))
        # self.record_user_data({'single_leg_balance_time': single_leg_balance_time})

        # # Collect user data for rotational exercise
        # rotational_score = float(input("Enter your score (0-10) for the rotational exercise: "))
        # self.record_user_data({'rotational_score': rotational_score})

        # Calculate the stabilization score
        self.calculate_score()

        print(f"Your stabilization assessment score is: {self.get_score()}")
        
        # Calculate the stabilization level
        self.calculate_level()
        print(f"Your stabilization assessment level is: {self.get_level()}")