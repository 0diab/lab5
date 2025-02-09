largest = 0
for number in range(1,11):
    usrin = int(input(f"please enter number {number}: "))
    print()
    if usrin > largest:
        largest = usrin

print(f"The largest number was {largest}")