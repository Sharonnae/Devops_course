def get_age():
    age = int(input("enter your age"))
    if age < 0:
        raise ValueError("Age can not be negative!!!! You ruined everything :(")


#
# try:
#     get_age()
# except ValueError as e:
#     print(e.args)

a = input("enter number: ")


def check_my_nymber(num):
    try:
        a = int(num)
    except ValueError:
        return False
