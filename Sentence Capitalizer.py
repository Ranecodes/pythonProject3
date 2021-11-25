string1 = input("Enter a sentence: ")
def capitalizer(string1):
    new_string = string1.split()
    x = ' '

    for i in new_string:
        a = i[0].upper()
        c = i.replace(i[0], a) + ' '
        x += c

    print(x)
capitalizer(string1)