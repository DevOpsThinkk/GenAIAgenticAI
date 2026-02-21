## 1. Create variables to store your:
Name = "Nareshkar"
Age = 25
Favorite_programming_language = "Python"
Is_student = True

##Print each of them with appropriate labels using f-strings.
print(f"My name is : {Name}")
print(f"My age is : {Age}")
print(f"my favorite programming language is : {Favorite_programming_language}")
print(f"Am I a student? : {Is_student}")
#--------------------------------------------------------------------------------#
##2. Predict the output and data types:

x = 10
y = 3.14
z = x + y
print("the data type of x is : ", type(x))
print("the data type of y is : ", type(y))
print(type(z))

#--------------------------------------------------------------------------------#
##3. Create a variable with a value "123" and check if it’s a number or string. 
# Then convert it to an integer and add 10.

value = "123"
print(f"the data type of value is : {type(value)}")
value = int(value)
print(f"the data type of value after conversion is : {type(value)}")
result = value + 10
##`4. Try creating invalid variable names like 2name, class, or my-name and note what errors Python gives you.

# 2name = "invalid variable name"  
# This will raise a SyntaxError because variable names cannot start with a number.
#--------------------------------------------------------------------------------#
#5. Advanced: Can a variable store multiple data types during execution?

x = 10
print(type(x))

x = "Now I am a string"

