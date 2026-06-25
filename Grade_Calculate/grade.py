class StudentGrade:
    def __init__(self,name:str,mark:float):
        self.name = name
        self.mark = mark
    
    def validate(self):
        if self.mark <0 or self.mark>100:
            print("Error! Score must be between 0 and 100")
            return False
        return True
    def get_grade(self):
        if self.mark >= 90:
            return "Excelent work! You got A."
        elif self.mark >= 80:
            return "Good job! You got B"
        elif self.mark >=70:
            return "You passed, You got C"
        elif self.mark >=60:
            return "Needs improvement! You got D"
        else:
            return "Unfortunately, you failed."
    def report(self):
        if not self.validate():
            return 
        grade = self.get_grade()
        print(f"{self.name} here is your grade: {grade}")

student_name = input("Enter your name: ")
student_mark = float(input("Enter your mark: "))
ReportCard = StudentGrade(name = student_name,mark = student_mark)
Final_Report = ReportCard.report()