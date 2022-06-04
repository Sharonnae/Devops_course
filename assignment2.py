########## Sharon Nae ###########

### A
x = 10
y = 20
if x > y:
    print("BIG")
elif x < y:
    print("small")


### B
for i in range(5):
    print(i)


### C
num = int(input("please enter a number between 1-4"))
if num == 1:
    print("summer")
elif num ==2:
    print("winter")
elif num == 3:
    print("fall")
elif num == 4:
    print("spring")
else:
    print("you picked a wrong number")

### D
# the loop will run 10 times, the last print will be 11

### E
age = 27
lname_letter = "N"
currency = 3.29
flew_before = True
apartment_num = 4

print(age, lname_letter, currency, flew_before, apartment_num)
print(age+currency)

### F
phone_num = input("what is your phone number?")
print("the phone number is: ",phone_num )

### G
def printHello():
    print("hello")


def calculate():
    num = 5+3.2
    print(num)


### H
def printNmae(name):
    print(name)


def divide(number):
    print(number/2)


### I
def summary(num1, num2):
    sum = num1+num2
    print(sum)


def concat_str(str1, str2):
    str3 = str1 + " " + str2
    return str3


### K
for i in range(2):
    for j in range(6):
        if i*j != 0:
            print(i*j*"#")

### L
for row in range(7):
    for column in range(7):
        if(column == i or column == j):
            print("*",end="")
        else:
            print(" ",end="")
    print("\n")
    i += 1
    j -= 1

### M
def input_number():
    return int(input("please enter a number"))


def calculate_digit_sum():
    number = input_number()
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum
