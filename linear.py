
numbers = [1,2,3,4,5,6,7,8,9]
target = 4

# For loop
def forSearch(arr, x):
    found = False
    for i in range(len(arr)):
        if arr[i] == x:
            found = True
            return "Item found"

    if found == False:
        return "Item not found"


callSearch = forSearch(numbers, target)
print(callSearch)

# While loop
def whileSearch(arr, x):
    i = 0
    found = False
    while not found:
        if arr[i] == x:
            return "Item found"
        else:
            i += 1
    return "Item not found"
    


callSearch2 = whileSearch(numbers, target)
print(callSearch2)
