


class User:
    name = 'No Name'
    email = ''
    password = '1111'
    account_number = 1

class Employee(User):
    base_pay = 15.50
    department = 'Teacher'

class Student(User):
    name = ''
    email = ''
    course = ''
