def square(num):
    result = num * num
    return result, num


a = square(4)
print(a)
print(square(10))


# b = int(input("enter amount of pets:"))
# if 0 < b < 4:
#     print("ok")
# else:
#     print("not ok")


def validate(prompt, min, max, good, not_good):
    a = int(input(prompt))
    if min < a < max:
        return good
    else:
        return not_good


validate("enter amount of pets:", 0,4,"ok","not ok")

print(validate("enter your age:", 0, 120, "ok", "not a normal age"))


