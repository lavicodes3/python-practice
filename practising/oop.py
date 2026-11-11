class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(f"name: {self.name}, Avg marks: {round(sum/3,2)}")

s1 = Student("Karan",[95,23,67])
s1.get_avg()

