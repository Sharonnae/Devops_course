# with open("urls.txt") as my_file:
#     for line in my_file.readlines():
#         print(line, end='')
#     #   print(line.strip())
#     my_file.seek(0)
#     my_file.close() # if you don't use "with as"

with open("names.txt", "w") as my_file:
    for i in range(5):
        current_name = input("Enter your name: ")
        my_file.write(f"{current_name}\n")

