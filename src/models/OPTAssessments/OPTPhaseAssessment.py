

class OPTPhaseAssessment:




    def __init__(self, user_data):
        self.user_data = user_data
        self.assessment_data = {}
        self.score = None
        self.level = None
        self.VO2_MAX_CHART = {
        'male': {
            (18, 25): {'excellent': 60, 'good': 52, 'above_avg': 47, 'average': 42, 'below_avg': 37, 'poor': 30},
            (26, 35): {'excellent': 56, 'good': 49, 'above_avg': 43, 'average': 40, 'below_avg': 35, 'poor': 30},
            (36, 45): {'excellent': 51, 'good': 43, 'above_avg': 39, 'average': 35, 'below_avg': 31, 'poor': 26},
            (46, 55): {'excellent': 45, 'good': 39, 'above_avg': 36, 'average': 32, 'below_avg': 29, 'poor': 25},
            (56, 65): {'excellent': 41, 'good': 36, 'above_avg': 32, 'average': 30, 'below_avg': 26, 'poor': 22},
            (66, 200): {'excellent': 37, 'good': 33, 'above_avg': 29, 'average': 26, 'below_avg': 22, 'poor': 20}
        },
        'female': {
            (18, 25): {'excellent': 56, 'good': 47, 'above_avg': 42, 'average': 38, 'below_avg': 33, 'poor': 28},
            (26, 35): {'excellent': 52, 'good': 45, 'above_avg': 39, 'average': 35, 'below_avg': 31, 'poor': 26},
            (36, 45): {'excellent': 45, 'good': 38, 'above_avg': 34, 'average': 31, 'below_avg': 27, 'poor': 22},
            (46, 55): {'excellent': 40, 'good': 34, 'above_avg': 31, 'average': 28, 'below_avg': 25, 'poor': 20},
            (56, 65): {'excellent': 37, 'good': 32, 'above_avg': 28, 'average': 25, 'below_avg': 22, 'poor': 18},
            (66, 200): {'excellent': 32, 'good': 28, 'above_avg': 25, 'average': 22, 'below_avg': 19, 'poor': 17}
        }
    }

    def record_user_data(self, data):
        """
        Record user data for the assessment phase.
        
        Args:
            data (dict): A dictionary containing user data relevant to the assessment phase.
        """
        self.assessment_data.update(data)

    def calculate_score(self):
        """
        Calculate the assessment score based on the recorded user data.
        
        This method should be overridden in the derived classes for each specific assessment phase.
        """
        raise NotImplementedError("calculate_score method must be implemented in the derived class.")

    def get_score(self):
        """
        Return the calculated assessment score.
        
        Returns:
            float: The assessment score, or None if the score has not been calculated yet.
        """
        return self.score

    def get_level(self):
        """
        Return the calculated assessment score.
        
        Returns:
            float: The assessment score, or None if the score has not been calculated yet.
        """
        return self.level


    def run_assessment(self):
        """
        Execute the assessment phase.
        
        This method should be overridden in the derived classes for each specific assessment phase.
        It should handle the necessary steps to collect user data, perform calculations, and store the assessment score.
        """
        raise NotImplementedError("run_assessment method must be implemented in the derived class.")
    
    def calculate_VO2_MAX_level(self):
        """
        Determine the endurance level (beginner, intermediate, advanced) based on the VO2 max.
        """
        if self.score is None:
            raise ValueError("Score has not been calculated yet.")

        gender = self.user_data.get('gender').lower()
        age = self.assessment_data.get('age', 0)
        vo2_max = self.score

        age_group = None
        for (start_age, end_age), _ in self.VO2_MAX_CHART[gender].items():
            if start_age <= age <= end_age:
                age_group = (start_age, end_age)
                break

        if age_group is None:
            raise ValueError("Age group not found.")

        levels = self.VO2_MAX_CHART[gender][age_group]
        if self.score >= levels['excellent']:
            self.level = "Excellent"
        elif self.score >= levels['good']:
            self.level = "Good"
        elif self.score >= levels['above_avg']:
            self.level = "Above Average"
        elif self.score >= levels['average']:
            self.level = "Average"
        elif self.score >= levels['below_avg']:
            self.level = "Below Average"
        elif self.score >= levels['poor']:
            self.level = "Poor"
        else:
            self.level = "Very Poor"