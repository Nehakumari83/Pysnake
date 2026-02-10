"""Command-line interface for the Student Management System."""

from database import StudentDatabase
from student import Student


class StudentManagementUI:
    """User interface for managing students."""
    
    def __init__(self):
        """Initialize the UI with the database."""
        self.db = StudentDatabase()
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*60)
        print("       STUDENT MANAGEMENT SYSTEM")
        print("="*60)
        print("1.  Add Student")
        print("2.  Remove Student")
        print("3.  View All Students")
        print("4.  Search Student")
        print("5.  Update Student")
        print("6.  View Student Details")
        print("7.  Get Top Students by GPA")
        print("8.  Get Students by GPA Range")
        print("9.  View Statistics")
        print("10. Save Database")
        print("11. Exit")
        print("="*60)
    
    def add_student(self):
        """Add a new student to the system."""
        print("\n--- Add New Student ---")
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone: ").strip()
        address = input("Enter Address: ").strip()
        
        try:
            gpa = float(input("Enter GPA (0-4.0): ").strip())
            if not (0 <= gpa <= 4.0):
                print("GPA must be between 0 and 4.0!")
                return
        except ValueError:
            print("Invalid GPA! Setting to 0.0")
            gpa = 0.0
        
        student = Student(student_id, name, email, phone, address, gpa)
        self.db.add_student(student)
    
    def remove_student(self):
        """Remove a student from the system."""
        print("\n--- Remove Student ---")
        student_id = input("Enter Student ID to remove: ").strip()
        self.db.remove_student(student_id)
    
    def view_all_students(self):
        """Display all students."""
        print("\n--- All Students ---")
        students = self.db.get_all_students()
        if not students:
            print("No students in the database.")
            return
        
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")
    
    def search_student(self):
        """Search for students."""
        print("\n--- Search Student ---")
        print("Search by: 1) Name  2) Email  3) Phone")
        choice = input("Enter choice (1-3): ").strip()
        
        search_options = {'1': 'name', '2': 'email', '3': 'phone'}
        if choice not in search_options:
            print("Invalid choice!")
            return
        
        query = input("Enter search query: ").strip()
        results = self.db.search_students(query, search_options[choice])
        
        if not results:
            print("No students found.")
            return
        
        print(f"\nFound {len(results)} student(s):")
        for i, student in enumerate(results, 1):
            print(f"{i}. {student}")
    
    def update_student(self):
        """Update a student's information."""
        print("\n--- Update Student ---")
        student_id = input("Enter Student ID: ").strip()
        
        student = self.db.get_student(student_id)
        if not student:
            print(f"Student with ID {student_id} not found!")
            return
        
        print("\nWhat would you like to update?")
        print("1. Name")
        print("2. Email")
        print("3. Phone")
        print("4. Address")
        print("5. GPA")
        print("6. Multiple fields")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter new name: ").strip()
            self.db.update_student(student_id, name=name)
        elif choice == '2':
            email = input("Enter new email: ").strip()
            self.db.update_student(student_id, email=email)
        elif choice == '3':
            phone = input("Enter new phone: ").strip()
            self.db.update_student(student_id, phone=phone)
        elif choice == '4':
            address = input("Enter new address: ").strip()
            self.db.update_student(student_id, address=address)
        elif choice == '5':
            try:
                gpa = float(input("Enter new GPA: ").strip())
                if 0 <= gpa <= 4.0:
                    self.db.update_student(student_id, gpa=gpa)
                else:
                    print("GPA must be between 0 and 4.0!")
            except ValueError:
                print("Invalid GPA!")
        elif choice == '6':
            updates = {}
            if input("Update name? (y/n): ").lower() == 'y':
                updates['name'] = input("Enter new name: ").strip()
            if input("Update email? (y/n): ").lower() == 'y':
                updates['email'] = input("Enter new email: ").strip()
            if input("Update phone? (y/n): ").lower() == 'y':
                updates['phone'] = input("Enter new phone: ").strip()
            if input("Update address? (y/n): ").lower() == 'y':
                updates['address'] = input("Enter new address: ").strip()
            if input("Update GPA? (y/n): ").lower() == 'y':
                try:
                    gpa = float(input("Enter new GPA: ").strip())
                    if 0 <= gpa <= 4.0:
                        updates['gpa'] = gpa
                except ValueError:
                    print("Invalid GPA!")
            
            if updates:
                self.db.update_student(student_id, **updates)
        else:
            print("Invalid choice!")
    
    def view_student_details(self):
        """View details of a specific student."""
        print("\n--- View Student Details ---")
        student_id = input("Enter Student ID: ").strip()
        
        student = self.db.get_student(student_id)
        if not student:
            print(f"Student with ID {student_id} not found!")
            return
        
        print(f"\n{student}")
    
    def get_top_students(self):
        """Display top students by GPA."""
        print("\n--- Top Students by GPA ---")
        try:
            n = int(input("How many top students to display? ").strip())
        except ValueError:
            n = 10
        
        students = self.db.get_top_students(n)
        if not students:
            print("No students in the database.")
            return
        
        print(f"\nTop {len(students)} Students:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")
    
    def get_students_by_gpa_range(self):
        """Get students within a GPA range."""
        print("\n--- Students by GPA Range ---")
        try:
            min_gpa = float(input("Enter minimum GPA: ").strip())
            max_gpa = float(input("Enter maximum GPA: ").strip())
        except ValueError:
            print("Invalid GPA values!")
            return
        
        students = self.db.get_students_by_gpa(min_gpa, max_gpa)
        if not students:
            print("No students found in that GPA range.")
            return
        
        print(f"\nFound {len(students)} student(s) with GPA between {min_gpa} and {max_gpa}:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")
    
    def view_statistics(self):
        """Display database statistics."""
        print("\n--- Statistics ---")
        stats = self.db.get_statistics()
        print(f"Total Students: {stats['total_students']}")
        print(f"Average GPA: {stats['average_gpa']}")
        print(f"Highest GPA: {stats['highest_gpa']}")
        print(f"Lowest GPA: {stats['lowest_gpa']}")
    
    def save_database(self):
        """Save the database to file."""
        self.db.save_to_file()
    
    def run(self):
        """Run the main application loop."""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-11): ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.remove_student()
            elif choice == '3':
                self.view_all_students()
            elif choice == '4':
                self.search_student()
            elif choice == '5':
                self.update_student()
            elif choice == '6':
                self.view_student_details()
            elif choice == '7':
                self.get_top_students()
            elif choice == '8':
                self.get_students_by_gpa_range()
            elif choice == '9':
                self.view_statistics()
            elif choice == '10':
                self.save_database()
            elif choice == '11':
                print("Saving database before exit...")
                self.save_database()
                print("Thank you for using Student Management System. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    ui = StudentManagementUI()
    ui.run()
