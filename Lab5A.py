print("Please enter 10 numbers and this program will display the largest.")
largest = 0
for number in range(1,11):
    usrin = int(input(f"Please enter number {number}: "))
    if usrin > largest:
        largest = usrin
    print("")
print(f"The largest number was {largest}")