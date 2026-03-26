from student import Student_result
student_list=[]
try:
    with open("practince_projects/marks.txt") as f:
     for line in f:
        line=line.strip()
        if line == " ":
            continue
        name,roll_id,section=line.split(",")
        student=(name,int(roll_id),section)
        student_list.append(student)
except FileExistsError:
    print("file not fount error")
for student in student_list:
   print(student_list)
   student.total()
   student.grade()