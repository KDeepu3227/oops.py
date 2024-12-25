###
create a class method hospital with a function named details method should take two parametrs name,dept and print them.create 3 different objects pass the values and display the results values should be taken a input from kb?
###
class Hospital:
    def details(self,name,department):
        print('name=',name)
        print('department=',department)
h = Hospital()
h.details('swapna','cardiologist')
h1 = Hospital()
h.details('deepu','gynecologist')
h1 = Hospital()
h.details('pravali','neurologist')
###
name= swapna
department= cardiologist
name= deepu
department= gynecologist
name= pravali
department= neurologist
