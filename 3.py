isTrue = False

strOne = "One"

strThree = "Three"

a = 2

b = 2

c = [1, 2, 3]

d = [1, 2, 3]

if a == b:
    print("a is equal to b")

if c == d:
    print("c equals d")

if a is b:
    print("a is b")
elif a is not b:
    print("a is not b")
elif "blab" == "blabbf":
    pass
else:
    print("something is very wrong")

if c is d:
    print("c is d")
#     is is by reference and == is by value
if type(a) is int:
    print("a is an integer")

# age = int(input("enter your age: "))
age = 10

if 0 < age < 120:
    print("ok")

if a < b and not (strThree == 3 or isTrue == 4):
    print(a, "is less than ", b)

elif a == b:
    print(a, "is equal to", b)

else:
    print(a, " is greater than ", b)

my_names = ["adi", "ben", "noam", "arthur", "ron"]

for i in range(len(my_names)):
    if "zohar" == my_names[i]:
        print(i)


if "zohar" in my_names:
    print("found Zohar")

my_list = []
if my_list:
    print("my_list is not empty")

print(a < b)

if len(my_names) > 2:
    print("I remember enough names")

'''
Loops
'''
#  -> יחיד in רבים
for name in my_names:
    print(f"hello {name}")
    if name == "adi":

        break
# else will run if the for loop ends successfully
else:
    print("print all names")

# by index
for i in range(len(my_names)):
    print("printing", my_names[i])

a = 0
while a < 5:
    print(a)
    a += 1
    if a == 2:
        break
    elif a == 3:
        continue
    a = a + 1


l = []
dict1 = {"key": "val"}

l.append("new str")
print(l)
current_input = input("enter letter:")

while current_input != "q":
    l.append(current_input)
    current_input = input("enter letter:")

n = [1, 2, 3, 4, 5]

result1 = []
for num in n:
    result1.append(num*2)

# list comprehension
result2 = [num * 2 for num in n if num > 2]
print(result2)
