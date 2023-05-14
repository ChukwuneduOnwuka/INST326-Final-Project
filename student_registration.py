import re
import json
import argparse
import sys

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
    """
    def __init__(self, student_id, name, major, email):
        """Intializes the attributes and variables of the class
        
        Attributes:
            student_id(int): Unique id for each student
            name(str): Name of student
            major(str): Each student's major
            email(str): Stduents email
            
        """
        super().__init__(name, email)
        
        if not isinstance(student_id, (int,str)):
            return ValueError("Invalid Student ID")
        id_match = re.match(r'^117\d{6}$', student_id)
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
        
        email_check = re.match(r'^.+@terpmail\.umd\.edu$', email)
        if not email_check:
            raise ValueError("Invalid email, must use university given email address.")
        else:
            self.email = email
        
    def __str__(self):
        return self.name + " " + self.student_id + " " + self.major + " " + self.email
        
class Course:
    """Class that represents class information
    
    Attributes:
        course_name (str): The name of the course
        section_number (int): The unique section number of the course
        enrollments (list): A list of student objects currently enrolled in the course
        waitlist (list): A list of student objects currently on the waitlist for the course
        max_enrollement(int): Sets the max number of student for each class at 20
        current_enrollement(int): A counter for each class current enrollement

    """

    
    def __init__(self, course_name, section_number, credits):
        """Intializes course object
        
        Attributes:
            course_name(str): name of course
            section_number(str): Unique section number of the course
            credits(int): Minimum amount of credits course requires for enrollment
    
         Side Effects:
             Initializes a new course with the given attributes and opens a file.
        
        """
        self.course_name = course_name
        self.section_number = section_number
        self.credits = credits
        self.enrollments = []
        self.waitlist = []
        self.max_enrollment = 20
        self.current_enrollment = 0
        
    
        
        with open("courses.json", "r", encoding="utf-8") as f:
            for line in f:
                regular_expression = r'^\s*"course_name":\s*"(.+)",\s*"section_number":\s*"(\d+)",\s*"credits":\s*(\d+)\s*$'
                match = re.search(regular_expression, line)
                if match and course_name.strip() == match.group(1).strip() and section_number == int(match.group(2)):
                    self.credits = int(match.group(3))
                    break
       
    def add_student(self, student):
        """Add student to a course or adds them to a waitlist if class is full
        
        Attributes:
            student(Student): Student to be added
        
        """
        
        if self.current_enrollment > self.max_enrollment:
            print(f"No space avaiable for {self.course_name},{self.section_number}")
            alternative = input("Would you like to be added to the waitlist? (y/n)")
            if alternative == 'y':
                self.waitlist.append(student)
                print(f"You have been added to the waitlist for {self.course_name}, {self.section_number}")
        elif student in self.enrollments:
            print(f"{student.name} is already enrolled in {self.course_name},{self.section_number}")
        
        else:
            self.enrollments.append(student)
            self.current_enrollment +=1
            print(f"{student.name} has been enrolled in {self.course_name}, {self.section_number}")
      
    def remove_student(self, student):
        
        
        """Remove student from a course. If class if full and a student is removed, then the first student on the waitlist g
            ets popped off and added to the course.
        
        Attributes:
            student_name(str): name of student to be removed
        
        """
        if student in self.enrollments:
            self.enrollments.remove(student)
            self.current_enrollment -= 1
            print(f"{student.name} has been removed from {self.course_name}, {self.section_number}")
        
            if self.waitlist:
                student1 = self.waitlist.pop(0)
                self.enrollments.append(student1)
                self.current_enrollment += 1
                print(f"{student1.name} has been enrolled in {self.course_name}, {self.section_number}")
                
        elif student in self.waitlist:
            self.waitlist.remove(student)
            print(f"{student.name} has been removed from the waitlist for {self.course_name}, {self.section_number}")
        
        else:
             print(f"Error: {student.name} is not enrolled in {self.course_name}, {self.section_number}.")
            
    
    def get_student_enrollments(self,student):
        """Returns the current schedule of a student
        
        Attributes:
            student(str): The student schedule that is being shown
            
        Returns:
            The students schedule
    
        """
        schedule = [self] if student in self.enrollments else []
        for course in self.enrollments:
            if course != self and student in course.enrollments:
                schedule.append(course)
        return schedule
    
    def __str__(self):
        """Informal string representation 
        
        Returns:
            Informal string representation of the course name, section number, student enrollments and waitlist
        
        
        """
        
        return f"{self.course_name} {self.section_number}, Enrollment: {self.enrollments},Waitlist: {self.waitlist}"
        
    
def main(file_path):
        """Adds, drops, or shows schedule of an inputted student using a filepath of courses.

        Args:
            filepath(str): File path for target file
    
        Side effects:
             Opens a file and prints to the console.
        
        """
    
        with open(file_path, 'r', encoding='utf-8') as f:
            coursedata = json.load(f)
        courses_data = coursedata['courses']
        courses = []
        for course_data in courses_data:
            course = Course(course_data['course_name'], course_data['section_number'], course_data['credits'])
            courses.append(course)
    
    
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        student_major = input("Enter student major: ")
        student_email = input("Enter student email: ")
        print(f"Student Information:\nName: {student_name}\nStudent ID: {student_id}\nMajor: {student_major}\nEmail: {student_email}")


       
        student = Student(student_id, student_name, student_major, student_email)
    
        while True:
            print("\nWhat would you like to do?")
            print("1. Add a course")
            print("2. Drop a course")
            print("3. Schedule")
            print("4. Quit")
            choice = input("Enter your choice (1, 2, 3, 4): ")
        
            if choice == "1":
                course_name = input("Enter course name: ")
                section_number = input("Enter section number: ")
                credits = int(input("Enter number of credits: "))
                for course in courses:
                     if course.course_name == course_name and course.section_number == section_number and course.credits == credits:
                         course.add_student(student)
                         break
                else:
                     print(f"Error: {course_name} {section_number} not found.")
                    
               
                
            elif choice == "2":
                course_name = input("Enter course name: ")
                section_number = input("Enter section number: ")
                credits = int(input("Enter number of credits: "))
                for course in courses:
                    if course.course_name == course_name and course.section_number == section_number and course.credits == credits:
                        course.remove_student(student)
                        break
                    else:
                         print(f"Error: {course_name} {section_number} not found.")
                         
            elif choice == "3":
                schedule= []
                for course in courses:
                    if student in course.enrollments:
                         schedule.append(f"{course.course_name} {course.section_number}")
                print("Enrollement Schedule:")
                for course in schedule:
                    print(course)
                
            elif choice == "4":
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
       

def parse_args(arglist):
    
    parser = argparse.ArgumentParser(description = "Add or remove student to a class")
    parser.add_argument("file_path", metavar="FILE_PATH", type=str, help="path to course file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file_path)

