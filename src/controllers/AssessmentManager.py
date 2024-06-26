
class AssessmentManager:
    def __init__(self, user_data):
        self.user_data = user_data
        self.level_order = ['Excellent', 'Very Good', 'Above Average', 'Average', 'Below Average', 'Poor', 'Very Poor']
        self.assessments = []
        self.assessment_scores = {}
        self.assessment_levels = {}

    def register_assessment(self, assessment_class):
        """
        Register an assessment phase with the manager.

        Args:
            assessment_class (OPTPhaseAssessment): A class representing an assessment phase.
        """
        assessment = assessment_class(self.user_data)
        self.assessments.append(assessment)

    def run_assessments(self):
        """
        Execute all registered assessment phases.
        """
        for assessment in self.assessments:
            assessment.run_assessment()
            score = assessment.get_score()
            level = assessment.get_level()  
            self.assessment_scores[type(assessment).__name__] = score
            self.assessment_levels[type(assessment).__name__] = level

    def generate_report(self):
        """
        Generate and print a report summarizing the assessment scores and levels.
        """
        print("Assessment Report:")
        print(f"Knowing that level order is {self.level_order}")
        for assessment_name in self.assessment_scores.keys():
            score = self.assessment_scores[assessment_name]
            level = self.assessment_levels[assessment_name]
            print(f"{assessment_name}: Score = {score}, Level = {level}")

    def get_score_for_phase(self, phase_name):
        """
        Get the assessment score for a specific phase.

        Args:
            phase_name (str): Name of the assessment phase.

        Returns:
            float: The assessment score for the specified phase, or None if the phase is not found.
        """
        return self.assessment_scores.get(phase_name)

    def get_level_for_phase(self, phase_name):
        """
        Get the assessment level for a specific phase.

        Args:
            phase_name (str): Name of the assessment phase.

        Returns:
            string: The assessment level for the specified phase, or None if the phase is not found.
        """
        return self.assessment_levels.get(phase_name)
    
    def get_assessment_data(self):
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
                "Score": self.get_score_for_phase(assessment_type),
                "Level": self.get_level_for_phase(assessment_type)
            }
        
        return result