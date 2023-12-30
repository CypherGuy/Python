
target = input("Target number: ")
integer max = length(array)
for row = 0 to max - 1
    if array[row] == target then #Got numebr
        print("Found it!")
    else: #Not got
        if array[row] < max then #Can still iterate
            next row 
        else: #Not in list
            print("Not here")
        endif
    endif
endfor
