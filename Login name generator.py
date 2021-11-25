import Login
def main():
    first = input("Input first name")
    last = input("Input last name")
    id_no = input("Input ID number")

    print("Your login name is")
    print(Login.get_login_name(first,last,id_no))

    password = input("Enter your password: ")
    while not Login.valid_password(password):
        print("That password is not valid")
        password = input("Enter your password: ")
    print("That is a valid password")


main()