

import sys

# UPPGIFT 2.8
# Read my file, check if the password is there, if not do nothing


def read_file(filename):

    new_passwords = [line.rstrip('\n') for line in open(filename)]  # opeb fike

    return new_passwords


file = "new_passwords.txt"
password_list = read_file(file)


# word_to_test = input("What password would you like to have?")

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))


if len(sys.argv) > 1:
    word_to_test = sys.argv[1]
    if word_to_test in password_list:
        print("Not suitable password")

else:
    print("Usage: argv[0] <ord>")
