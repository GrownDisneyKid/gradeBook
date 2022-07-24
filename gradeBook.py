
# receives each student's name into a dictionary
def names():
    name = input('What is the student\'s name?\n')
    return name


# func will receive all three grades, apply the weight, and return the average of the three
def student_average():
    grade_book = []
    discussion_grade = int(input('What is the grade of the quiz?\n'))
    discussion_score = discussion_grade * .20
    grade_book.append(discussion_score)
    quiz_grade = int(input('What is the grade of the discussion?\n'))
    quiz_score = quiz_grade * .20
    grade_book.append(quiz_score)
    program_grade = int(input('What is the grade of the program?\n'))
    program_score = program_grade * .60
    grade_book.append(program_score)
    average = sum(grade_book)
    return average


studentNames = []

studentAverages = []

student_add = True

while student_add is True:
    add_student = input('Would you like to add a student? Y or N\n')
    add_student = add_student.upper()
    if add_student == 'Y':
        # inputs the scores and names with a loop based on student count student by student
        studentNames.append(names())
        studentAverages.append(student_average())
    if add_student == 'N':
        student_add = False


# # following line was for testing purposes only
# print(studentNames)
# print(studentAverages)

# sets the base to evaluate the highest average
highest_average = 0
highest_student = ''
position = 0


for student in studentAverages:
    aver = student
    aver_name = studentNames[position]
    print(f'' + aver_name + ' has an average of ' + str(aver) + '.\n')
    if student > highest_average:
        highest_average = student
        highest_student = studentNames[position]  # ensures the score position matches the name list position
        position += 1  # increases the position each loop to track the name list
    else:
        position += 1  # increases the position each loop to track the name list

print(f'The student with the highest average is ' + highest_student + ' with an average of ' + str(highest_average) + '.')

# following line was for testing purposes only
# print(str(highest_average), highest_student)
