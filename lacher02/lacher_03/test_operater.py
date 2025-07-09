num1 = int(input("Enter your operater"))
num2 = float(input("Enter your number"))
num3 = float(input("Enter your number"))
if num1 == 1:
    print(f"{num2}+{num3}:", num2 + num3)
elif num1 == 2:
    print(f"{num2}-{num3}:", num2 - num3)
elif num1 == 3:
    print(f"{num2}*{num3}:", num2 * num3)
elif num1 == 4:
    if num3 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"{num2}/{num3}:", num2 / num3)
else:
 print("Invalid operator. Please enter a number between 1 and 4.")