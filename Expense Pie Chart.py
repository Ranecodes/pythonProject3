import matplotlib.pyplot as plt
Outfile = open("Expenses.txt", 'w')
Outfile.write(str(10) + '\n')
Outfile.write(str(20) + '\n')
Outfile.write(str(30) + '\n')
Outfile.write(str(40) + '\n')
Outfile.write(str(50) + '\n')
Outfile.write(str(60) + '\n')
Outfile.close()

infile = open("Expenses.txt", "r")
data = infile.readlines()
infile.close()

index = 0
while index < len(data):
    data[index] = data[index].rstrip('\n')
    index += 1
res = [int(i) for i in data]
print(res)

expense_labels = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Misc"]

plt.pie(res, labels=expense_labels, colors=("r", "y", "c", "m", "b", "k"))

plt.title("Expense Paid Chart")
plt.show()