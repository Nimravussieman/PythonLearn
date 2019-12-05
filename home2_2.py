import datetime
import random as r
class Person:
    def __init__(self,date = None,firstName = "Default",lastName = "Default"):
        self.firstName = firstName
        self.lastName = lastName
        if isinstance(date, datetime.date):
            self.date = date
        else:
            self.date = datetime.date.today()
    def get_age(self):
        return datetime.date.today().year - self.date.year
    def displayInfo(self):
        return "First name: "+self.firstName +"\nLast name: "+ self.lastName+"\nAge: "+ str(self.get_age())
    @staticmethod
    def is_teenager(obj):
        if isinstance(obj,Person) and 16 > (datetime.date.today().year - obj.date.year) > 13:
            return True
        return False

#print(isinstance(datetime.date.today(), datetime.date))

#pers = Person(datetime.date(1999,12,23),"first","Last")
#print(pers.displayInfo())


class Student(Person):
    def __init__(self,person):
        if isinstance(person,Person):
            self.firstName = person.firstName
            self.lastName = person.lastName
            self.date = person.date
        else:
            pass
    def displayInfo(self):
        return "Student " + super().displayInfo()
    def __repr__(self):
        return self.displayInfo()

class ClassRoom:
    def __init__(self,students = []):
        if isinstance(students,list):
            self.studentList = students
        else:
            self.studentList = []
    def addStudent(self,student):
        self.studentList.append(student)
    def displayInfo(self):
        for x in self.studentList:
            print(x.displayInfo())
    def __lt__(self,other):
        return True if len(self.studentList) < len(other.studentList) else False
    def __gt__(self,other):
        return True if len(self.studentList) > len(other.studentList) else False
    def __eq__ (self,other):
        return True if len(self.studentList) == len(other.studentList) else False



#Person("first","Last",datetime.date(1999,12,23))
#person = Person()

classRoom1 = ClassRoom([Student(Person(datetime.date(r.randint(2000,2012),r.randint(1,12),r.randint(1,28)),"studentFN"+str(x),"studentLN"+str(x))) for x in range(1,11)])
classRoom2 = ClassRoom([Student(Person(datetime.date(r.randint(2000,2012),r.randint(1,12),r.randint(1,28)),"studentFN"+str(x),"studentLN"+str(x))) for x in range(11,21)])

    #Person("studentFN"+str(x),"studentLN"+str(x),datetime.date(r.randint(2000,2012),r.randint(1,12),r.randint(1,29))) for  x in range(1,11)])

#print(tuple(["1","2"]).index("1"))


class Teacher(Person):
    def __init__(self,person):
        if isinstance(person, Person):
            if isinstance(person, Person):
                self.firstName = person.firstName
                self.lastName = person.lastName
                self.date = person.date
            else:
                pass
    def __repr__(self):
        return "Teacher"
    def displayInfo(self):
        print("Teacher")
        super().displayInfo()

class School:
    def __init__(self):
        self.teachers = dict()
        self.classrooms = []

    def add_techer(self,teacher,discipline = "ALL"):
        if isinstance(teacher, Teacher):
            if self.teachers.get(discipline):
                self.teachers.get(discipline).append(teacher)
            else:
                self.teachers[discipline]=[teacher]
            return True
        else:
            return False
    def add_class(self,classroom):
        if isinstance(classroom, ClassRoom):
            self.classrooms.append(classroom)
            return True
        return False

    @classmethod
    def get_teachers(cls, obj, discipline):
        #return [x for (k,v) in obj.teachers if k == discipline for x in v]
        return obj.teachers.get(discipline)

teacher1 = Teacher(Person(datetime.date(1979,12,23),"Teacherfirst1","TeacherLast1"))
teacher2 = Teacher(Person(datetime.date(1969,12,23),"Teacherfirst2","TeacherLast2"))

school = School()
school.add_techer(teacher1,"fiz")
school.add_techer(teacher2,"mat")

class Leson:
    def __init__(self,theme,teacher,discipline):
        self.theme = theme
        self.discipline = discipline
        self.teacher = teacher
    def __repr__(self):
        return "discipline: {}, theme: {}, teacher: {}".format(self.discipline,self.theme,self.teacher)

class Schedule:
    def __init__(self,leson,date,room):
        self.leson = leson
        self.date = date
        self.room = room
        self.absent = []
    def set_absent(self,student):
        self.absent.append(student)
class Schedules:
    def __init__(self):
        self.schedul_list = []

    def add_schedule(self,schedule):
        if isinstance(schedule,Schedule):
            self.schedul_list.append(schedule)

    def get_lesons_count(self,date):
        return len([x for x in self.schedul_list if x.date == date])

    def get_absents(self,date,discipline):
        return [y for x in self.schedul_list if x.date == date and x.leson.discipline == discipline for y in x.absent]
        #print(l)
