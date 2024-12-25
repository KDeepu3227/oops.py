class A:
    def function_one(self):
        print('class A function one')
    def function_two(self):
        print('class A function two')
class B(A):
    def function_two(self):
        super().function_two()
        print('class B function two')
    def function_three(self):
        print('class B function three')
one = B()
one.function_one()
one.function_two()
one.function_three()
try:
    x = int(input("enter the number"))
    print(x)
    y = [10,20,30]
    print(y[0])
    print(y[1])
    print(y[2])
except ValueError:
    print("enter a valid number__")
except NameError:
    print("x is valid")
except IndexError:
    print("you are accessing wrong position")
x = [1,2,3,4,5]
try:
    print(10/0)
except:
    print("it is not divisible by zero")
try:
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])
    print(x[4])
    print(x[5])
except IndexError:
    print("you are accessing wrong position")
    


