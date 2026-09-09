emails_ids = ['saketh@codegnan.com','support@codegnan.com','ceo@codegnan.com','info@codegnan.com']
new_ids =['prasad@gmail.com','gautham@gmail.com','harsha@gmail.com']
emails_ids.extend(new_ids)
'''
print(len(emails_ids))
print(emails_ids[1])
print(emails_ids[-2:])


for mail in emails_ids:
    #print(mail)
    print(f'mail id of person is {mail}')
'''
users = {}
#users = dict.fromkeys(emails_ids)
'''for i in range(len(emails_ids)):
    users[i+1] = emails_ids[i]
print(users)'''

#enumerate --> it provides by default a counter object (you can store in desired collection)
#python --> object
#functions --> first class objects
#set is an unordered collection as no indexing

data=dict(enumerate(emails_ids,1))
print(data)