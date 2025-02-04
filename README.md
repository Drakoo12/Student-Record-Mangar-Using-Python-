# Student-Record-Mangar-Using-Python-
The Student class represents individual student records. Each student has the following attributes:

student_id: A unique identifier for each student.

name: The name of the student.

age: The age of the student.

grade: The current grade or class of the student.

The __init__ method initializes these attributes when a new Student object is created. The __str__ method provides a string representation of the student object, making it easier to display student details.

Student Management System Class:
The StudentManagementSystem class manages the collection of student records. It includes methods to:

Add a Student: The add_student method adds a new student to the system. It takes a Student object as input and appends it to the list of students.

View Students: The view_students method displays all the students in the system. If there are no students, it indicates that the list is empty.

Update a Student: The update_student method updates the details of an existing student. It allows updating the student's name, age, and grade based on the provided student ID.

Delete a Student: The delete_student method removes a student from the system based on the provided student ID.

Main Program:
The main program provides a menu-driven interface for the user to interact with the student management system. It includes the following options:

Add Student: Prompts the user to enter the details of a new student and adds the student to the system.

View Students: Displays a list of all students in the system.

Update Student: Prompts the user to enter the student ID and the new details to update an existing student.

Delete Student: Prompts the user to enter the student ID and deletes the corresponding student from the system.

Exit: Exits the program.
