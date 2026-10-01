from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class Person(BaseModel):
    name:str="Raj"
    age:Optional[int]=None
    cgpa:Optional[int]=Field(lt=10,gt=1,description='represent the student cgpa grade',default=5)
    email_id:Optional[EmailStr]=None

person= Person(email_id='test@gmail.com')

print(person)
print(person.age)