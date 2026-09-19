'''
OOP --> object oriented programming --> objects (class,objects)

POP --> procedure oriented programming -->  functions

#chair(objects) --> wood (materials),design(dimensions),person

a class is a blueprint of a object

a object is a real world entity which contains --> attributes (variables)
                                               --> methods (functions)

class keyword

flipkart --> products --> laptop,mobiles,gadgets.....

features --> encapsulation,inheritance,polymorphism

class ClassName:
    """docstring"""
    #attributes (define the data)
    ......
    ......
    def fname(self):#behaviour
    def __init__(self):
        statement(s)...
        ..........
obj = ClassName()

#students --> name,age

class Students:
    """Students details"""
    name = "Harsha"
    age = 22
    place = "Vizag"

    def details(self):
        print(f'{self.name} is in {self.place} and age of {self.age} years')

#creation of objects
st1 = Students()
print(st1)
print(dir(st1))
print(st1.name,st1.age,st1.place)
#print(st1.details()) #nameerror as we have thrown self but no reference
#now we pass the reference
st1.details()
st2 = Students()
st2.details()

# in above case how many objects u create the result will be same

class Students:
    """Student details for multiple students"""
    def details(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    # now to access those details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')

st1 = Students()
st1.details("vardhan",22,"vizag")
print(st1.name,st1.place)
st1.display()
print(st1.__class__)
print(st1.__doc__)
print(st1.__dict__)
st2 = Students()
st2.details("harsha",22,"vizag")
st2.display()
print(st2.__dict__)
    

#in this case we want object to be initialized --> __init__()
class Students:
    """Student details for multiple students"""
    def __init__(self,name,age,place):
        self.name = name #instance variables
        self.age = age
        self.place = place
    # now to access those details
    def display(self): #instance method
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1 = Students("venkat",22,"vizag")
st1.display()
print(st1.__dict__)
st2 = Students("sai",22,"vizag")
st2.display()
print(st2.__dict__)



#create a cars class with attributes as brand,name,price
#create multiple objects

class Cars:
    """ Car details for multiple brands"""
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def display(self):
        print(f'Car brand is {self.brand} Car name is {self.name} and Car price is {self.price}')
c1 = Cars("toyota","innova","49L")
c1.display()


#encapsulation --> how the methods and attributes are binded to single
#class,in similar way how we can access the data --> public,protected,private

#public attributes --> can be created and modified even outside the class

class Users:
    """usage of public attributes"""
    def __init__(self,username):
        self.user = username #public attributes
    def display(self):
        print(f'username is {self.user}')
u1 = Users("john")
print(u1.user)
u1.user = "sam" # we can modify the public attribute
print(u1.user)
u1.display()


#protected attribute --> these can also be modified outside the class its mainly useful as a hint/coding convention for other users/developers to create a protected attribute we use underscore --> _otp
class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp):
        self.user = username #public attributes
        self._otp = _otp # protected attribute
    def display(self):
        print(f'username is {self.user}')
        print(f'OTP is {self._otp}')
u1 = Users("sai",4567)
u1.display()
u1._otp = 5432
u1.display()


#private attribute --> restrict the usage and cannot be directly accessed
#we have the usage or notation asdouble leading underscore --> _password
class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp,__password):
        self.user = username #public attributes
        self._otp = _otp # protected attribute
        self.__password = __password  # private attribute
    def display(self):
        print(f'username is {self.user}')
        print(f'OTP is {self._otp}')
u1 = Users("anil",5432,"anil@123")
print(u1.user,u1._otp)
#print(u1.__password)
print(u1.__dict__)
#in above case password can't be accessed directly --> NameMangling
print(u1._Users__password)

'''
#usage of getter(),setter() methods
class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp,__password):
        self.user = username #public attributes
        self._otp = _otp # protected attribute
        self.__password = __password  # private attribute
    #usage of getter(),get() method for password
    def get_password(self):
        """ getter method for password"""
        #return "******"
        return self.__password
    #usage of setter() to modify the data
    def set_password(self,new_password):
        if len(new_password) < 6:
            return 'password length is not matching'
        else:
            self.__password = new_password
            return 'updated password'
u1 = Users("admin",5432,"admin")
print(u1.get_password())
print(u1.set_password("admin"))  #you are not satisfying password reqmnts
print(u1.set_password("admin123")) # in this case satisfied
print(u1.get_password())
print(u1.__dict__)



