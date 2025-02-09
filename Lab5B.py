stars = int(input("Please enter a value for the size: "))

print(f" This is the requested {stars}x{stars} box:")
for shape in range(stars):
    for n in range(stars):
        print("*", end="")
    print()

print(f"This is the requested right-facing {stars}x{stars} right-triangle:")
for shape in range(1,stars+1):
    for x in range(shape):
        print(f"", end="*")
    print()

print(f"This is the requested left-facing {stars}x{stars} right-triangle:")
for shape in range(1, stars + 1):
    for x in range(stars - shape):
        print(" ", end="")
    for y in range(shape):
        print("*", end="")
    print()
