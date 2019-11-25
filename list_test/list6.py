bob = {'name': {'first': 'Bob', 'last': 'Smith'},
'age': 42,
'job': ['software', 'writing'],
'pay': (40000, 50000)}

#print(bob)
bob['job'][-1]
bob['job'].append('janitor')


bob2 = dict(name='bob smith', age=42, pay=30000, job='dev')
sue2 = dict(name='sue', age=45, pay=40000,job='hdw')

db={}
db['bob']=bob2
db['sue']=sue2
#print(db)



import pprint 
#pprint.pprint(db)


for key in db:
    print(key, '=>','$',db[key]['name'],db[key]['pay'])
    
