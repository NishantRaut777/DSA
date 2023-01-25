    
class parenthesisChecker:    
    def getReverse(self, bracket):

        if bracket == "}":

            return "{"

        if bracket == ")":

            return "("

        if bracket == "]":

            return "["

        return ""

    def ispar(self,exp):

        # code here

        a=[]

        for x in exp:

            if x in ('{','[','('):

                a.append(x)

                continue

            if x not in ('}',']',')'):

                continue

            if (len(a)<=0):

                return False

            rev=self.getReverse(x)

            fromstack=a.pop()

            #print(fromstack,rev)

            if fromstack!=rev:

                return False

        

        if len(a)!=0:

            return False

        return True

p = parenthesisChecker()
mystr = "{([])}"
result = p.ispar(mystr)
print(result)


# steps:
# 1. In "ispar" method first create empty list "a". Traverse in list check for values like "'{','[','('" If found append them in list and continue.
# 2. If character not in "'}',']',')'" then continue. 
# 3. If length of list is less than or equal to 0 then return False.
# 4. Find the rev of x by calling "getReverse" method in which we are finding reverse of "'}',']',')'" characters.
# 5. pop the element from list for comparison with "rev"
# 6. If both are not equal then return False.
# 7. Ouside the loop check length of list . If it is not equal to zero then return False else return True .