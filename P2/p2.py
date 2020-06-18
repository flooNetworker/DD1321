
### LAB p2 ###


alphabeta = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
             'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
             'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}


# UPPGIFT 2.1
# wants a dictionary with the alphabet to be able to convert lowcase letters to uppercase letters
# if the letter in a password is lowercase, change to uppercase, otherwise return unchanged
# IN: a letter, from the password string
# UT: that same letter but as uppercase


def uppercase(letter):

    for key in alphabeta:  # will take letter and compare it to every letter in the alphabet
        if letter == key:
            # change to upper via the dictionary alphabeta
            upper = alphabeta[key]
            break

        if letter == alphabeta[key]:  # if it is already uppercase
            upper = alphabeta[key]
            break

    return upper


# UPPGIFT 2.2
# wants to change one letter in password to uppercase
# IN: a string, the password we want to change
# UT: a list with changed passwords
# returnerar tex. ['Admin', 'aDmin', 'adMin', 'admIn', 'admiN']
def one_uppercase(string):

    one_upper_pwrds = []
    pwrd = ''

    num = 0
    # go through the entire length of string, change the letter that is going to be uppercase
    while num < len(string):
        pwrd = ''
        for i, x in enumerate(string):
            if i == num:  # will change 1st, 2nd, etc letter to be uppercase
                v = uppercase(x)
                pwrd += v
            else:
                pwrd += x

        one_upper_pwrds.append(pwrd)  # put new password in list
        num += 1  # take next letter

    return one_upper_pwrds


print(one_uppercase('password'))
# UPPGIFT 2.3
# take password string and change it to every combination of two uppercase letters
# IN: a string, the password we want to change
# UT: a list with changed passwords


def two_uppercase(string):
    two_upper_pwrds = []
    one_upper_pwrds = one_uppercase(string)
    pwrd = ''

    # take every password in list with one uppercase letter (from 2.2)
    for element in one_upper_pwrds:
        num = 0

        while num < len(string):
            pwrd = ''  # nollställ efter varje inläggning i ny lista

            for i, x in enumerate(element):
                if i == num:  # will change 1st, 2nd, etc letter to be uppercase
                    # if already uppercase, add as it is and take next letter
                    if x == uppercase(x):
                        pwrd += x
                        num += 1

                    else:
                        v = uppercase(x)  # change to uppercase
                        pwrd += v

                else:
                    pwrd += x  # add lowercase letter

            two_upper_pwrds.append(pwrd)  # put new password in list
            num += 1  # take next letter

    two_upper_pwrds_copy = []  # make copy of password list

    # CLEAN UP LIST
    for i in two_upper_pwrds:  # filter out all doublets, and also the passwords that does not have two uppercase letters
        if i not in one_upper_pwrds:  # take all passwords not already in the one_upper list
            if i not in two_upper_pwrds_copy:  # add passwords that not already have been added into empty copy list
                two_upper_pwrds_copy.append(i)

    return two_upper_pwrds_copy  # return list with new passwords


# UPPGIFT 2.4
# Will add a number/special sign at beginning or the end of every letter
# returnerar ['2och', '3och', '+och', 'o2ch', 'o3ch', 'o+ch', 'oc2h', 'oc3h', 'oc+h', 'och2', 'och3', 'och+']
# IN: a string, the password we want to change
# UT: a list with changed passwords

def special_sign(string, sign):

    pwrd_list = []

    # add what sign to add
    # sign = input("What special sign would you like to add?")

    # antal positioner 0 1 2 3, one more to add after last letter
    for i in range(len(string)+1):
                                                      # o c h
        pwrd = string[:i] + sign + string[i:]  # add sign after each letter

        # if i == 0:
        #   pwrd = sign + string[i:]  # if first sign add before letter

        pwrd_list.append(pwrd)

    return pwrd_list


print(special_sign('password', '+'))
# UPPGIFT 2.5
# combine ALL methods!
# IN: string with password
# OUT: list with all changed passwords


def comb(string):
    new_passwords = []
    # sign = input("What special sign would you like to add?")
    sign = '+'

    print("The password is:" + " " + string)

    # add every element in one:uppercase in list
    # add for one:uppercase special signs to all
    for element in read_file("p2_passwords.txt"):
        new_passwords.append(element)

    for element in one_uppercase(string):
        new_passwords.append(element)
        for i in special_sign(element, sign):
            new_passwords.append(i)

    for element in two_uppercase(string):
        new_passwords.append(element)
        for i in special_sign(element, sign):
            new_passwords.append(i)

    yes = {'yes', 'y'}
    no = {'no', 'n'}
    choice = 'n'

    while (choice in yes):
        choice = input("Would you like to add another sign? [y/n]")

        if choice in yes:
            sign = input("What special sign would you like to add?")

            for element in one_uppercase(string):
                for i in special_sign(element, choice):
                    new_passwords.append(i)

            for element in two_uppercase(string):
                for i in special_sign(element, sign):
                    new_passwords.append(i)

        elif choice in no:
            print("finished")
        else:
            print("Please respond y or n")

    print("The changed passwords are")
    # print(new_passwords)
    print("Number of combinations are:")
    print(len(new_passwords))

    return new_passwords


# UPPFIFT 2.6
# Komplexiteten av funktionen comb() kommer vara kvadratisk
# T(n^2) då iomed att vi har två for looper i varandra ökas den proportinellt till kvadraten av N
# while loopen är konstant oavsett hur många saker den gör
# (O(M*N^2))

# INPUT STORLEK SAMBAND MED OUTPUT STORLEK:
 # SKICKAR IN N ORD; ÄNDRAR N GÅNGER
 # SKICKAR IN + SOM OCKSÅ KAN ÄNDRAS N GÅNGER
 # N^2

# MED ETT SPECIALTECKEN
# När 5 tecken: 105 kombinationer: n=105, n^2=11 025
# När 10 tecken: 660 kombinationer n=660, n^2=435 600
# När 15 tecken: 2040 kombinationer n=2040, n^2=416 1600

# MED TVÅ SPECIALTECKEN
# När 5 tecken: 195 kombinationer:  n^2=38025
# När 10 tecken: 1265 kombinationer  n^2=435 1600225
# När 15 tecken: 3960 kombinationer, n^2=416 15681600


# UPPGIFT 2.7
# Write all passwords on a file (p2_passwords.txt)

def read_file(filename):

    new_passwords = [line.rstrip('\n') for line in open(filename)]  # opeb fike

    return new_passwords


def save_file_content(filename, list_of_combinations):

    with open(filename, 'w') as f:
        for item in list_of_combinations:
            f.write("%s\n" % item)


# file = input("What file would you like to read passwords from?")
passwords = read_file("p2_passwords.txt")
comb_list = []

for pwrd in passwords:
    comb_list += comb(pwrd)

save_file_content("new_passwords.txt", comb_list)
