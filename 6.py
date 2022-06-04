

# Write a function that takes in a numerical value, and returns
#  the word corresponding to that number.
# The program will handle numbers: 0 - 4, for other numbers it will
# return that the input is incorrect.


def get_numeric(number):
    numbers = ["zero", "one", "two", "three", "four"]
    if number < len(numbers):
        return numbers[number]
    else:
        return "not supported"
result = get_numeric(10)
print(result)
a = 6


def my_function(x):
    x = 10
    print(x * a)


my_function(a)


def my_function1(x, a):
    print(x * a)


def my_function2(x):
    a = 6
    print(x * a)