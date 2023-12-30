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
    run+=1
print('\n')

shopList = ['lemon', 'tomatoes', 'chair', 'Halima'] #Array or list

print('\nshopList before: {}'.format(shopList))
for i in range(4): #Remember that i can be anything
    shopList[i] = 'Bacon'
    i = i + 1

print('shopList after: {}'.format(shopList))

print('\n')

Halima = 11
if Halima > 10:
    print('Halima is over 10 years old')
elif Halima == 9:
    print("Halima is 9")
else:
    print("Halima is under 9")


print('\n')
class Vehicle: 
    def __init__(self, tyres, weight):
        self.tyres = tyres
        self.weight = weight

    def turn(self, amount):
        return ("The car has turned {} steps".format(amount))

    def turnOnLight(lightNum):
        return ('The car has turned on {} lights'.format(lightNum))


car = Vehicle(4, 5000)
print(car.tyres)
print(car.turn(5))
