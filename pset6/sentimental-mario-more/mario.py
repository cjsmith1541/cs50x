from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break
for i in range(height):
    for j in range(((height * 2) + 3) - (height - i)):
        if j < height - (i + 1) or j == height or j == height + 1:
            print(" ", end="")
        else:
            print("#", end="")
    print()