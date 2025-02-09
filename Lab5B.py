stars = int(input("Please enter a value for the size: "))

for shape in range(stars):
    for n in range(stars):
        print("*", end="")
    print("")


for shape in range(stars+1):
    for x in range(shape):
        print(f"", end="*")
    print("")

for shape in range(1, stars + 1):
    for x in range(stars - shape):
        print(" ", end="")
    for y in range(shape):
        print("*", end="")
    print()
