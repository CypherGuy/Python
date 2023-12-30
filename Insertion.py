
def insertionSort(nList): 
    for i in range(1, len(nList)):
        key = nList[i]
 
        # Move elements of nList[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1 
        while j >= 0 and key < nList[j]:
            nList[j + 1] = nList[j] #Moves the item 1 right
            j -= 1
        nList[j + 1] = key
 
 
# Driver code to test above
nList = [12, 11, 13, 5, 6]
insertionSort(nList)
for item in nList:
    print(item)
