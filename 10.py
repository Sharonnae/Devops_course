from url_1 import url_caller

def ask_name():
    name = input("Please enter your name: ")
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")


def print_hello_name():
    with open("names.txt","r") as file:
        for line in file.readlines():
            print(f"Hello {line}", end='')


def url_forward():
    with open("urls.txt", "r") as urls:
        for line in urls.readlines():
            url_caller(line.strip())


ask_name()
print_hello_name()
url_forward()