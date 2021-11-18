correct_answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

student_answers = ["C", "C", "A", "B", "D", "B", "D", "A", "C", "B", "B", "D", "C", "A", "D", "C", "A", "B", "D", "A"]

pass_mark = 15

student_file = open("Student.txt", "w")
for item in student_answers:
    student_file.write(item + '\n')

student_file.close()

student_file = open("Student.txt", "r")
answers = student_file.readlines()

student_file.close()

index = 0
while index < len(answers):
    answers[index] = answers[index].rstrip('\n')
    index += 1

correct, incorrect = 0, 0
incorrect_ans = []
for i in range(len(correct_answers)):
    if answers[i] == correct_answers[i]:
        correct += 1
    else:
        incorrect += 1
        incorrect_ans.append((i + 1))

print("Correct", correct)
print("Incorrect", incorrect)
print("Incorrect answers", incorrect_ans)
if correct >= pass_mark:
    print("Congratulations! You passed.")
else:
    print("Unfortunately, you have failed")
