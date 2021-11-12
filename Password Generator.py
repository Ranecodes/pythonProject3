import random
import string

characters = list(string.ascii_letters + string.digits + "!£$%&*()")


def generate_password():
    pwd_length = int(input("What should be the length of the password?"))
    random.shuffle(characters)
    password = []

    for count in range(pwd_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))


generate_password()