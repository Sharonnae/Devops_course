### 1 2
import codecs

try:
    a = 1 / 0
except ZeroDivisionError:
    print("could not devide by zero")

### 3
# yes, it is legal, the finally will be executed no matter what happens.

### 4
# any error can be caught.
### 5
# it is problematic because it's too generic.

### 6
# except IOError = It is an error raised when an input/output operation fails,
# such as the print statement or the open() function when trying to open a file that does not exist.
# It is also raised for operating system-related errors.
# except ZeroDivisionError = when we divide a number by 0.

### 7 8
with open("words.txt", "w") as f:
    f.write("Sharon Nae")

### 9
with open("words.txt") as f:
    for line in f.readlines():
        print(line)
### 10
with codecs.open("words.txt", "w+", "iso-8859-8") as f:
    f.write("עברית")
    f.seek(0)
    for line in f.readlines():
        print(line)

### Challenge

from PIL import Image , ImageDraw

img = Image.new('RGB', (100, 100), color = 'pink')
d = ImageDraw.Draw(img)
d.text((20,40), "Giraffe O.o", fill=(255,255,0))
img.save('pink_giraffe.png')


