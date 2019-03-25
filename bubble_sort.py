def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        for k in range(0,n):
            if arr[k] < arr[k+1]:
                temp = arr[k+1]
                arr[k+1] = arr[k]
                arr[k] = temp
    return arr


arr = [16,2,4,8,-1,10,3,4]
print(bubble_sort(arr))
