class Student_result:
    def __init__(self,name,roll_id,section):
        self.name=name
        self.roll=roll_id
        self.section=section
    

    def __repr__(self):
        return f"name={self.name} | roll={self.roll} | section={self.section}"
    
    def total(self,total_marks):
        self.math=int(input("enter maths marks"))
        self.toc=int(input("enter toc marks"))
        self.os=int(input("enter os marks"))
        self.lntd=int(input("enter lntd marks"))
        self.total_marks=total_marks
        self.total_marks=sum([self.math,self.toc,self.lntd,self.os])
        print(self.total_marks)

    def grade(self):
        if self.total_marks>=90:
            print("A+")
        elif self.total_marks>=80:
            print("B+")
        elif self.total_marks>=70:
            print("c+")
        elif self.total_marks>=60:
            print("D+")
        else:
            print("fail")

        