def bin_search(arr,n):
    if n < arr[0] or n > arr[len(arr)-1]:
        raise ValueError("Given number is outside of the scope of array values")

    min = 0
    max = len(arr)-1

    while min < max:
        mid = int((min+max)/2)
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            min = mid
        else:
            max = mid
    return None

print(bin_search([1,6,7,8,9,10],1))
