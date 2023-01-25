def isBinary(str):
    # code here
    for i in str:
        if i != '0' and i != '1':
            return 0
    return 1

mystr = "0111100110101100"
result = isBinary(mystr)
print(result)