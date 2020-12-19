def alphabet():
    let = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"
        ]
    return let

letters = alphabet()

def numb():
    numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    return numbers

number = numb()

def sym():
    symb = "_"
    return symb

symbols = sym()

import random as r

def randoms_numbers():
    random_numbers01 = r.choice(number)
    random_numbers02 = r.choice(number)
    random_numbers03 = r.choice(number)
    randomnumbers = random_numbers03, random_numbers02, random_numbers01
    return randomnumbers

randomn = randoms_numbers()

def random_letters():
    random_letters01 = r.choice(letters)
    random_letters02 = r.choice(letters)
    random_letters03 = r.choice(letters)
    random_letters04 = r.choice(letters)
    random_letters05 = r.choice(letters)
    random_symbols = r.choice(symbols)
    randomletters = random_letters01, random_letters02, random_letters03, random_letters04, random_letters05, random_symbols

    return randomletters
randomnmb = randomn
randoml = random_letters()
random = randoml + randomn
print(random)


import time as t

def write_password():
    text = open("python pass gen.txt", "a")
    text.write("New Password\n")
    text.writelines(r.choices(random, k=12))
    text.write("\n")
    text.write("\n")
    text.close()
    return text

run = write_password()

print(run)
#run2 = open("python pass gen.txt", "w+")
#run2.writelines(random)
#run2.write("\n")
#print(run2)
#while True:
    #print(run2)
    #t.sleep(2)
    








# run_program = program()



#while True:
# print(run_program)





