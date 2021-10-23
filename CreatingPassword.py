import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase10)
s3 = list(string.digits)
s4 = list(string.punctuation)

char_num = input("please enter number of charcters of the password! ")

while True:
    try:
        char_num = int(char_num)
        if char_num < 6 :
            char_num = input("please enter 6 or more! ")
        else:
            break
    except:
        char_num = input("please enter an integer number ")

print(char_num)
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(char_num*.3)
part2 = round(char_num*.2)

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)
password = "".join(password[:])
print(password)
