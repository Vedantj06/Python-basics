def check_oddeven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num1 = int(input("Enter a number: "))
result = check_oddeven(num1)
print("The number is:",result)