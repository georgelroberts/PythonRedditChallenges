class Employees:

    def __init__(self,first,last,email,pay):
        self.first=first
        self.last=last
        self.email=email
        self.pay=pay

    def fullname(self):
        return f'{self.first} {self.last}'

employee1=Employees('George','Roberts','glr28@cam.ac.uk',50000)
employee2=Employees('George2','Roberts2','glr28@cam.ac.uk2',500002)

Employees.fullname(employee2)