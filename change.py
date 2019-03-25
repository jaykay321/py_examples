values = [100,50,20,10,5,2,1]
mem = []

def check_change(num,values,mem):

    if num in values:
        mem.append(num)
        return mem
    elif num > values[0]:
        mem.append(values[0])
        check_change(num-values[0],values[1:],mem)
    else:
        check_change(num-values[0],values[1:],mem)

print(check_change(220,values,mem))
