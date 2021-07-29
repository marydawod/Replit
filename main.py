from GPA import foo
#imports the def foo(letter_grade) from GPA.py to main.py

#In this marking period, there will be three homework grades, two quiz grades, and one test grade.
print("WELCOME TO THE PYTHON CALCULATOR!!\n\n\tThe Python Calculator calculates your grade point average as well as category averages for sections including tests, quizzes, and homework! \n\n\tBy inserting the grade(s) per category, the Python Calculator will provide the average grade you will have received and proceeds to take each of the category averages and calculate them together in order to provide your grade point average.\n\n")

questions = ["What is your name? \n\t", "What grade are you in? \n\t", "What is your age? \n\t", "What year will you graduate? \n\t"]
for x in questions:
  input(x)

print("\nNow we will be calculating your average assignments and we'll assign a grade for it. After that, you will receive a letter grade for the class, which will be utilized to figure out your final GPA! Lets start! \n\nFor the categories that you will be asked, please write clearly and put it in singular form (ex: Project, Test, Quiz, etc.).")

category__1 = str(input("\tEnter your first category: "))
#Asks the user to put in three category__1 grades.
#1
category1 = int(input("\tEnter "+category__1+" 1: "))
#2
category11 = int(input("\tEnter "+category__1+" 2: "))
#3
category111 = int(input("\tEnter "+category__1+" 3: "))
print(" ")

category__2 = str(input("\tEnter your second category: "))
#Asks the user to put in three grades.
#1
category2 = int(input("\tEnter "+category__2+" 1: "))
#2
category22 = int(input("\tEnter "+category__2+" 2: "))
#3
category222 = int(input("\tEnter "+category__2+" 3: "))
print(" ")

category__3 = str(input("\tEnter your third category: "))
#Asks the user to put in their category__3 grades.
#1
category3 = int(input("\tEnter "+category__3+" 1: "))
#2
category33 = int(input("\tEnter "+category__3+" 2: "))
#3
category333 = int(input("\tEnter "+category__3+" 3: "))
print(" ")

#This averages out the three Homework grades, and multiplies the average by the percentage.
averagecategory1 = (category1+category11+category111)/(3.0)
category_1 = (0.15*averagecategory1)
print("\nYour average "+category__1+" grade is a "+str(category_1)+"%, after multiplying it by 0.15, since it is graded as 15% in this class.")
#This averages out the two Quiz grades, and multiplies the average by the percentage.
averagecategory2 = (category2+category22+category222)/3.0
averagecategory3 = (category3+category33+category333)/3.0
#Calculates the quizzes, test, and has a final grade
category_2 = (float)(0.35*(averagecategory2))
print("\nYour average "+category__2+" grade is a "+str(category_2)+"%, after multiplying it by 0.35, since it is graded as 35% in this class.")
category_3 = (float)(0.50*(averagecategory3))
print("\nYour average "+category__3+" grade is a "+str(category_3)+"%, after multiplying it by 0.50, since it is graded as 50% in this class.")
grade = (float)(category_1+category_2+category_3)

print("Your grade is "+(str(round(grade, 2)))+"%")

