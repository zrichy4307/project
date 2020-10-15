  


# parent class User
class User:
    name = 'Jane'
    email = 'Jane@gmail.com'
    password = 'abcdefgh'

    def getLoginInfo(self):
        entry_name = input('Enter your name: ')
        enrty_email = input('Enter your email: ')
        entry_password = input('Enter your password: ')
        if (entry_email == self.email and entry_password == self.password):
            print('Welcome back, {}!'.format(entry_name))
        else:
            print('The password or email is incorrect.')

    

# child class Student
class Student(User):
    GPA = 4.0
    classification = 'Student'
    pin_number = '4598'

    def getLoginInfo(self):
        entry_name = input('Enter your name: ')
        enrty_email = input('Enter your email: ')
        entry_password = input('Enter your password: ')
        if (entry_email == self.email and entry_pin == self.pin):
            print('Welcome back, {}!'.format(entry_name))
        else:
            print('The password or email is incorrect.')


# child class Parent
class Parent(User):
    classification = 'Parent'
    address = '111 Main Street'
    pin_number = '6734'

    def getLoginInfo(self):
        entry_name = input('Enter your name: ')
        enrty_email = input('Enter your email: ')
        entry_password = input('Enter your password: ')
        if (entry_email == self.email and entry_pin == self.pin):
            print('Welcome back, {}!'.format(entry_name))
        else:
            print('The password or email is incorrect.')























if __name__ == '__main__':
# The following code invokes the methods inside each class for Teacher and Parent

    teacher = User()
    teacher.getLoginInfo()

    parent = Parent()
    parent.getLoginInfo()
