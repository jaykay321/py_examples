def sel_sort(arr):
    for n in range(len(arr)-1,0,-1):
        max = 0
        for k in range(0,n+1):
            if arr[k] > arr[max]:
                max = k
        temp = arr[n]
        arr[n] = arr[max]
        arr[max] = temp
    return arr

arr = [-5,3,8,-4,10,1]
print(sel_sort(arr))
