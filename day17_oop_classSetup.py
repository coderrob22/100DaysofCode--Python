class User:
    pass #This is how you can create a class and leave it alone w/o adding anything to it.

user_1= User()  #this is how you creat a new object from that class. You initialize the with the      parenthesis.

#Using a constructor AKA Initializing

class Using:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name


another_one = Using('001', 'Sonic')

print(another_one.name)