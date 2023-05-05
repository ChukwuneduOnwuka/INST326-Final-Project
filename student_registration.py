import re
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

class Student:
    """Class that repesents student information
    Attributes:
        student_id(int): Unqiue id for each student
        name(string): Name of each student
        major(string): Each students major
        phone(int): Students phone number
        email(string): Students email
        credits(int): How many credits a student has
    
    """
    def __init__(self, student_id, name, major, phone, email, credits):
        """Intializes student object
        
        Attributes:
            student_id(int): Unqiue id for each student
            name(string): Name of each student
            major(string): Each students major
            phone(int): Students phone number
            email(string): Students email
            credits(int): How many credits a student has
        
        
        """
        if not isinstance(student_id, int):
            return TypeError
        
        if not isinstance(phone, int):
            return TypeError
        
        id_match = re.match(r'^117\d{5}$', student_id)
        phone_match =  re.match(r'^\d{10}$' ,phone)
        
        if not id_match:
            raise ValueError("Invalid student ID")
        if not phone_match:
            raise ValueError("Invalud phone number")
        
        
        self.student_id = student_id
        self.name = name
        self.major = major
        self.phone = phone
        self.email = email
        self.credits = credits
        
class Course:
    """Class that represents class information
    

    """
    
    def __init__(self, name, section_number, credit_required, open_slots):
        """Intializes course object
        
        Attributes:
            name(string): name of course
            section_number(int): Unique section number of the course
            credits_required(int): Minimum amount of credits course requires for enrollment
            open_slots(int): How many open slots are available for the course
        
        
        """
        self.name = name
        self.section_number = section_number
        self.credit_required = credit_required
        self.open_slots = open_slots
        self.enrollments = []
    
        
class Registration:
    
    def __init__(self):
        """intialize object
        
        
        """
        self.courses = []
        self.course_database = []
        
    def add_student(self, student):
        """Add student to a course
        
        Attributes:
            student(Student): Student to be added
        
        """
        return
    
    def remove_student(self,student):
        """remove student from a course
        
        Attributes:
            student(Student): student to be removed
        
        """
        return
        
        
    def add_course(self, course):
        """Add a course to the registration database
        
        Attributes:
            course(Course): Course to be added to registration database
        
        """
        return
        
    def remove_course(self, course):
        """Remove course from registration database
        
        Attributes:
            course(Course): Course to be removed from registration database
        
        
        """
         
        return
        
    
    def update_database(self, database):
        """Updates database
        
        """
        return