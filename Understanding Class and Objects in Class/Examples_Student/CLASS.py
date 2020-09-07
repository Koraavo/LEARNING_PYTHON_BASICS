class Student:
    def __init__(self, name, subject, test_scores):
        self.name = name
        self.subject = subject
        self.test_scores = test_scores

    def on_honor_roll(self):
        if self.test_scores >= 90:
            return True
        else:
            return False

