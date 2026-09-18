'''
module --> a module is simple python (reusable,organized code)

import keyword --> use import keyword to access module functions



organization --> class
encapsulation,inheritance,polymorphism

employees --> function(methods)
performance metrics --. function
increment --> function

emp1,emp2,emp3,........ --> objects

'''
def employees(*names,**settings):
    """employee details along with their settings"""
    print("employee names")
    for employee in names:
        print('-',employee)

    for key,value in settings.items():
        print("key is",key)
        print("value is",value)

#employees("rahul","akash","sunil",department = "operations",experience_letters = True,salary = True)

details = {'organization':'codegnan','year':2020,'branches':['vjy','hyd','vsp']}
print(__name__)   # dunder methods --> magic method
