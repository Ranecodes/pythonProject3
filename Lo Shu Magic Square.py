list1 = [[4, 9, 1],
         [3, 5, 8],
         [2, 7, 6]]

for row in list1:
    print(row)


def magic_square(list2d):
    if isinstance(list2d, list) and len(list2d) == 3:
        list1d = sum(list2d, [])
        print(list1d)
        if max(list1d) >= 10 or min(list1d) <= 0:
            print("Out of range, select a number within 0 and 9")
            return False
        if len(list1d) != len(set(list1d)):
            print("There is a duplicate present")
            return False

        row1sum = list2d[0][0] + list2d[0][1] + list2d[0][2]
        row2sum = list2d[1][0] + list2d[1][1] + list2d[1][2]
        row3sum = list2d[2][0] + list2d[2][1] + list2d[2][2]
        col1sum = list2d[0][0] + list2d[1][0] + list2d [2][0]
        col2sum = list2d[0][1] + list2d[1][1] + list2d[2][1]
        col3sum = list2d[0][2] + list2d[1][2] + list2d[2][2]
        row_diag1 = list1d[0] + list1d[4] + list1d[8]
        row_diag2 = list1d[2] + list1d[4] + list1d[6]

        if row1sum == row2sum == row3sum == col1sum == col2sum == col3sum == row_diag2 == row_diag1:
            print("This is a Lo Shu Magic Square")
            return True

        else:
            print("This is not a Lo Shu Magic Square")


magic_square(list1)
