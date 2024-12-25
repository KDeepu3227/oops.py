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
class TypesMethod:
    def __init__(self):
        print("this is init method")
    def instance(self):
        print('this is instance method')
    @classmethod
    def class_method(cls):
        print("this is class method")
    @staticmethod
    def static_method():
        print('this is static method')
t1 = TypesMethod()
t1.instance()
TypesMethod.class_method()
TypesMethod.static_method()


