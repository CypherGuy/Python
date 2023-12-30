import typing #To make things optional
import sys

basket = dict({})
prods = ('Beans', 2.00), ('Rocks', 0.50), ('Lemons', 1.20)
itemsSold = {}

def getProdDetails(both: typing.Optional[bool] = True):
    names = [x[0] for x in prods]
    prices = [x[1] for x in prods]
    return (names, prices) if both else names

def getBasketDetails() -> list:
    names = list(basket.keys())
    quantity = list(basket.values())
    return names, quantity


def launchMenu():
#Launches the main menu
    print("Please enter 'a' to add an item, 'r' to view your current reciept, 'c' to checkout, 't' to view your running total and 'p' to view current products and their prices")
    direction = input("In addtion, you may enter 'ADs' to view total items sold or 'ADc' to view your total revenue.")
    if str(direction) == 'a': 
        addItem()
        launchMenu()

    if str(direction) == 'p': 
        viewProds()
        launchMenu()

    if str(direction) == 't': 
        tot = total()
        print(f'Your current running total is: £{tot:.2f}')
        launchMenu()

    if str(direction) == 'r': 
        printReciept()
        launchMenu()

    if str(direction) == 'c': 
        checkout()
        sys.exit()

    if str(direction) == 'ADs': 
        viewQuantitySold()
        launchMenu()

    if str(direction) == 'ADc': 
        showTotalMade()
        launchMenu()

def showTotalMade():
    total = 0
    for j in range(len(itemsSold)):
        try:
            itemName = list(itemsSold.keys())[j]
        except:
            continue
        for i in prods:
            if i[0] == itemName:
                toAdd = i[1] * itemsSold[itemName]
                total += toAdd
    print(f'The total price of everything sold is: £{total:.2f}')
    
def addToSoldItems(food: str, quant):
    try:
        itemsSold[food] += quant
    except KeyError:
        itemsSold[food] = quant

def viewQuantitySold():
    if itemsSold:
        print('\n')
        for i in range(len(itemsSold)):
            print(f"You have sold {list(itemsSold.values())[i]} {list(itemsSold.keys())[i]}")
        return print('\n')
    print("Nothing has been sold just yet :)")
        
def checkout():
    totalPrice = total()
    decision = str(input(f"Your total is {round(totalPrice, 2)}0. Would you like a receipt? type 'y' or 'n'."))
    if decision not in ('y', 'n'):
        print("That is an invalid answer. Please go back and retry.")
        return launchMenu()
    if decision == 'y':
        printReciept()
        print("Your receipt has been printed. Have a nice day!")
    else:
        print("Your receipt has been refused. Have a good day!")
        sys.exit(0)

def addItem():
    food = input('Enter item key: ')
    names = getProdDetails(False)
    names = list(names)
    if food not in names:
        return print(f"Item `{food}` is not in the shop.")

    quant = int(input("Enter how many you want to buy: "))
    if quant <= 0 or quant > 20:
        print("Please choose a reasonable amount, you can't give us stuff, nor can we give more then 20 items in a go!")
        return launchMenu()
    try:
        if basket[food]:
            addToSoldItems(food, quant)
            basket[food] += quant
    except KeyError:
        addToSoldItems(food, quant)
        basket[food] = quant
    print(f"{quant} {food} added to receipt!")
    print(basket)

def viewProds():
    print('\n')
    i = 0
    names, prices = getProdDetails()
    for i in range(len(prods)):
        print(f'{i + 1}) {names[i]}          £{prices[i]:.2f}')#To 2sf
        i += 1
    print('\n')
    launchMenu()

def total():
    total = 0
    for j in range(len(basket)): #Get values of dict
        try:
            itemName = list(basket.keys())[j]
        except Exception:
            continue
        for i in prods:
            if i[0] == itemName:
                toAdd = i[1] * basket[itemName]
                total += toAdd
    return total

def printReciept():
    import tabulate#Allows you to make nice tables given a list of data
    from tabulate import tabulate
    table = [['ITEM NAME', 'QUANTITY', 'PRICE']]
    i = 0
    baskName, baskQuant = getBasketDetails()
    i = 0
    for j in range(len(basket)): #Get values of dict
        try:
            itemName = list(basket.keys())[j]
        except Exception:
            continue
        for k in prods:
            if k[0] == itemName:
                price = k[1] * basket[itemName]
                table.append([baskName[i],baskQuant[i], round(price, 2) ])
                i += 1
    totalPrice = total()
    table.append(['TOTAL PRICE', '', round(totalPrice, 2)])
    print('\n')
    print(tabulate(table, headers='firstrow', tablefmt='grid'))
    print('\n')

launchMenu()