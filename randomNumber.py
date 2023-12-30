import sys
peopleDict = {}
def main():
    num = int(input("Enter random number form 1-100: "))
    flag = num #Used to keep track of the number variable
    if num > 50:
        num += 20
        num *= 5
        num -= flag
    else:
        num *= 20
        num -= flag
        num /= 2
    num = round(num)
    print(f"Your number is {num}.")
    try:
        age = int(input('How old are you? '))
        name = input("And what should we identify you as?")
        num += age
        peopleDict[name] = num
    except Exception:
        print("There was an error, maybe check your name or age and make sure it's a number/word?. Shutting down program..")
        sys.exit()
for _ in range(3):
    main()
for i in range(3):
    print(f'Person {list(peopleDict.keys())[i]} got a score of {list(peopleDict.values())[i]}')
while True:
    locator = str(input("Please enter the name of any person whose score you wish to view. Press 'ex' to exit."))
    if locator == 'ex':
        sys.exit()
    if locator in peopleDict:
        print(f'Person {locator} got a score of {peopleDict[locator]}')
    else:print("Person not found.")