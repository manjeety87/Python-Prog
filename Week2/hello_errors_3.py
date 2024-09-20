#Logic errors are errors where we have written valid python code,
# but the code doesn't behave in the manner that we intended.
#Programs will always do what you TOLD them to do,
# which is not necessarily what you WANTED them to do.
#Programs behave like children who take everything you say literally.
#Find the errors
#This is a program for calculating an average grade
# grade1 = 0.90   #90%
# grade2 = 65.5   #65.5%
# grade3 = "B+"   #78%
#Calculate the grade average. This should be a floating point number
# between 0 and 1.0
# gradeAvg = grade1 + grade2 + grade3 / 3
#Multiply by 100 so we can show the value as a percentage.
# gradeAsPercentage = gradeAvg * 100
# print("Your final average grade percentage is:", gradeAvg, "%")


#Logic errors are errors where we have written valid python code,
# but the code doesn't behave in the manner that we intended.
#Programs will always do what you TOLD them to do,
# which is not necessarily what you WANTED them to do.
#Programs behave like children who take everything you say literally.
#Find the errors
#This is a program for calculating an average grade
grade1 = 0.90   #90%
grade2 = 0.655   #65.5%
grade3 = 0.78   #78%
#Calculate the grade average. This should be a floating point number
# between 0 and 1.0
gradeAvg = (grade1 + grade2 + grade3) / 3
#Multiply by 100 so we can show the value as a percentage.
gradeAsPercentage = gradeAvg * 100
print("Your final average grade percentage is:", gradeAsPercentage, "%")