# PR-3 - Student Data Organizer
<div align="center">

# 🎓 Student Data Organizer

### A Python-Based Student Management System

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=28&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=850&lines=Student+Data+Organizer;Manage+Student+Records+Easily;Add+%7C+Update+%7C+Delete+%7C+Display;Built+with+Python;Console-Based+Student+Management+System" alt="Animated Typing Header"/>

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Project](https://img.shields.io/badge/Project-Student%20Management-00C2FF?style=for-the-badge)
![Console](https://img.shields.io/badge/Application-Console-success?style=for-the-badge)

</div>

---

# 📚 About The Project

**Student Data Organizer** is a Python-based console application designed to manage student information efficiently.

The application allows users to **add, display, update, and delete student records** through a simple menu-driven interface.

Each student record stores important information such as:

* 🆔 Student ID
* 👤 Student Name
* 🎂 Age
* 📅 Date of Birth
* 📚 Subjects
* 📝 Subject Scores
* ➕ Total Score
* 📊 Average Score
* 🏆 Grade

The project demonstrates practical use of Python **lists, dictionaries, tuples, loops, conditional statements, user input, and basic data processing**.

---

# 🎯 Project Objectives

The main objectives of this project are:

* Manage student records using Python
* Store multiple students efficiently
* Add new student information
* Display all stored students
* Update existing student information
* Delete student records
* Store subjects and corresponding scores
* Automatically calculate total marks
* Automatically calculate average marks
* Automatically assign grades
* Practise Python collection data types
* Build a real-world menu-driven Python application

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### ➕ Add Student

Add a new student with their personal information, subjects, and scores.

</td>

<td width="50%">

### 📋 Display Students

Display all student records along with their academic results.

</td>
</tr>

<tr>
<td width="50%">

### ✏️ Update Student

Find a student using their Student ID and update their information.

</td>

<td width="50%">

### 🗑️ Delete Student

Remove an existing student record from the student list.

</td>
</tr>

<tr>
<td width="50%">

### 📚 Subjects

Store and display subjects associated with students.

</td>

<td width="50%">

### 🏆 Grade Calculation

Automatically calculate total, average, and grade based on scores.

</td>
</tr>
</table>

---

# 🧰 Technologies Used

| Technology                | Purpose                                 |
| ------------------------- | --------------------------------------- |
| 🐍 Python                 | Application development                 |
| 📋 List                   | Store multiple student records          |
| 📖 Dictionary             | Store individual student information    |
| 🔢 Tuple                  | Store Student ID and Date of Birth      |
| 🔁 Loops                  | Menu handling and record processing     |
| 🔀 Conditional Statements | Grade calculation and record operations |
| ⌨️ Input                  | Collect information from the user       |

---

# 🏗️ Data Structure

The application uses a **list of dictionaries** to store student information.

A student record follows this structure:

```python
{
    "student_id": (101,),
    "name": "Alice",
    "age": 20,
    "date_of_birth": ("2006-05-15",),
    "subjects": ["Python", "Math", "English"],
    "scores": [85, 90, 80],
    "total": 255,
    "average": 85.0,
    "grade": "B+"
}
```

All student records are stored inside:

```python
students = []
```

This makes the project a practical example of using **nested Python collections**.

---

# 🔄 Application Workflow

```text
              ┌──────────────────┐
              │      START       │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │  Display Menu    │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │  User Selection  │
              └────────┬─────────┘
                       ↓
       ┌───────────────┼───────────────┐
       ↓               ↓               ↓
   Add Student     Display         Update
       │           Students        Student
       │               │               │
       └───────────────┼───────────────┘
                       ↓
                  Delete Student
                       ↓
                Display Subjects
                       ↓
                     Exit
```

---

# 📋 Menu Options

When the program starts, the following menu is displayed:

```text
Select an option:

1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

---

# ➕ 1. Add Student

The user can enter:

```text
Student Id:
Name:
Age:
Date of Birth:
Subjects:
```

The program then asks for a score for every subject.

For example:

```text
Student Id: 101
Name: Alice
Age: 20
Date of Birth: 2006-05-15
Subjects: Python,Math,English

Enter a score Python: 85
Enter a score Math: 90
Enter a score English: 80
```

The program automatically calculates:

```text
Total   = 255
Average = 85.00
Grade   = B+
```

---

# 📊 Automatic Result Calculation

The program calculates the total using:

```python
total = sum(student["scores"])
```

The average is calculated using:

```python
average = total / len(student["scores"])
```

The grade is then determined according to the average score.

| Average | Grade |
| ------- | ----- |
| > 95    | A+    |
| > 90    | A     |
| > 85    | B+    |
| > 80    | B     |
| > 75    | C+    |
| > 70    | C     |
| > 65    | D+    |
| > 60    | D     |
| > 55    | E+    |
| > 50    | E     |
| ≤ 50    | F     |

---

# 📋 2. Display All Students

The program displays all stored students with their:

```text
Student ID
Name
Age
Subjects
Date of Birth
Scores
Total
Average
Grade
```

Example:

```text
Student ID: 101 | Name: Alice | Age: 20 |
Subjects: ['Python', 'Math', 'English'] |
Date of Birth: 2006-05-15 |
Scores: [85, 90, 80] |
Total: 255 |
Grade: B+ |
Average: 85.00
```

---

# ✏️ 3. Update Student Information

The user enters a Student ID to find the required student.

```text
Enter a Student id to update:
```

The program allows the user to update:

* Name
* Age
* Date of Birth
* Subjects
* Scores

After updating the scores, the program recalculates:

```text
Total
Average
Grade
```

This ensures that the student's academic information remains updated.

---

# 🗑️ 4. Delete Student

The user can remove a student by entering their Student ID.

```text
Enter a student id:
```

If the ID exists, the student record is removed from the list.

```text
Student Deleted Successfully
```

---

# 📚 5. Display Subjects Offered

The program can display the subjects stored for the students.

This feature demonstrates how nested lists can be collected from dictionaries stored inside the main student list.

---

# 🧠 Python Concepts Practised

This project combines several important Python concepts.

### Variables

```python
student_name = input("Name: ")
student_age = int(input("Age: "))
```

### Lists

```python
students = []
scores = []
subjects = []
```

### Dictionaries

```python
student = {
    "name": student_name,
    "age": student_age,
    "subjects": subjects,
    "scores": scores
}
```

### Tuples

```python
"student_id": (student_id,)
```

### Loops

```python
while True:
    ...
```

and:

```python
for student in students:
    ...
```

### Conditional Statements

```python
if choice == 1:
    ...
elif choice == 2:
    ...
```

### String Methods

```python
subjects = subject.split(",")
```

### Built-in Functions

The project uses functions such as:

```python
input()
print()
int()
len()
sum()
range()
exit()
```

---

# 📁 Project Structure

```text
PR-3 - Student Data Organizer/
│
├── student_data_organizer.py
│
├── README.md
│
└── requirements.txt
```

Since this project uses Python's built-in functionality, external packages may not be required.

---

# 🚀 How to Run

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2. Navigate to the Project

```bash
cd Student-Data-Organizer
```

## 3. Run the Python Program

```bash
python student_data_organizer.py
```

The application will start in the terminal.

---

# 🖥️ Example Application

```text
~~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to the student Data Organizer! ~~~~~~~~~~~~~~~~~~~~~~~~~

Select an option:

1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice:
```

---

# 📈 Project Learning Outcomes

By creating this project, I practised:

* 🐍 Python fundamentals
* 📋 List manipulation
* 📖 Dictionary manipulation
* 🔢 Tuple usage
* 🔁 Loops
* 🔀 Conditional logic
* ⌨️ User input handling
* 🧮 Basic calculations
* 🗂️ Data organization
* 🧠 Problem-solving
* 🏗️ Menu-driven application design

---

# 🔮 Future Improvements

The project can be extended with additional features such as:

* 🔎 Search student by name
* 🔍 Search student by Student ID
* 📊 Sort students by average
* 🏆 Display top-performing student
* 📉 Display students who failed
* 📚 Display unique subjects
* ✏️ Update individual fields instead of all fields
* 💾 Save student data to a JSON file
* 📂 Export student data to CSV
* 🗄️ Store records in a database
* 🖥️ Build a graphical user interface
* 🌐 Convert the project into a web application
* 📊 Add student performance analytics

---

# 🧩 Possible Future Data Structure

The project could eventually store data in JSON format:

```json
{
    "student_id": 101,
    "name": "Alice",
    "age": 20,
    "date_of_birth": "2006-05-15",
    "subjects": ["Python", "Math", "English"],
    "scores": [85, 90, 80],
    "total": 255,
    "average": 85.0,
    "grade": "B+"
}
```

This would allow student information to remain available even after the program is closed.

---

# ⭐ Why I Built This Project

This project was created to strengthen my understanding of Python collection data types and apply them to a practical real-world problem.

Instead of working with isolated examples, the project combines:

```text
List
  ↓
Dictionary
  ↓
Tuple
  ↓
String
  ↓
Loops
  ↓
Conditions
  ↓
Calculations
  ↓
Menu-Driven Application
```

This makes the project a practical exercise in building a complete Python application using fundamental programming concepts.

---

# 👨‍💻 Developer

<div align="center">

### Python Developer | Data Science & AI/ML Learner

Currently learning and building projects using:

```text
Python
  ↓
Data Structures
  ↓
Data Analysis
  ↓
Data Science
  ↓
AI / ML
```

</div>

---

# 🚀 Future Vision

The Student Data Organizer is a starting point for building larger data-management applications.

The long-term goal is to progress from:

```text
Console Application
       ↓
File-Based Application
       ↓
Database Application
       ↓
GUI Application
       ↓
Web Application
       ↓
Data Analytics
       ↓
AI / ML Integration
```

---

<div align="center">

# ⭐ Keep Learning. Keep Building. Keep Improving.

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=700&lines=Python+%7C+Data+Structures+%7C+Problem+Solving;Build+Projects+%7C+Learn+Concepts+%7C+Grow+Skills;Keep+Learning+%7C+Keep+Building" alt="Animated Footer"/>

<br><br>

**Built with ❤️ and Python**

</div>
