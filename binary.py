numbers = ['1,2,3,4,5,6,7,8,9,10']
target = 2

low = 0
high = len(numbers) - 1
found = False

def binary(low, high, found, numbers, target):
    middle = int(high) // 2
    while not found:
        if numbers[middle] < target:
            low = middle
            middle = (low + high) // 2

        if numbers[middle] > target:
            high = middle
            middle = (low + high) // 2
        
        else:
            found = True
            return print('target found')

    return print("item not found")
    
test = binary(low, high, found, numbers, target)
print(test)