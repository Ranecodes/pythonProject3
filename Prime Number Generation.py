user_entry = int(input())
list1 = []
for num in range(2, user_entry + 1):
    list1.append(num)

for i in list1:
    c = 0
    for j in range(1, i):
        if i % j == 0:
            c += 1
    if c == 1:
        print(i, 'prime')
    else:
        print(i, 'not prime')