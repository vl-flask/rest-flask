class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def friend(self, friend_name):
        friend = Student(friend_name, self.school)
        return friend

anna = Student('Anna', 'Oxford')
friend = anna.friend("Greg")
print(friend.name)
print(friend.school)
