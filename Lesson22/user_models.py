from pydantic import BaseModel, conint, constr

class User(BaseModel):
    id: int
    name: str
    age: int = 0
    email: str = 'noname@example.com'

user = User(id=1, name='John Doe')
print(user)

class AnotherUser(BaseModel):
    id: conint(gt=50)
    name: constr(min_length=2, max_length=50)


user1 = AnotherUser(id=51, name='Alice')
print(user1)
















