# 1. Take two numbers as input and print:
# Their sum, difference, product, division, and remainder.

num1 = int(input("enter a First Number: "))
num2 = int(input("enter a Second Number: "))
print("Sum :", num1 + num2, "\nDifference : ", num1 - num2, "\nProduct :", num1 ** num2, "\ndivision :", num1 / num2, "\nRemainder :" , num1 % num2)

# 2. Ask the user for their age and check:
# Are they 18 or older? Print True or False.

age = input("Enter your age : ")
print("Are you a more than 18 years old : ", int(age) >= 18)

# 3. Ask the user to enter their math and science marks (out of 100). If both are greater than 40, print “Pass”, else “Fail”.

maths = int(input("Enter your maths marks out of 100 : "))
science = int(input("Enter your science marks out of 100 : "))
print(f"Pass" if maths > 40 and science > 40 else "Fail")

# 4. Check the result of:

x = 7
print(x > 5 and x < 10)
print(x > 10 or x < 5)
print(not(x > 5))


# 5. Challenge: Ask for two numbers and print True if the first number is divisible by the second and greater than it.
num3 = int(input("Enter a First Number: "))
num4 = int(input("Enter a Second Number: "))
print(num3 % num4 == 0 and num3 > num4)
