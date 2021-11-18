num_day = 7

sales = []

for index in range(num_day):
    print("Day #", index + 1, ": $", sep=' ', end=' ',)
    item = float(input())
    sales.append(item)
    index += 1

total = 0
for index in range(num_day):
    sales1 = sales[index]
    total += sales1
print("Total sales in the week is $", total)