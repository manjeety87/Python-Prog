# finalGrade = 0.0;
# eliminateExtraText = ['%', '+', '-']
# allowedGrades = ["F", "D", "D+", "C", "C+", "B", "B+", "A-", "A", "A+"]
# def eliminateString(string):
#     for character in eliminateExtraText:
#        return string.replace(character, '')
# def check(s):
#     print("Checking",s)
#     s = s.strip().upper()
#     if s in allowedGrades:
#         return True
#     try:
#         s == "done" or float(s)
#         return True
#     except ValueError:
#         print(f'"{s}"is not a valid grade')
#         return False
# def calculateGrade(grade):
#     print("Calculating grade",grade,)
#     if grade >= 90 and grade <= 100 or grade == "A+" or grade == "a+":
#        return 4.0
#     elif grade >= 85 and grade <= 89 or grade == "A" or grade == "a":
#         return 3.8
#     elif grade >= 80 and grade <= 84 or grade == "A+" or grade == "a-":
#         return 3.6
#     elif grade >= 75 and grade <= 79 or grade == "B+" or grade == "b+":
#        return 3.3
#     elif grade >= 70 and grade <= 74 or grade == "B" or grade == "b":
#         return 3.0
#     elif grade >= 65 and grade <= 69 or grade == "C+" or grade == "c+":
#        return 2.5
#     elif grade >= 60 and grade <= 64 or grade == "C" or grade == "c":
#         return 2.0
#     elif grade >= 55 and grade <= 59 or grade == "D+" or grade == "d+":
#        return 1.5
#     elif grade >= 50 and grade <= 54 or grade == "D" or grade == "d":
#         return 1.0
#     else:
#         return 0.0
    
# def calculateGradePoint(grade):
#     print("Calculating grade",n)
#     if grade >= 90 and grade <= 100:
#        return "A +"
#     elif grade >= 85 and grade <= 89:
#         return "A"
#     elif grade >= 80 and grade <= 84:
#         return "A-"
#     elif grade >= 75 and grade <= 79:
#        return "B +"
#     elif grade >= 70 and grade <= 74:
#         return "B"
#     elif grade >= 65 and grade <= 69:
#        return "C +"
#     elif grade >= 60 and grade <= 64:
#         return "C"
#     elif grade >= 55 and grade <= 59:
#        return "D +"
#     elif grade >= 50 and grade <= 54:
#         return "D"
#     else:
#         return "F"
# # grades = input(f"Enter a grade for course {n}")
# # def printGrade(n):
# #     print(f"Grade {n} is {grades[n]}")

# def overAllGrade(grades,courses):
#     return grades/courses
    
# while True:
#     name = input("What is your name? ")
#     numberOfCourses = input("Enter number of courses: ")
#     numberOfCourses = int(numberOfCourses)
#     for n in range(numberOfCourses):
#         grade = input(f"Enter grade for course {n+1}: ")
#         while not check(grade):  # Keep asking until valid input
#             grade = input(f"Enter grade for course {n+1}: ")
#         # grade = input(f"Enter grade for course {n+1}: ")
#         if not check(grade):
#             print("CHECK FLOAT")
#             continue
#         grade = eliminateString(grade)
#         print("Checking GRADE -> ",grade)
#         grade.replace('%', '')
#         # course = input(f"Enter course {n+1} name :")
#         # grade.translate('%','', + ,'')
#         grade = float(grade)
#         eachGrades = calculateGrade(grade)
#         # finalGrade = finalGrade + grade
#         # print(overAllGrade(finalGrade,numberOfCourses))
#     #     finalGrade = finalGrade + grade
#     # print(f"{name}, your final GPA is ")
#         # break




# <username>_a1_p3.py

def calculateGrade(grade):
    # isinstance function is used to match the datatype of variable
    if isinstance(grade, str):
        grade = grade.upper()  # Normalize letter grades to uppercase

    if isinstance(grade, (int, float)):
        if 90 <= grade <= 100:
            return 4.0
        elif 85 <= grade < 90:
            return 3.8
        elif 80 <= grade < 85:
            return 3.6
        elif 75 <= grade < 80:
            return 3.3
        elif 70 <= grade < 75:
            return 3.0
        elif 65 <= grade < 70:
            return 2.5
        elif 60 <= grade < 65:
            return 2.0
        elif 55 <= grade < 60:
            return 1.5
        elif 50 <= grade < 55:
            return 1.0
        else:
            return 0.0
    else:
        if grade == "A+":
            return 4.0
        elif grade == "A":
            return 3.8
        elif grade == "A-":
            return 3.6
        elif grade == "B+":
            return 3.3
        elif grade == "B":
            return 3.0
        elif grade == "C+":
            return 2.5
        elif grade == "C":
            return 2.0
        elif grade == "D+":
            return 1.5
        elif grade == "D":
            return 1.0
        elif grade == "F":
            return 0.0

def checkInput(grade):
    allowedGrades = ["F", "D", "D+", "C", "C+", "B", "B+", "A-", "A", "A+"]
    
    if grade.endswith('%'):
        grade = grade[:-1]  # eliminating the '%' symbol

    try:
        float(grade) 
        return True
    except ValueError:
        return grade.upper() in allowedGrades

def runProgram():
    name = input("What is your name? ")
    numberOfCourses = int(input("Enter number of courses: "))
    total_grade_points = 0.0

    for n in range(numberOfCourses):
        while True:
            grade = input(f"Enter a grade for course {n + 1}: ")
            if checkInput(grade):
                break
            else:
                print(f'"{grade}" is not a valid grade. Please try again.')

        # Clean and process the grade
        if grade.endswith('%'):
            grade = float(grade[:-1])  # Convert and remove '%'
        else:
            grade = float(grade) if grade.isdigit() else grade.upper()

        grade_points = calculateGrade(grade)  # Calculate grade points
        total_grade_points += grade_points  # Accumulate total grade points
        print(f"GP for {grade}: {grade_points}")

    # Calculate and print final GPA
    final_gpa = total_grade_points / numberOfCourses
    print(f"{name}, your final GPA is {final_gpa:.2f}")

runProgram()
