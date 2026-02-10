# Student Management System

A comprehensive Python-based Student Management System with a command-line interface for managing student records.

## Features

- **Add Students**: Add new student records with ID, name, email, phone, address, and GPA
- **Remove Students**: Delete student records by ID
- **View All Students**: Display all students in the database
- **Search Students**: Search by name, email, or phone number
- **Update Information**: Modify student details (individual fields or multiple fields)
- **View Details**: Display specific student information
- **Top Students**: Get top N students by GPA
- **GPA Range Filter**: Find students within a specific GPA range
- **Statistics**: View database statistics (total students, average GPA, highest/lowest GPA)
- **Data Persistence**: Automatically saves and loads student data from JSON file

## Project Structure

```
student_management_system/
├── main.py           # Main application with CLI interface
├── student.py        # Student class definition
├── database.py       # Database management system
├── students_data.json # Student records (auto-generated)
└── README.md         # This file
```

## File Descriptions

### student.py
Defines the `Student` class with:
- Constructor for creating student objects
- Methods to update student information
- Conversion methods to/from dictionary (for JSON storage)
- String representation for display

### database.py
Implements the `StudentDatabase` class with:
- JSON file-based persistence
- CRUD operations (Create, Read, Update, Delete)
- Search functionality (by name, email, phone)
- GPA filtering and top students ranking
- Statistical calculations

### main.py
Provides the `StudentManagementUI` class with:
- Interactive command-line menu
- User input handling
- All CRUD operations
- Search and filter operations
- Data persistence

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Installation & Setup

1. Navigate to the project folder:
```bash
cd student_management_system
```

2. Run the application:
```bash
python main.py
```

## Usage

When you run the application, you'll see a menu with the following options:

1. **Add Student** - Enter student details to add a new record
2. **Remove Student** - Delete a student by ID
3. **View All Students** - List all students in the database
4. **Search Student** - Find students by name, email, or phone
5. **Update Student** - Modify existing student information
6. **View Student Details** - Display details of a specific student
7. **Get Top Students by GPA** - Show top N students ranked by GPA
8. **Get Students by GPA Range** - Filter students by GPA range
9. **View Statistics** - Display database statistics
10. **Save Database** - Manually save data to file
11. **Exit** - Close the application

### Example Usage:

```
1. Select "1. Add Student"
2. Enter Student ID: STU001
3. Enter Name: John Doe
4. Enter Email: john@example.com
5. Enter Phone: 1234567890
6. Enter Address: 123 Main St
7. Enter GPA: 3.85
```

## Data Storage

Student records are automatically saved to `students_data.json` in JSON format:

```json
[
    {
        "student_id": "STU001",
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "address": "123 Main St",
        "gpa": 3.85
    }
]
```

## Features Highlight

- **No External Dependencies**: Uses only Python standard library
- **Data Persistence**: Automatically saves data to JSON file
- **User-Friendly**: Interactive CLI with clear menus and prompts
- **Search Capabilities**: Multiple search options
- **Statistical Analysis**: View class statistics at a glance
- **Validation**: Input validation for GPA and other fields

## Future Enhancements

- Database support (SQLite, MySQL)
- GUI interface using tkinter
- Export to CSV/Excel
- Student enrollment management
- Grade management
- Advanced reporting

## License

This project is free to use and modify.
made By Neha Kumari