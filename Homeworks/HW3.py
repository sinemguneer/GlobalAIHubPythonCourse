#Explain your work

#Question 1

studentList = {"Name":[],"Surname":[],"midTerm":[],"Project":[],"Final":[],"passGrade":[]}
passGrades = []

for i in range(2):
	studentList["Name"].append(input("Name:"))
	studentList["Surname"].append(input("Surname:"))
	studentList["midTerm"].append(int(input("Midterm:")))
	studentList["Project"].append(int(input("Project:")))
	studentList["Final"].append(int(input("Final:")))
for j in range(len(studentList["Name"])):
	studentList["passGrade"].append(studentList["midTerm"][j]*0.3 + studentList["Project"][j]*0.3 + studentList["Final"][j]*0.4)
	passGrades.append(studentList["passGrade"][j])

passGrades.sort(reverse=True)
print(passGrades)