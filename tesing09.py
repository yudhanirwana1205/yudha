students = input("Enter the number of students in your class : ")
name = []
total_grade = []

def totalGrades(grades):
    grade = 0
    grades = grades.split(",")
    for i in grades :
        grade += float(i)
        grade = grade/len(grades)
        return grade
    
for i in range (int(students)):
        name.append(input("Enter the name of student"))
        grades = input("Enter the grades of student" + str(i+l) + " (comma-separated) :")
        total_grade.append(total_grade(grades))

        print()
        print("Averange grades")
        for z in range(int(students)):
            print(name[z], ":" , total_grade[z])

for i in range (int(students)):
     name = input("Enter the name of student " + str(i+l) + ": ")
     grades = input("Enter the grades of student " + str(i+l) + " (comma-separated):")
     students.append(
          {
          "name" : name,
          "grade": grades,
          "averang_grade" : totalGrades(grades)
          }
     )

     # total_grade.append(totalGrades(grades))

     print('mobile')
     print("Averange grades :")
     for z in student:
          print(z["name"] ,  ":", z ["averange_gread"])