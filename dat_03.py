total = 0

for i in range(5):
    num = int(input("Enter an integer: "))

    if num < 0:
        continue  

    total += num  

print("The sum of all positive numbers entered is:", total)
