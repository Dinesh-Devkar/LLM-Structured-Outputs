from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person=Person(name='Dinesh',age='27')
another_person:Person = {'name':'Devabhai','age':22}
print(new_person)
print(another_person)