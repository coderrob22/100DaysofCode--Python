class User:
    pass #This is how you can create a class and leave it alone w/o adding anything to it.

user_1= User()  #this is how you creat a new object from that class. You initialize the with the      parenthesis.

#Using a constructor AKA Initializing

class Using:
    def __init__(self, user_id, user_name):  #This init function is the constructor!
        self.id = user_id
        self.name = user_name
        self.followers = 0   #This is how you give a default value to an attribute for every object.
        self.following = 0    # There is no need to add it to the paramenter. It has a value already.

    def follow(self, user): #Always use the 'self' keyword when creating methods. Methods are funcs associated with objects.
        user.followers += 1
        self.following += 1

another_one = Using('001', 'Sonic')
user_2 = Using('002', 'China')

user_2.follow(another_one)

print(another_one.followers)
print(another_one.following)