"""Database management for storing and retrieving student records."""

import json
import os
from student import Student


class StudentDatabase:
    """Class to manage student database operations."""
    
    def __init__(self, filename='students_data.json'):
        """
        Initialize the database.
        
        Args:
            filename (str): Path to the JSON file storing student data
        """
        self.filename = filename
        self.students = {}
        self.load_from_file()
    
    def load_from_file(self):
        """Load student data from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for student_data in data:
                        student = Student.from_dict(student_data)
                        self.students[student.student_id] = student
                print(f"Loaded {len(self.students)} students from file.")
            except json.JSONDecodeError:
                print("Error reading database file. Starting with empty database.")
    
    def save_to_file(self):
        """Save student data to JSON file."""
        with open(self.filename, 'w') as f:
            data = [student.to_dict() for student in self.students.values()]
            json.dump(data, f, indent=4)
        print("Database saved successfully.")
    
    def add_student(self, student):
        """
        Add a new student to the database.
        
        Args:
            student (Student): Student object to add
            
        Returns:
            bool: True if added successfully, False if ID already exists
        """
        if student.student_id in self.students:
            print(f"Student with ID {student.student_id} already exists!")
            return False
        self.students[student.student_id] = student
        print(f"Student {student.name} added successfully.")
        return True
    
    def remove_student(self, student_id):
        """
        Remove a student from the database.
        
        Args:
            student_id (str): ID of the student to remove
            
        Returns:
            bool: True if removed, False if student not found
        """
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found!")
            return False
        name = self.students[student_id].name
        del self.students[student_id]
        print(f"Student {name} removed successfully.")
        return True
    
    def get_student(self, student_id):
        """
        Retrieve a student by ID.
        
        Args:
            student_id (str): ID of the student
            
        Returns:
            Student: Student object or None if not found
        """
        return self.students.get(student_id)
    
    def update_student(self, student_id, **kwargs):
        """
        Update a student's information.
        
        Args:
            student_id (str): ID of the student
            **kwargs: Key-value pairs to update
            
        Returns:
            bool: True if updated, False if student not found
        """
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found!")
            return False
        self.students[student_id].update_info(**kwargs)
        print(f"Student {student_id} updated successfully.")
        return True
    
    def get_all_students(self):
        """Get all students."""
        return list(self.students.values())
    
    def search_students(self, query, search_by='name'):
        """
        Search for students.
        
        Args:
            query (str): Search query
            search_by (str): Field to search (name, email, phone)
            
        Returns:
            list: List of matching Student objects
        """
        results = []
        query = query.lower()
        for student in self.students.values():
            if search_by == 'name' and query in student.name.lower():
                results.append(student)
            elif search_by == 'email' and query in student.email.lower():
                results.append(student)
            elif search_by == 'phone' and query in student.phone:
                results.append(student)
        return results
    
    def get_students_by_gpa(self, min_gpa=0.0, max_gpa=4.0):
        """
        Get students within a GPA range.
        
        Args:
            min_gpa (float): Minimum GPA
            max_gpa (float): Maximum GPA
            
        Returns:
            list: List of Student objects within GPA range
        """
        return [s for s in self.students.values() if min_gpa <= s.gpa <= max_gpa]
    
    def get_top_students(self, n=10):
        """
        Get top N students by GPA.
        
        Args:
            n (int): Number of top students to return
            
        Returns:
            list: List of top students sorted by GPA
        """
        sorted_students = sorted(self.students.values(), key=lambda s: s.gpa, reverse=True)
        return sorted_students[:n]
    
    def get_statistics(self):
        """Get database statistics."""
        if not self.students:
            return {
                'total_students': 0,
                'average_gpa': 0,
                'highest_gpa': 0,
                'lowest_gpa': 0
            }
        
        gpas = [s.gpa for s in self.students.values()]
        return {
            'total_students': len(self.students),
            'average_gpa': round(sum(gpas) / len(gpas), 2),
            'highest_gpa': round(max(gpas), 2),
            'lowest_gpa': round(min(gpas), 2)
        }
