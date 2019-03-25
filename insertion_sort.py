def ins_sort(arr):
    for i in range(1,len(arr)):
        currentValue = arr[i]
        position = i
        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position = position - 1
        arr[position] = currentValue

    return arr


arr = [14,2,-5,7,11,-3,1]

print(ins_sort(arr))
