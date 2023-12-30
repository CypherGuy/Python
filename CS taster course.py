"""
I use this code to teach beginner students about data types, 
loops, structures etc.. I used to use this code in my Summer School
Python introductory course.
"""

number = 6
word = 'Lemon'

try:
    print(number - 1)
    print(int(word * number))
except:
    print("The try except loop has broken because a word and a number can't be multiplied.")

print('\n')

run = 1
while run < 10:
    print(run)
    run += 1
print('\n')

shopList = ['lemon', 'tomatoes', 'chair', 'Halima']  # Array or list

print('\nshopList before: {}'.format(shopList))
for i in range(4):  # Remember that i can be anything
    shopList[i] = 'Bacon'
    i = i + 1

print('shopList after: {}'.format(shopList))

print('\n')

name = 11
if name > 10:
    print('Joe is over 10 years old')
elif name == 9:
    print("Joe is 9")
else:
    print("Joe is under 9")


print('\n')


class Vehicle:
    def __init__(self, tyres, weight):
        self.tyres = tyres
        self.weight = weight

    def turn(self, amount):
        return ("The car has turned {} steps".format(amount))

    def turnOnLight(lightNum):  # Why does this not work?
        return ('The car has turned on {} lights'.format(lightNum))


car = Vehicle(4, 5000)
print(car.tyres)
print(car.turn(5))
