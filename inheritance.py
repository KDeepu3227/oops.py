class Calc:
    def add(self):
        print('add')
    def sub(self):
        print('sub')
    def mul(self):
        print('mul')
    def div(self):
        print('div')
one = Calc()
one.add()
one.sub()
one.mul()
one.div()
class X:
    a = 10
class Y(X):
    b = 20
y = Y
print(Y.a)
class X:
    a = 10
class Y(X):
    b = 20
class Z(Y):
    c = 30
z = Z
print(Z.a)
print(Z.b)
print(Z.c)
class A:
    x = 10
class B(A):
    y = 20
class C(A):
    z = 30
C = C()
print(C.x)
B = B()
print(B.y)
class A:
    x = 10
class B:
    y = 20
class C(A,B):
    z = 30
C = C()
print(C.z)
class A:
    x = 10
class B(A):
    y = 20
class C(A):
    z = 30
class D(B,C):
    W = 40
D = D()
print(C.x)
