

from src.models.OPTAssessments import OPTPhaseAssessment

class EnduranceAssessment(OPTPhaseAssessment):
    def __init__(self, user_data):
        super().__init__(user_data)


    def calculate_vo2_max(self, distance):
        """
        Calculate VO2 max using the Cooper test formula.
        """
        # Implement the vo2_max scoring algorithm for Endurance assessment
        # Cooper test formula: VO2 max = (distance in meters - 504.9) / 44.73
        vo2_max = (distance - 504.9) / 44.73
        return vo2_max



    def calculate_score(self):
        """
        Calculate the endurance assessment score based on the recorded user data.
        """
        # Retrieve data
        running_distance = self.assessment_data.get('running_distance', 0)
        # Calculate VO2 max for running and cycling
        endurance_score = self.calculate_vo2_max(running_distance)

        self.score = endurance_score
        
    def calculate_level(self):
        super().calculate_VO2_MAX_level()


    def run_assessment(self):
        """
        Execute the endurance assessment phase.
        """
        print("Starting endurance assessment...")

        # Collect user data for running
        running_distance = float(input("Enter the distance (in meters) you ran for 12 minutes: "))
        running_time = 12
        self.record_user_data({'running_distance': running_distance, 'running_time': running_time})
        age = int(self.user_data.get("age"))
        self.record_user_data({'age': age})
        # Calculate the endurance score
        self.calculate_score()

        print(f"Your endurance assessment score is: {self.get_score()}")


        # Calculate the endurance level
        self.calculate_level()
        print(f"Your endurance assessment level is: {self.get_level()}")