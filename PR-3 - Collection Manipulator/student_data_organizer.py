print("~"*25,"Welcome to the student Data Organizer!","~"*25)

students = []

while True:
    print("\nSelect an option: ")
    
    list_of_menu = ["1. Add Student",
                    "2. Display All Students",
                    "3. Update Student Information",
                    "4. Delete Student",
                    "5. Display Subjects Offered",
                    "6. Exit"]
    
    for menu in list_of_menu:
        print(menu)
        
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        
        print("\nEnter student details:")
        
        student_id = int(input("Student Id: "))
        student_name = input("Name: ")
        student_age = int(input("Age: "))
        student_Date_of_Birth = input("Date of Birth (YYYY-MM-DD): ")
        
        subject = input("Subjects (Comma-separated): ")
        subjects = subject.split(",")
        
        scores = []
        for sub in range(len(subjects)):
            score = int(input(f"Enter a score {subjects[sub]}: "))
            scores.append(score)
            
        add_student = {
            "student_id":(student_id,),
            "name":student_name,
            "age":student_age,
            "date_of_birth":(student_Date_of_Birth,),
            "subjects":subjects,
            "scores":scores     
        }
        students.append(add_student)
        
        for student in students:        
            total = sum(student["scores"])
            average = total/len(student["scores"])
            
            if average > 95:
                grade = "A+"
            elif average > 90:
                grade = "A"
            elif average > 85:
                grade = "B+"
            elif average > 80:
                grade = "B"
            elif average > 75:
                grade = "C+"
            elif average > 70:
                grade = "C"
            elif average > 65:
                grade = "D+"
            elif average > 60:
                grade = "D"
            elif average > 55:
                grade = "E+"
            elif average > 50:
                grade = "E"
            else:
                grade = "F"
                
            student["total"] = total
            student["average"] = average
            student["grade"] = grade
           
            
        print("\nStudent Added Successfully.\n")
            
    
    elif choice == 2:
        print("\n","<"*20,"Display All Students",">"*20,"\n")
        for student in students:
            print("Student ID:",student["student_id"][0],"|","Name:",student["name"],"|","Age:",student["age"],"|","Subjects:",student["subjects"],"|","Date of Birth:",student["date_of_birth"][0],"|","Scores:",student["scores"],"|","Total:",student["total"],"|","Grade:",student["grade"],"|",f"Average:{student['average']:.2f}")
        
    
    
    elif choice == 3: 
        print("\n","<"*20,"Update student information",">"*20)
        
        stud_id = int(input("\nEnter a Student id to you want to update details: ")) 
         
        for student in students:
            if student["student_id"][0] == stud_id:
                
                new_name = input("Enter a new name:")
                new_age = int(input("Enter a new age:"))
                new_date_of_birth = input("Enter a new Date of Birth (YYYY-MM-DD): ")
                student["name"] = new_name
                student["age"] = new_age
                student["date_of_birth"] = (new_date_of_birth,)
                
                new_subjects = input("Enter a new subjects (Comma-separated):")
                new_subject = new_subjects.split(",")
                student["subjects"] = new_subject
                
                new_scores = []
                for i in range(len(new_subject)):
                    new_score = int(input(f"Enter a score of {new_subject[i]}:"))
                    new_scores.append(new_score)
                student["scores"] = new_scores
                
                total = sum(new_scores)
                average = total / len(student["scores"])
                
                if average >= 95:
                    grade = "A+"
                elif average >= 90:
                    grade = "A"
                elif average >= 85:
                    grade = "B+"
                elif average >= 80:
                    grade = "B"
                elif average >= 75:
                    grade = "C+"
                elif average >= 70:
                    grade = "C"
                elif average >= 65:
                    grade = "D+"
                elif average >= 60:
                    grade = "D"
                elif average >= 55:
                    grade = "E+"
                elif average >= 50:
                    grade = "E"
                else:
                    grade = "F"

                student["total"] = total
                student["average"] = average 
                student["grade"] = grade  
                 
                print(f"\nStudent updated Successfully.")
                
                break
        else:
            print("\nStudent id not found.")
    
    elif choice == 4:
        print("\n","<"*20,"Delete Student",">"*20)
        
        delete_student = int(input("\nEnter a student id: "))
        
        for student in students:
            if student["student_id"][0] == student_id:
                students.remove(student)
                print("\nStudent Deleted Successfully")
                
    elif choice == 5:
        print("\n", "<"*20, "Display Subjects Offered", ">"*20)

        for student in students:
            print(f"{student['name']}: {', '.join(student['subjects'])}")
        
            
    elif choice == 6:
        print("\nThank you.")
        exit()
            
        
        
                
                
                
                
                         
            
            
            
        
            
        
        
     
        
                 
         
    
    
    