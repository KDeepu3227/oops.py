###
take a subject name and marks as input from kb pass that to a method present in class named academics.call the methid display name and marks
###
subname = input("enter the name:")
marks = int(input("enter the marks:"))
class Academics:
    def a1(self,subname,marks):
        print('subname=',subname,'marks=',marks)
a = Academics()
a.a1(subname,marks)
###
enter the name:python
enter the marks:30
subname= python marks= 30
