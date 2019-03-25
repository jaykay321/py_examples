def largest_sum(arr):
    major = 0
    accum = 0

    for num in arr:
        accum += num

        if num > accum:
            accum = num
        if accum > major:
            major = accum

    return major

arr = [-11,2,16,5,-8,9,1]

print(largest_sum(arr))
