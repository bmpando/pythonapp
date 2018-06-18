
class Person:
__name=''
__email=''
def set_name(self,name):
    self.__name=name
def set_email(self,email):
    self.__email=email
def get_name(self):
    return self.__name
def get_email(self):
    return self.__email

brad=Person()
brad.set_name('Booker')
brad.set_email('bbbb')