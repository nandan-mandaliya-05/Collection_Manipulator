# PR-3 - Student Data Organizer

<div align="center">

# 🎓 Student Data Organizer

### A Python-Based Student Management System

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=28&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=850&lines=Student+Data+Organizer;Manage+Student+Records+Easily;Add+%7C+Update+%7C+Delete+%7C+Display;Python+%7C+Lists+%7C+Tuples+%7C+Dictionaries;Console-Based+Student+Management+System" alt="Animated Typing Header"/>

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Project](https://img.shields.io/badge/Project-Student%20Management-00C2FF?style=for-the-badge)
![Console](https://img.shields.io/badge/Application-Console-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

<br>

</div>

---

# 🌟 About The Project

**Student Data Organizer** is a Python-based console application designed to manage student information through a simple menu-driven system.

The application allows users to **add, display, update, and delete student records**.

Each student record contains:

* 🆔 Student ID
* 👤 Student Name
* 🎂 Age
* 📅 Date of Birth
* 📚 Subjects
* 📝 Subject Scores
* ➕ Total Score
* 📊 Average Score
* 🏆 Grade

The project demonstrates practical usage of Python **Lists, Dictionaries, Tuples, Strings, Loops, Conditional Statements, and Built-in Functions**.

> **"Organize data. Calculate results. Build practical Python projects."**

---

# 🎯 Project Objectives

The main objectives of this project are:

* 🧑‍🎓 Manage multiple student records
* ➕ Add new students
* 📋 Display all student information
* ✏️ Update existing student information
* 🗑️ Delete student records
* 📚 Store subjects for every student
* 📝 Store scores for each subject
* 🧮 Calculate total marks automatically
* 📊 Calculate average marks automatically
* 🏆 Assign grades based on average marks
* 📖 Practise Python collection data types
* 🧠 Build a practical menu-driven Python application

---

# ✨ Key Features

<table>
<tr>

<td width="50%">

### ➕ Add Student

Add a student with their ID, name, age, date of birth, subjects, and scores.

</td>

<td width="50%">

### 📋 Display Students

Display all stored students together with their academic information.

</td>

</tr>

<tr>

<td width="50%">

### ✏️ Update Student

Find a student using Student ID and update their information, subjects, and scores.

</td>

<td width="50%">

### 🗑️ Delete Student

Remove a student record using the Student ID.

</td>

</tr>

<tr>

<td width="50%">

### 📚 Display Subjects

Display each student's name together with their subjects.

</td>

<td width="50%">

### 🏆 Grade Calculation

Automatically calculate total, average, and grade from the student's scores.

</td>

</tr>

</table>

---

# 🧰 Technology Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,vscode,git,github" />

</div>

### Core Technologies

| Technology                | Purpose                                   |
| ------------------------- | ----------------------------------------- |
| 🐍 Python                 | Application development                   |
| 📋 List                   | Store multiple student records and scores |
| 📖 Dictionary             | Store individual student information      |
| 🔢 Tuple                  | Store Student ID and Date of Birth        |
| 🔤 String                 | Handle names, dates, and subjects         |
| 🔁 Loops                  | Process students and menu options         |
| 🔀 Conditional Statements | Handle menu choices and grades            |
| 🧮 Built-in Functions     | Calculate totals, averages, and lengths   |
| ⌨️ Input                  | Collect information from the user         |

---

# 🏗️ Data Structure

The application uses a **list of dictionaries** to store student records.

The main student list is:

```python
students = []
```

Each student is stored as a dictionary:

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

This project therefore combines several Python collection types:

```text
List
  ↓
Dictionary
  ↓
Tuple
  ↓
List
  ↓
String
```

---

# 🔄 Application Workflow

```text
                  ┌──────────────────┐
                  │      START       │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │   Display Menu   │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │  Enter Choice    │
                  └────────┬─────────┘
                           ↓
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
   Add Student         Display Students    Update Student
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ↓
                    Delete Student
                           ↓
                  Display Subjects
                           ↓
                         Exit
```

---

# 📋 Menu Options

When the application starts, the following menu is displayed:

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

The user enters the student's basic information:

```text
Student Id:
Name:
Age:
Date of Birth:
Subjects:
```

The subjects are entered using comma-separated values.

Example:

```text
Subjects (Comma-separated): Python,Math,English
```

The program separates the subjects using:

```python
subjects = subject.split(",")
```

The program then asks for a score for every subject.

Example:

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

After the student is added, the program calculates the:

* Total
* Average
* Grade

```text
Student Added Successfully.
```

---

# 📊 Automatic Result Calculation

The total score is calculated using:

```python
total = sum(student["scores"])
```

The average is calculated using:

```python
average = total / len(student["scores"])
```

The grade is then assigned according to the student's average.

### Grade System

| Average     | Grade |
| ----------- | ----- |
| Above 95    | A+    |
| Above 90    | A     |
| Above 85    | B+    |
| Above 80    | B     |
| Above 75    | C+    |
| Above 70    | C     |
| Above 65    | D+    |
| Above 60    | D     |
| Above 55    | E+    |
| Above 50    | E     |
| 50 or below | F     |

---

# 📋 2. Display All Students

The program displays all stored student records.

The information includes:

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
Student ID: 101 | Name: Alice | Age: 20 | Subjects: ['Python', 'Math', 'English'] | Date of Birth: 2006-05-15 | Scores: [85, 90, 80] | Total: 255 | Grade: B+ | Average:85.00
```

This allows all student information and academic performance to be viewed from one place.

---

# ✏️ 3. Update Student Information

The user can update an existing student by entering their Student ID.

```text
Enter a Student id to you want to update details:
```

The program allows the following information to be updated:

* 👤 Name
* 🎂 Age
* 📅 Date of Birth
* 📚 Subjects
* 📝 Scores

After the scores are updated, the program recalculates:

```text
Total
Average
Grade
```

Example:

```text
Student updated Successfully.
```

If the Student ID does not exist:

```text
Student id not found.
```

---

# 🗑️ 4. Delete Student

The user can delete a student record using their Student ID.

```text
Enter a student id:
```

If the student is found, the record is removed from the `students` list.

Example:

```text
Student Deleted Successfully
```

This feature demonstrates the use of list modification and dictionary-based record searching.

---

# 📚 5. Display Subjects Offered

The program displays **each student's name and their subjects on the same line**.

The program uses:

```python
for student in students:
    print(f"{student['name']}: {', '.join(student['subjects'])}")
```

### Example Output

```text
<<<<<<<<<<<<<<<<<<<< Display Subjects Offered >>>>>>>>>>>>>>>>>>>>

Alice: Python, Math, English
Bob: Python, Excel
Rahul: Java, Python
```

The `join()` method converts the subject list into a readable comma-separated format:

```python
', '.join(student['subjects'])
```

This makes it easy to identify **which subjects belong to each student**.

---

# 🚪 6. Exit

The user can select option `6` to exit the application.

```text
Thank you.
```

The program then terminates using:

```python
exit()
```

---

# 🧠 Python Concepts Practised

This project combines multiple Python concepts.

## 🐍 Variables

```python
student_name = input("Name: ")
student_age = int(input("Age: "))
```

## 📋 Lists

```python
students = []
scores = []
subjects = []
```

## 📖 Dictionaries

```python
student = {
    "name": student_name,
    "age": student_age,
    "subjects": subjects,
    "scores": scores
}
```

## 🔢 Tuples

The project uses tuples for Student ID and Date of Birth:

```python
"student_id": (student_id,)
```

```python
"date_of_birth": (student_Date_of_Birth,)
```

## 🔤 String Methods

The `split()` method separates comma-separated subjects:

```python
subjects = subject.split(",")
```

The `join()` method displays subjects neatly:

```python
', '.join(student['subjects'])
```

## 🔁 For Loop

The project uses `for` loops to process student records:

```python
for student in students:
    ...
```

## 🔄 While Loop

The main menu continuously runs using:

```python
while True:
    ...
```

## 🔀 Conditional Statements

Menu choices are handled using:

```python
if choice == 1:
    ...
elif choice == 2:
    ...
elif choice == 3:
    ...
```

## 🧮 Built-in Functions

The project uses:

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

Since the project uses Python's built-in features, no external libraries are required for the current version.

---

# 🚀 How to Run the Project

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

Through this project, I practised:

* 🐍 Python fundamentals
* 📋 List manipulation
* 📖 Dictionary manipulation
* 🔢 Tuple usage
* 🔤 String methods
* 🔁 For loops
* 🔄 While loops
* 🔀 Conditional statements
* ⌨️ User input handling
* 🧮 Basic calculations
* 🗂️ Data organization
* 🧠 Problem-solving
* 🏗️ Menu-driven application development

---

# 📌 Key Learning Outcomes

### 📋 Working With Lists

Learned how to store and manipulate multiple student records and scores.

### 📖 Working With Dictionaries

Learned how to organize different pieces of information belonging to each student.

### 🔢 Working With Tuples

Practised storing Student ID and Date of Birth as tuple values.

### 🔤 String Processing

Practised using `split()` and `join()` for handling subject information.

### 🧮 Data Processing

Learned how to calculate total scores, averages, and grades from student data.

### 🧠 Problem Solving

Applied Python concepts to create a practical student management application.

---

# 🔮 Future Enhancements

The project can be extended with additional features such as:

* 🔎 Search student by name
* 🔍 Search student by Student ID
* 📊 Sort students by average
* 🏆 Display top-performing student
* 📉 Display students who failed
* 📚 Display unique subjects
* ✏️ Update individual fields
* 💾 Save student data to JSON
* 📂 Export student data to CSV
* 🗄️ Store student records in a database
* 🖥️ Build a graphical user interface
* 🌐 Convert the project into a web application
* 📊 Add student performance analytics

---

# 🗺️ Project Roadmap

```text
[████████████████████] 100% Student Data Structure

[████████████████████] 100% Add Student

[████████████████████] 100% Display Students

[████████████████████] 100% Update Student

[████████████████████] 100% Delete Student

[████████████████████] 100% Display Subjects

[████████████████████] 100% Grade Calculation

[██████████░░░░░░░░░░]  50% File Storage

[████░░░░░░░░░░░░░░░░]  20% Database Integration

[██░░░░░░░░░░░░░░░░░░]  10% GUI Application
```

---

# 🧩 Possible Future Data Structure

The current application stores data temporarily in a Python list.

In the future, the student information could be saved as JSON:

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

This would allow student records to remain available even after the program is closed.

---

# ⭐ Why I Built This Project

This project was created to strengthen my understanding of Python collection data types and apply them to a practical real-world problem.

Instead of practising individual Python concepts separately, this project combines:

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

This project helped me understand how different Python concepts can work together to build a complete application.

---

# 👨‍💻 About The Developer

<div align="center">

## Python Developer | Data Science & AI/ML Learner

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

# 🌐 Connect With Me

<div align="center">

### GitHub

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/)

### LinkedIn

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/)

</div>

---

# ⭐ Support The Project

If you found this project useful or interesting:

⭐ **Star** this repository

🍴 **Fork** this repository

💬 **Share** your feedback

🤝 **Connect** with me

---

<div align="center">

# 🚀 Keep Learning. Keep Building. Keep Growing.

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=700&lines=Python+%7C+Data+Structures+%7C+Problem+Solving;Build+Projects+%7C+Learn+Concepts+%7C+Grow+Skills;Keep+Learning+%7C+Keep+Building" alt="Animated Footer"/>

<br><br>

**Made with ❤️ and Python**

</div>
