# My first Python program
# By Eugene Barasa

print("Hello World!")
print("My name is Eugene Barasa")
print("I am a Mathematics & Computer Science student")
print("Work Faithfully. Grow Intentionally. Seek God Consistently.")
# Variables
name = "Eugene Barasa"
age = 20
university = "Maseno University"
is_christian = True

print(name)
print(age)
print(university)
print(is_christian)

# User Input
your_name = input("What is your name? ")
your_age = input("How old are you? ")

print("Hello " + your_name + "!")
print("You are " + your_age + " years old.")
print("God bless you " + your_name + "! 🙏")

# If Statements
marks = int(input("Enter your marks out of 100: "))

if marks >= 70:
    print("Excellent! Keep it up! 🔥")
elif marks >= 50:
    print("Good work! You can do better! 💪")
elif marks >= 40:
    print("You passed! Study harder! 📚")
else:
    print("Don't give up! God has a plan! 🙏")

    # Loops
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("---")

# Loop through a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("My favourite fruits:")
for fruit in fruits:
    print("- " + fruit)

print("---")

# While loop
count = 1
while count <= 3:
    print("This is repeat number " + str(count))
    count += 1

    # Functions
def greet(name):
    print("Hello " + name + "! God bless you! 🙏")

def add_numbers(a, b):
    result = a + b
    return result

def check_grade(marks):
    if marks >= 70:
        return "A - Excellent!"
    elif marks >= 50:
        return "B - Good!"
    elif marks >= 40:
        return "C - Pass"
    else:
        return "F - Try again"

# Call the functions
greet("Eugene")
greet("Maseno University")

sum = add_numbers(10, 20)
print("10 + 20 = " + str(sum))

grade = check_grade(85)
print("Grade: " + grade)

# Lists
students = ["Eugene", "John", "Mary", "Peter"]
print("Students:", students)
print("First student:", students[0])
print("Last student:", students[-1])

students.append("Paul")
print("After adding Paul:", students)

print("Total students:", len(students))

print("---")

# Dictionaries
eugene = {
    "name": "Eugene Barasa",
    "university": "Maseno University",
    "course": "Mathematics & Computer Science",
    "year": 2,
    "is_christian": True
}

print("Name:", eugene["name"])
print("University:", eugene["university"])
print("Course:", eugene["course"])
print("Year:", eugene["year"])

# Loop through dictionary
print("---")
print("All my details:")
for key, value in eugene.items():
    print(key + ":", value)
    print(key + ":", value)

    # File Handling

# Writing to a file
file = open("my_notes.txt", "w")
file.write("My Python Learning Notes\n")
file.write("By Eugene Barasa\n")
file.write("University: Maseno University\n")
file.write("Work Faithfully. Grow Intentionally. Seek God Consistently.\n")
file.close()

print("File written successfully!")

# Reading from a file
file = open("my_notes.txt", "r")
content = file.read()
file.close()

print("File contents:")
print(content)

# Appending to a file
file = open("my_notes.txt", "a")
file.write("Lesson 7 - File Handling completed!\n")
file.close()

print("File updated successfully!")