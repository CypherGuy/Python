classMail = 3.50
price = float(input('Enter price: '))
if price < 15: price += 3.50
nextDayQuestion = input("Type 'yes' or 'no' to if you want next day delivery: ")
if nextDayQuestion == 'yes': price += 5.00
print(f"Customer pays £{price}")