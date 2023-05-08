import re
import json
UMD_MAJORS = {
    'A. James Clark School of Engineering': ['Aerospace Engineering', 'Chemical and Biomolecular Engineering', 'Civil and Environmental Engineering', 'Computer Engineering', 'Electrical Engineering', 'Materials Science and Engineering', 'Mechanical Engineering'],
    'College of Agriculture and Natural Resources': ['Agricultural and Resource Economics', 'Animal Sciences', 'Environmental Science and Policy', 'Plant Science'],
    'College of Arts and Humanities': ['Art History', 'Classical Languages and Literatures', 'Communication', 'Dance', 'English Language and Literature', 'Film Studies', 'French Language and Literature', 'Germanic Studies', 'Linguistics', 'Music', 'Philosophy', 'Spanish Language and Literature', 'Theatre', 'Women\'s Studies'],
    'College of Behavioral and Social Sciences': ['Anthropology', 'Criminology and Criminal Justice', 'Economics', 'Geographical Sciences', 'Government and Politics', 'Psychology', 'Sociology'],
    'College of Computer, Mathematical, and Natural Sciences': ['Applied Mathematics and Statistics', 'Atmospheric and Oceanic Science', 'Biochemistry', 'Biological Sciences', 'Chemistry', 'Computer Science', 'Geology', 'Mathematics', 'Neuroscience and Cognitive Science', 'Physics', 'Physiology and Neurobiology', 'Statistics'],
    'College of Education': ['Education', 'Human Development and Quantitative Methodology', 'Special Education'],
    'College of Information Studies': ['Information Science'],
    'Philip Merrill College of Journalism': ['Journalism'],
    'Robert H. Smith School of Business': ['Accounting', 'Business Management', 'Finance', 'Management Information Systems', 'Marketing', 'Supply Chain Management'],
    'School of Architecture, Planning and Preservation': ['Architecture'],
    'School of Public Health': ['Health Administration and Policy', 'Public Health Science'],
    'School of Nursing': ['Nursing']
}

class Person:
    """Class that represents a person
    Attributes:
        name(str): Name of the person
        email(str): Email of the person
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Student(Person):
    """Class that represents student information
    Attributes:
        student_id(int): Unique id for each student
        major(str): Each student's major
        phone(int): Student's phone number
        credits(int): How many credits a student has
    
    """
    def __init__(self, student_id, name, major, email, credits):
        super().__init__(name, email)
        
        if not isinstance(student_id, int) or not isinstance(student_id,str):
            return TypeError("student id must be a int or str")
        id_match = re.match(r'^117\d{5}$', student_id)
        if not id_match:
            raise ValueError("Invalid student ID")  
        else:
            self.student_id = student_id 
        
        valid_majors = []
        for majors in UMD_MAJORS.values():
            valid_majors.extend(majors)
        
        if major not in valid_majors:
            raise ValueError("Invalid major")
        self.major = major
        
        self.credits = credits if isinstance(credits, int) and credits >= 0 and 12 <= credits <= 18 else None

        
class Course:
    """Class that represents class information
    

    """

    
    def __init__(self, name, section_number, credits_required, open_slots=20):
        """Intializes course object
        
        Attributes:
            name(string): name of course
            section_number(int): Unique section number of the course
            credits_required(int): Minimum amount of credits course requires for enrollment
            open_slots(int): How many open slots are available for the course
        
        """

        
        with open("courses_json.py", "r", encoding="utf-8") as f:
            for line in f:
                regular_expression = r"^(.+?)\s+(\d+)\s+(\d+)$"
                match = re.search(regular_expression, line)
                self.name = match.group(1)
                self.section_number = match.group(2)
                self.open_slots = match.group(3)
    
       
        self.credits_required = credits_required
        self.open_slots = open_slots
        self.enrollments = []
        self.waitlist = []
    
    def add_student(self, student):
        """Add student to a course
        
        Attributes:
            student(Student): Student to be added
        
        """
        
        if self.open_slots <= 0:
            print(f"No space avaiable for {self.name},{self.section_number}")
            alternative = input("Would you like to be added to the waitlist? (y/n)")
            if alternative == 'y':
                self.waitlist.append(student)
                print(f"You have been added to the waitlist for {self.name}, {self.section_number}")
        elif student in self.enrollments:
            print(f"{student} is already enrolled in {self.name},{self.section_number}")
        
        else:
            self.enrollments.append(student)
            self.open_slots-=1
            print(f"{student} has been enrolled in {self.name}, {self.section_number}")
        
        """
        for course in self.courses:
            if course.name == course_name and course.section_number == section_number:
                for enrollment in course.enrollments: 
                    if enrollment.name == student_name:
                        print(f"Error: {student_name} is already enrolled in {course_name} - Section {section_number}")
                        return
                if course.open_slots > 0:
                    course.enrollments.append(student_name)
                    course.open_slots -= 1
                    print(f"{student_name} has been enrolled in {course_name} - Section {section_number}")
                    return
                print(f"Error: No open slots available for {course_name} - Section {section_number}")
                return
        print(f"Error: Course {course_name} - Section {section_number} not found.")
        """
    def remove_student(self, student):
        """Remove student from a course
        
        Attributes:
            student_name(str): name of student to be removed
        
        """
        
        if student in self.enrollments:
            self.enrollments.remove(student)
            self.open_slots += 1
            print(f"{student} has been removed from {self.name}, {self.section_number}")
            if self.waitlist:
                student1 = self.waitlist.pop(0)
                self.enrollments.append(student1)
                self.open_slots -= 1
                print(f"{student1} has been enrolled in {self.name}, {self.section_number}")
        elif student in self.waitlist:
            self.waitlist.remove(student)
            print(f"{student} has been removed for the waitlist from {self.name}, {self.section_number}")
        else:
             print(f"Error: {student} is not enrolled in {self.name}, {self.section_number}.")
        
        
        """
        course_name = input("Enter course name: ")
        section_number = input("Enter section number: ")
        
        for course in self.courses:
            if course.name == course_name and course.section_number == section_number:
                for enrollment in course.enrollments: 
                    if enrollment == student_name:
                        course.enrollments.remove(enrollment)
                        course.open_slots += 1
                        print(f"{student_name} has been removed from {course_name} - Section {section_number}")
                        return
                print(f"Error: {student_name} is not enrolled in {course_name} - Section {section_number}")
                return
        print(f"Error: Course {course_name} - Section {section_number} not found.")
        """
        
    
    def main():
       
        with open('course_json.py', 'r', encoding='utf-8') as f:
            coursedata = json.load(f)
        courses_data = coursedata['courses']
        courses = []
        for course_data in courses_data:
            course = Course(course_data['name'], course_data['section_number'], course_data['credits_required'], course_data['open_slots'])
            courses.append(course)
    
    
        student_name = input("Enter student name: ")
        student_email = input("Enter student email: ")
        student_major = input("Enter student major: ")
        student_id = input("Enter student ID: ")
        student_credits = int(input("Enter student credits: "))
    
        student = Student(student_id, student_name, student_major, student_email, student_credits)
    
        while True:
            print("\nWhat would you like to do?")
            print("1. Add student to a course")
            print("2. Remove student from a course")
            print("3. Quit")
            choice = input("Enter your choice (1, 2, or 3): ")
        
            if choice == "1":
                course.add_student(student)
            elif choice == "2":
                course.remove_student(student)
            elif choice == "3":
                 break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

   