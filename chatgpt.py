num = int(input("Enter a number between 1 to 50: "))
while num < 1 or num > 50:
    num = int(input("Invalid input. Please enter a number between 1 to 50: "))

print("Multiplication table of", num, ":")
for i in range(1, 12):
    print(num, "*", i, "=", num * i)