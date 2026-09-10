'''
python project --> pop/oop --> DSA(logic based --> pattern based --> platform)
pop(procedure oriented programming) --> dividing the entire code into blocks --> procedures --> functions(def)
functions --> a reusable block of code(a block of statements which performs a specific task)

syntax:
def <funcname>(parameters): # func def
    """doc string"""
    statement(s)...
    ...........      # body of func
    return value(s)...
fname(args)  # func call


# simple scenario to understand

def add(a,b):
    """ addition function"""
    c=a+b
    return c
print(add(4,6))  # addition
c,d = 'codegnan','vizag'
print(add(c,d))  #concatenation
e,f = map(str,input("enter the value: ").split(','))
print(add(e,f))
print(add([1,3,4],[4,6,7]))  #merging
#print(add(1,2,3,4))  #positional arguments fail


#variable length arguments --> *args we can pass any number of positional arguments --> data will be stored in tuple...()

def sample(*a):
    """ demo of variable length arguments"""
    print(a)
    print(type(a))  # default it stores in tuple format
sample()
sample(2,3,4,5)
sample('codegnan',[2,35],'vizag',2+4j)

marks = [20,15,25,18]
sample(marks)
sample(*marks)
# * is used to unpack the values into a collection
a,*b,c = 12,'code','poll',23,4,9
print(a)
print(b)
print(c)

def add(*a):
    """ perform addition for numeric values"""
    print(a)
    result = 0
    for i in a:
        #print(i)
        #if type(i) in [int,float]:
        if type(i) == int or type(i) == float:
            result = result + i
    return result
print(add(2,3,4))
print(add(2,'code',3,4))


#keyword arguments --> we can pass the name for the arguments
def batch(age,name="harsha",place="vizag"):  # error --> non default always follows a default arguments
    """keyword arguments usage"""
    print(f'{name} is in {place} and age is {age} years')
batch('codegnan',1,'vizag')
batch(place='vizag',name='codegnan',age =1)
#keywors arguments only needs name matching not order
batch(age = 23)
#default arugments can accept a value as default


print(4,5,sep=':') #here keyword argument is sep and we are changing the default value for sep

'''
#keyword variable length argument (**kwargs) --> any number of keyword arguments,add is stored in dictionary

def batch(**a):
    """keyword variable length arguments usage"""
    print(a)
    print(type(a))
batch ()
batch(name="harsha",age=22,place = "vizag",branch="CSE")
data = {'names':['harsha','vardhan'],
        'place':['vizag','VSP']}
#batch(**data)
data.update({'batch':'PFS-VSP-007'})
print(data)

#task - create a function with the usage of * and **
