# 1. Ask the user for:
# Their name
# Their birth year
# Then print: Hello <name>, you are <age> years old!

name = input("Enter your name: ") # This line prompts the user to enter their name and stores the input in the variable 'name'.
birth_year = int(input("Enter your Birth Year: ")) # This line prompts the user to enter their birth year, converts the input to an integer, and stores it in the variable 'birth_year'.
age = 2026 - birth_year # This line calculates the age by subtracting the birth year from the current year (2026) and stores the result in the variable 'age'.
print(f"Hello {name}, you are {age} years old! ") # This line prints a formatted string that includes the user's name and calculated age, resulting in a message like "Hello Alice, you are 30 years old!"

# 2. Ask the user for two numbers and print:
# Their sum
# Their difference
# Their product

num1 = int(input("Enter the first number: ")) # This line prompts the user to enter the first number, converts the input to an integer, and stores it in the variable 'num1'.
num2 = int(input("Enter the second number: ")) # This line prompts the user to enter the second number, converts the input to an integer, and stores it in the variable 'num2'.
print(f"The sum of {num1} and {num2} is : {num1 + num2}") # This line prints the message "The sum of " followed by the values of 'num1' and 'num2', and then the result of adding 'num1' and 'num2'.
print(f"The difference of {num1} and {num2} is : {num1 - num2}") # This line prints the message "The difference of " followed by the values of 'num1' and 'num2', and then the result of subtracting 'num2' from 'num1'.
print(f"The product of {num1} and {num2} is : {num1 * num2}") # This line prints the message "The product of " followed by the values of 'num1' and 'num2', and then the result of multiplying 'num1' and 'num2'.


# 3. Ask the user to enter a float number and cast it to integer. Print both values.

float_num = float(input("Enter a float number: ")) # This line prompts the user to enter a float number, converts the input to a float, and stores it in the variable 'float_num'.
int_num = int(float(float_num)) # This line takes the value of 'float_num', converts it to a float (which is redundant since it's already a float), then converts it to an integer, and stores the result in the variable 'int_num'. The conversion to integer will truncate the decimal part of the float number.
print(f"You entered the float number: {float_num} the data type of float_num is : {type(float_num)}") # This line prints the message "You entered the float number: " followed by the value of 'float_num'. It also prints the data type of 'float_num', which will be <class 'float'>.
print(f"The integer value after casting is: {int_num} the dat type of int_num is : {type(int_num)}") # This line prints the message "The integer value after casting is: " followed by the value of 'int_num'. It also prints the data type of 'int_num', which will be <class 'int'>.

# 4. Ask the user to enter two words and print them in reverse order, separated by a comma.
# Example:
# Input 1: Hello
# Input 2: World
# Output: World, Hello

word1 = input("Enter the first word: ") # This line prompts the user to enter the first word and stores it in the variable 'word1'.
word2 = input("Enter the second word: ") # This line prompts the user to enter the second word and stores it in the variable 'word2'.
print(f"{word2}, {word1}") # This line prints the value of 'word2' followed by a comma and a space, and then the value of 'word1'. This will output the two words in reverse order, separated by a comma.

# 5. Challenge: Ask for a number, multiply it by 5, then convert the result to a string and print:
# "Your number multiplied by 5 is: <result>"

num = int(input("Enter a number: ")) # This line prompts the user to enter a number, converts the input to an integer, and stores it in the variable 'num'.
result = num * 5 # This line multiplies the value of 'num' by 5 and stores the result in the variable 'result'.
result_str = str(result) # This line converts the integer 'result' to a string and stores it in the variable 'result_str'.
print(f"Your number multiplied by 5 is: {result_str} and the data type of result_str is : {type(result_str)}") # This line prints the message "Your number multiplied by 5 is: " followed by the value of 'result_str'. It also prints the data type of 'result_str', which will be <class 'str'>.