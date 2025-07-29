# Student Management System

""" 
1️⃣ Add Student Record
Input student details:
Name (string)
Roll Number (string/integer)
Age (integer)
Courses (store as a tuple)
Marks (store as a dictionary — subject as key, marks as value)
"""
name = input("Enter student's name: ")  # string
roll_number = input("Enter roll number: ")  # string/integer
age = int(input("Enter age: "))  # integer
courses_input = input("Enter courses: ")
courses = tuple(course.strip() for course in courses_input.split(','))
marks = {}
print("Enter marks for each course:")
for course in courses:
    mark = float(input(f"Marks in {course}: "))
    marks[course] = mark


"""
2️⃣ Display All Records
Show a summary of all student records.
Display Name, Roll No, Age, Courses, Marks, Average Marks, and Grade.
"""    
# Display all records 
print("\nStudent Details:")
print("Name:", name)
print("Roll Number:", roll_number)
print("Age:", age)
print("Courses:", courses)
print("Marks:", marks) 
""" 
3️⃣ Search Student by Roll Number
Allow the user to enter a roll number.
Display all details of the corresponding student (if found).
"""
   
rollnumber=input("Enter a rollno.")
if rollnumber == ("rollno."):
    print("\nStudent Details:")
    print("Name:", name)
    print("Roll Number:", roll_number)
    print("Age:", age)
    print("Courses:", courses)
    print("Marks:", marks) 
else:
    print("rollno not found")  
    
      
""" 
4️⃣ Update Student Record
Modify student marks or details using their roll number.
Prompt for updated values (courses or marks).
"""    


""" 
5️⃣ Delete Student Record
Remove a student record using the roll number.
"""
students = [
    {"roll_no": 1, "name": "Rahul Sharma", "grade": "A"},
    {"roll_no": 2, "name": "Priya Ray", "grade": "B"},
    {"roll_no": 3, "name": "Amit Patel", "grade": "A"},
    {"roll_no": 4, "name": "Sneha Sahu", "grade": "C"}
]
def delete_student_record(roll_no, student_list):
    for student in student_list:
        if student["roll_no"] == roll_no:
            student_list.remove(student)
            print(f"Roll No {roll_no} removed all records of this roll No.")
            return
    print(f"Roll No {roll_no} not get this roll No.")

delete_student_record(1, students)  # Amit Patel record deleted

print(students)

""" 
6️⃣ Calculate Average Marks
Calculate and display the average of marks for each student.
Based on the average, determine and display the grade:
"""
# Get marks for multiple subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))

# Calculate the average
average = (subject1 + subject2 + subject3 + subject4 + subject5) / 5

# Determine the grade using if-elif-else
if average >= 90:
    grade = 'A+'
elif average >= 75:
    grade = 'A'
elif average >= 60:
    grade = 'B'
elif average >=45:
    grade = "C"
else:
    grade = 'Fail'

# Print the average and the assigned grade
print(f"\nAverage marks: {average:.2f}")
print(f"Assigned Grade: {grade}")

""" 
7️⃣ Exit
Exit the program gracefully with a thank-you message.
"""
text = input("Thankyou for seeing this codes")
print("text")


    
    
    




      
    
    
    
    



    
    
