class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        c = len(self.marks)
        t = sum(self.marks)
        try:
            return t/c
        except:
            print("An error occured")

    @staticmethod
    def go_to_school():
        print(f"I'm going to school")
        # print(f"I'm a {cls}")
        # print(f"I'm going to {self.school}")

    # @classmethod
    # def go_to_school(cls):
    #     print(f"I'm going to school")
    #     print(f"I'm a {cls}")
        # print(f"I'm going to {self.school}")

Student.go_to_school()
# anna = Student("Anna", "MIT")
# # anna.marks.append(56)
# # anna.marks.append(73)
# # print(anna.marks)
# # print(anna.average())
# anna.go_to_school()
