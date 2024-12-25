class Details:
    def __init__(self,name,age,location):
        print('name=',name)
        print('age=',age)
        print('location=',location)
one = Details('deepu','19','chowdepalli')
class  Details:
    def __init__(self):
        print('deepu')
        print('19')
        print('chowdepalli')
one = Details()
class Student:
    def __init__(self,no,name,sub):
        print('no=',no)
        print('name=',name)
        print('sub=',sub)
    def display(self, no, name, sub):
        print('no=', no)
        print('name=', name)
        print('sub=', sub)
one= Student('3227','deepu','python')
one.display('3227','deepu','python')
class Student:
    def m1(self,name,location):
        self.name = name
        self.location= location
    def m2(self):
        print(self.name)
        print(self.location)
s = Student()
s.m1('deepu','newyork')
s.m2()
class Student:
    def __init__(self,no,name,sub):
        self.no = no
        self.name = name
        self.sub = sub
    def display2(self):
        print(self.no)
        print(self.name)
        print(self.sub)
        print('\n')
s =Student('1','ramesh','python')
s.display()
s1=Student('2','suresh','django')
s1.display()
s2=Student('3','mahesh','java')
s2.display()
class Student:
    def __init__(self,no,name,sub):
        self.no = no
        self.name = name
        self.sub = sub
    def display(self):
        print(self.no)
        print(self.name)
        print(self.sub)
        print('\n')
s =Student('1','ramesh','python')
s.display()
s1=Student('2','suresh','django')
s1.display()
s2=Student('3','mahesh','java')
s2.display()
class Doctor:
    def __init__(self,no,name,spec):
        self.no = no
        self.name = name
        self.spec = spec
    def display(self):
        print(self.no)
        print(self.name)
        print(self.spec)
        print('\n')
d = Doctor('1','sachin','pediatric')
d.display()
d1 = Doctor('2','veena','ent')
d1.display ()
class Test:
    def __init__(self,x):
        self.y = x
    def f1(self):
      print(self.y)
t1 = Test(10)
print(t1.y)
class State:
    def __init__(self,name,capital,language):
        self.name = name
        self.capital = capital
        self.language = language
        print(self.name)
        print(self.capital)
        print(self.language)
        print('\n')
s1 = State('ap','amaravathi','telugu')
s2 = State('tamil nadu','chennai','tamil')
s3 = State('karnataka','banglore','kannada')
class Student:
    def __init__(self,name,branch,marks):
        self.name = name
        self.branch = branch
        self.marks = marks
        print(self.name)
        print(self.branch)
        print(self.marks)
        print('\n')
s1 = Student('deepika','cse ds','30')
s2 = Student('sumiya','ece','25')
s3 = Student('pravalika','ai&ds','29')
s4 = Student('sandhya','cse','23')
s5 = Student('madhu','civil','30')
class Test:
    class_variable =10
    def __init__(self):
        self.instance_variable=30
test_one = Test()
print(test_one.instance_variable)
print(Test.class_variable)

