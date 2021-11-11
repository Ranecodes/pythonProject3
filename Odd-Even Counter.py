import random


def main():
    even_count, odd_count = 0, 0
    for count in range(100):
        random_numbers = random.randint(1, 200)
        print(random_numbers)
        if random_numbers % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print('Number of even numbers in the loop: ', even_count)
    print("Number of odd numbers in the loop: ", odd_count)


main()
