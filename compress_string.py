def compress(s):
    cur = s[0]
    counter = 1
    ret = ""

    if not s:
        raise ValueError("Empty sting or no argument.")

    else:
        for i in range(1,len(s)):
            if s[i] == cur:
                counter += 1
            else:
                ret += cur + str(counter)
                counter = 1
                cur = s[i]
        ret += cur + str(counter)
    return ret


print(compress('AAAAbbC222aaa'))
