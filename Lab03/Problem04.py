class StudentSupportList:
    def __init__(self):
        self.student_ids = []

    def submit_id(self, student_id):
        if student_id not in self.student_ids:
            self.student_ids.append(student_id)
            print(f"Student ID {student_id} submitted successfully.")
        else:
            print(f"Student ID {student_id} already exists!")

class StudentSupportSet:
    def __init__(self):
        self.student_ids = set()

    def submit_id(self, student_id):
        if student_id in self.student_ids: 
            print(f"Student ID {student_id} already exists!")
        else:
            self.student_ids.add(student_id)
            print(f"Student ID {student_id} submitted successfully.")
