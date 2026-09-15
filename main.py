"""
You're the engineer responsible for a lightweight internal tool that turns messy weekly quiz-score exports from the LMS into clean, usable student records, 
then ranks students by performance. The exports are inconsistent on purpose: some rows have malformed score data, some are duplicates. 
Your tool has to clean what it can, refuse what it can't, and never crash on a single bad row.
"""

import pandas as pd
import numpy as np


class Student():
    def __init__(self, name: str, scores: []):
        # check if any score is below 0 or above 100 (a numpy array) else raise invalid score error
        # raise InvalidScoreError
        for score in scores:
            if 0 < score > 100: raise InvalidScoreError

        self.name = name
        self.scores = np.array(scores)

    def lock(self):
        pass

    def average(self):
        return np.mean(self.scores)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        raise StudentRecordLockedError()

    def __str__(self):
        return f"Name: {self.name}\nScores: {self.scores}\nAverage: {self.average}"

    def __repr__(self):
        return f"Type: {typeof(self)}\nName: {self.name}\nScores: {self.scores}\nAverage: {self.average}"
    
class InvalidScoreError(Exception):
    def __init(self, score):
        super().__init__("The score is below 0 or above 100. Please enter a valid score")

class StudentRecordLockedError(Exception):
    def __init__(self):
        super().__init__("This student's records are already locked and cannot be changed")

if __name__ == "__main__":
    raw_rows = [
        {"name": " Amara ", "scores": "92,85,78"},
        {"name": "Leo", "scores": "88,91,73"},
        {"name": "Priya", "scores": "65,72,150"},         
        {"name": "Sam", "scores": "70,not_a_number,60"},  
        {"name": "Amara", "scores": "95,90,88"},          
        {"name": "Jade", "scores": "81,77,84,90"},
    ]

    students = pd.DataFrame(raw_rows)
    students["name"] = students["name"].str.strip()

    # use pandas to parse the scores into a proper row
    students["scores"] = pd.to_numeric(students["scores"], errors="coerce")

    students = students.drop_duplicates() # keeps first occurence by default

    # Parse each students df row into a Student object
    
    print(students)



"""
From the scenario, it looks like we need to create a Student class with name and scores as its attributes.
There are specific rules to keep in mind when building this class:
- scores must be between 0 and 100, else an informative error (so either a custom exception or an exception
that we catch and modify the error message via print)
- Once a student record is finalized, it should be locked and immutable. Attempting to 
edit it will result in a custom exception with an informative message. So maybe once we call init once, we create a setter and
add a condition that raises this custom exception.
- Every student also needs overrides for its __str__ and __repr__

In our main flow, we should first clean our data using Pandas
- trim
- parse the score string into numeric values (and we need to coerce invalid values to avoid crashing the flow)
- drop duplicates without including in failures list or printing
- Turn the now-cleaned rows into Student objects, with exception handling
- Every row add (batch builder) must print errors AND success
- calculate student's ave score using numpy ops

Specific class, function, and attribute names are listed in the task details.
"""