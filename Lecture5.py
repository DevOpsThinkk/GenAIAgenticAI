# 1. Ask the user for:
# Their name
# Their birth year
# Then print: Hello <name>, you are <age> years old!

name = input("Enter your name: ")
birth_year = int(input("Enter your Birth Year: "))
age = 2026 - birth_year
print(f"Hello {name}, you are {age} years old! ")

# 2. Ask the user for two numbers and print:
# Their sum
# Their difference
# Their product

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The sum of {num1} and {num2} is : {num1 + num2}")
print(f"The difference of {num1} and {num2} is : {num1 - num2}")
print(f"The product of {num1} and {num2} is : {num1 * num2}")


# 3. Ask the user to enter a float number and cast it to integer. Print both values.

float_num = float(input("Enter a float number: "))
int_num = int(float(float_num))
print(f"You entered the float number: {float_num} the data type of float_num is : {type(float_num)}")
print(f"The integer value after casting is: {int_num} the dat type of int_num is : {type(int_num)}")

# 4. Ask the user to enter two words and print them in reverse order, separated by a comma.
# Example:
# Input 1: Hello
# Input 2: World
# Output: World, Hello

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print(f"{word2}, {word1}")

# 5. Challenge: Ask for a number, multiply it by 5, then convert the result to a string and print:
# "Your number multiplied by 5 is: <result>"

num = int(input("Enter a number: "))
result = num * 5
result_str = str(result)
print(f"Your number multiplied by 5 is: {result_str} and the data type of result_str is : {type(result_str)}")