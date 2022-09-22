# conditional statements

# functions

# Enter the first number
# Enter the second number
# Enter the third number
# Output the greatest number
# Output the least number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
def greatest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        greatest_num = num1
    elif (num2 >= num1) and (num2 >= num3):
        greatest_num = num2
    else:
        greatest_num = num3
    print("The greatest number is " + greatest_num)
def least(num1, num2, num3):
    if (num1 <= num2) and (num1 <= num3):
        least_num = num1
    elif (num2 <= num1) and (num2 <= num3):
        least_num = num2
    else:
        least_num = num3
    print("The least number is " + least_num)
greatest(num1, num2, num3)
least(num1, num2, num3)