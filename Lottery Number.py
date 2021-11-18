stats = []
series = 5
index = 0

for count in range(series):
    print("#", index + 1, ':', sep=' ', end=' ')
    items = int(input())
    stats.append(items)
    index += 1


print("The lowest number is", min(stats))
print("The highest number is ", max(stats))

total = 0
for num in stats:
    total += num
average = total/len(stats)
print("The total of the numbers is", total)
print("The average of the numbers is ", average)
