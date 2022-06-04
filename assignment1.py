# First assignment - Sharon Nae

### A

# 1. Create a variable name first with value 7.
first = 7

# 2. Create a variable name second with value 44.3.
second = 44.3

# 3. Print result of adding first to second.
print(second+first)

# 4. Print result of multiplying first by second
print(first*second)

# 5. Print result of dividing second by first
print(second/first)


### B

# What will be the values of a, b, c at the end?
a = 9
b = 8
c = 15


### C

# Is there a difference between the two lines below? Why?
# Answer: No, both will be used to store a string. ' will allow you to add " to your stirng, while " will require \ before the ".

# What is the issue with the code below:
my_number=5+5
# print("result is"+my_number)
#Answer: the problem is that my_number is a number and we can't add it to a string. we need to cast it to str using str(my_number), so we'll get:
print("result is"+str(my_number))


### D

# what is the output of:
x = 5
y = 2.36
print(x+int(y))
#Answer: the output is 7 because we're casting y from 'float' to 'integet' so we loose the digits after the dot.


# Challenge
a = 8
b = "123"
print(a+int(b))




