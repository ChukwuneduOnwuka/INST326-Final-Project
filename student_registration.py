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