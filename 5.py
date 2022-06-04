for i in range(1, 101):
    if (i % 7 != 0) and i % 10 != 7 and int(i / 10) != 7:
        print(i)

for i in range(1, 101):
    if (i % 7 != 0) and '7' not in str(i):
        print(i)