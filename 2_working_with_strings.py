
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
greeting = "Hello" #string data types
name = "World" #string data types

# ----------------------------------------
# Basic String Operations
# ----------------------------------------

# 1. Concatenation: Combining strings using the + operator
message = greeting + " " + name
print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"
name = "Felipe"
phrase2 = "SUPERCAGEFRAGISLISTCIOUS"

# # Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!
print("Name Lowercase:", name.lower())
print("Lowercase Phrase 2:", phrase2.lower())

# # Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
#upper case all of the previous variables
print("Name Uppercase:", name.upper())
print("Uppercase Phrase 2:", phrase2.upper())

# # Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
print("Is Uppercase?", name.isupper())
print("Is Uppercase?", phrase2.isupper())

# # Find the length of the string
# print("Length of phrase:", len(phrase))  # Output: 14
phrase3 = "The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
print("Length of the Declaration of Independence:", len(phrase3))

# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------
chicago_mayor = "Johnson"
#index slicing
print(chicago_mayor[0]) #first letter
print(chicago_mayor[-1]) #last letter
print(chicago_mayor[-3] ) # the letter "s" in johnson
#slicing
print(chicago_mayor[4 :]) #this is how to get "son" from "Johnson"
#The first number is inclusing
#The second number is exclusive
print(chicago_mayor[0:4]) # This is how to get "john" from "johnson"
print(chicago_mayor[1:5]) # this is how to get "ohns" from "Johnson"
#When we get one character/letter
#this is called string indexing
#when we get a chunk of letters from a string, its called string slicing

phrase4 = "Supercagifragilstic"
#uppercase it
#slice Super out of it into a different variable
#slice cagi out of phase3 into its own variable
#print out the last letter.
print("Uppercase:", phrase4.upper())
cut = phrase4[0:5]
print(cut)
cut1 = phrase4[5:9]
print(cut1)
print(phrase4[-1])
#git add .
#git commit -m "practice slicing"
#git push origin

# # Indexing: Access characters by position (0-based index)
# print("First character:", phrase[0])  # Output: P
# print("Last character:", phrase[-1])  # Output: !

# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!


# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

# sentence = "Python is fun to learn"

# # .split(): Splits the string into a list of words
# words = sentence.split()
# print("Split result:", words)

# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)

# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)