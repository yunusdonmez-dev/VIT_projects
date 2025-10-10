# Project 5: Student Grading System 
# Practice dictionaries, lists, loops, and averages

# Create an empty dictionary to store student data
students = {}

# Ask user for number of students (minimum 3)
num_students = int(input("How many students? (at least 3): "))

if num_students < 3:
    num_students = 3  # enforce minimum of 3

# Input each student's name and 3 grades
for i in range(num_students):
    name = input(f"\nEnter name of student {i + 1}: ")
    grades = []
    for j in range(3):
        grade = float(input(f"Enter grade {j + 1} for {name}: "))
        grades.append(grade)
    students[name] = grades

# Print each student's average
print("\nStudent averages:")
averages = {}
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    averages[name] = avg
    print(f"{name}: {avg:.2f}")

# Extra: Show student(s) with the highest average
highest_avg = max(averages.values())
top_students = [name for name, avg in averages.items() if avg == highest_avg]

print("\nHighest average student(s):")
for student in top_students:
    print(f"{student}: {highest_avg:.2f}")
