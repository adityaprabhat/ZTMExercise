# class PlayerCharacter():
#     membership = True
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def adding_things(cls,n1,n2):
#         return n1+n2

#     def run(self):
#         return self


# # print(PlayerCharacter.adding_things(2,3))
# player1 = PlayerCharacter("Roger",25)
# print(player1.run())
# print(isinstance(player1,object))
# print(player1)
from functools import reduce

class User():
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with a power of {self.power}')

class Archer(User):
    def __init__(self,name,arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')


class HydbridBorg(Wizard,Archer):
    def __init__(self,name,power,email):
        self.name = name
        self.power = power
        User.__init__(self,email)
        

hb1 = HydbridBorg("Doggie", 50, "doggie@bark.com");
print (hb1.name)
print (hb1.power)
print (hb1.email)

my_list = [1,2,3]

def accumulate(item,acc):
    return acc+item

print(reduce(accumulate,my_list,0))

