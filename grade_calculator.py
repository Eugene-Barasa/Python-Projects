# Student Grade Calculator
# By Eugene Barasa
# Maseno University

print("=" * 50)
print("   STUDENT GRADE CALCULATOR")
print("   By Eugene Barasa - Maseno University")
print("=" * 50)

# Function to calculate grade
def get_grade(marks):
    if marks >= 70:
        return "A - Excellent!"
    elif marks >= 60:
        return "B - Very Good"
    elif marks >= 50:
        return "C - Good"
    elif marks >= 40:
        return "D - Pass"
    else:
        return "F - Fail"

# Function to calculate average
def get_average(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return round(average, 2)

# Store all students
students = []

# Get number of students
num_students = int(input("\nHow many students? "))

print()

# Loop through each student
for i in range(num_students):
    print(f"--- Student {i + 1} ---")
    name = input("Enter student name: ")
    
    # Get marks for each subject
    math = float(input("Mathematics marks: "))
    english = float(input("English marks: "))
    science = float(input("Science marks: "))
    computer = float(input("Computer Science marks: "))
    
    # Calculate average
    marks_list = [math, english, science, computer]
    average = get_average(marks_list)
    grade = get_grade(average)
    
    # Store student data
    student = {
        "name": name,
        "math": math,
        "english": english,
        "science": science,
        "computer": computer,
        "average": average,
        "grade": grade
    }
    students.append(student)
    print(f"✅ {name} recorded successfully!\n")

# Display results
print("\n" + "=" * 50)
print("           RESULTS SUMMARY")
print("=" * 50)

for student in students:
    print(f"\nStudent: {student['name']}")
    print(f"  Mathematics:      {student['math']}")
    print(f"  English:          {student['english']}")
    print(f"  Science:          {student['science']}")
    print(f"  Computer Science: {student['computer']}")
    print(f"  Average:          {student['average']}")
    print(f"  Grade:            {student['grade']}")
    print("-" * 40)

# Find best student
best = max(students, key=lambda x: x['average'])
print(f"\n🏆 Best Student: {best['name']} with {best['average']}%")

# Save to file
file = open("results.txt", "w")
file.write("STUDENT GRADE RESULTS\n")
file.write("By Eugene Barasa - Maseno University\n")
file.write("=" * 40 + "\n\n")

for student in students:
    file.write(f"Name: {student['name']}\n")
    file.write(f"Average: {student['average']}\n")
    file.write(f"Grade: {student['grade']}\n")
    file.write("-" * 30 + "\n")

file.write(f"\nBest Student: {best['name']} - {best['average']}%\n")
file.close()

print("\n✅ Results saved to results.txt!")
print("\nWork Faithfully. Grow Intentionally. Seek God Consistently. 🙏")
print("=" * 50)