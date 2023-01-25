# Question = Given two strings A and B. Find the characters that are not common in the two strings.Complete the function UncommonChars() which takes strings A and B as input parameters and returns a string that contains all the uncommon characters in sorted order. If no such character exists return "-1".

def UncommonChars(A, B):
    # code here
    unCommonCharsList = []
    A = set(A)
    for i in A:
        if i not in B:
            unCommonCharsList.append(i)

    B = set(B)
    for i in B:
        if i not in A:
            unCommonCharsList.append(i)

    unCommonCharsList.sort()

    finalresult = ''.join(unCommonCharsList)

    if len(finalresult) == 0:
        return -1
    return finalresult


A = "geeksforgeeks"
B = "geeksquiz"

result = UncommonChars(A,B)
print(result)

