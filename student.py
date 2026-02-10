"""Student class definition for the management system."""

class Student:
    """Class representing a student."""
    
    def __init__(self, student_id, name, email, phone, address, gpa=0.0):
        """
        Initialize a Student object.
        
        Args:
            student_id (str): Unique identifier for the student
            name (str): Student's full name
            email (str): Student's email address
            phone (str): Student's phone number
            address (str): Student's address
            gpa (float): Student's GPA (default 0.0)
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.gpa = gpa
    
    def __str__(self):
        """Return string representation of the student."""
        return (f"ID: {self.student_id} | Name: {self.name} | Email: {self.email} | "
                f"Phone: {self.phone} | Address: {self.address} | GPA: {self.gpa}")
    
    def update_info(self, **kwargs):
        """
        Update student information.
        
        Args:
            **kwargs: Key-value pairs of attributes to update
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def to_dict(self):
        """Convert student object to dictionary."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'gpa': self.gpa
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary."""
        return cls(
            student_id=data['student_id'],
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address'],
            gpa=data.get('gpa', 0.0)
        )
