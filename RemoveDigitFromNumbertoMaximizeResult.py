class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        indexOfdigit=[]
        for i in range(len(number)):
            if number[i]==digit:
                indexOfdigit.append(i)
        listOfNumbersRemovingADigit=[]

        for i in indexOfdigit:
            s=''
            for j in range(len(number)):
                if j!=i:
                    s+=number[j]
                if s!='':
                    listOfNumbersRemovingADigit.append(int(s))
        print(indexOfdigit,listOfNumbersRemovingADigit)
        # return max(listOfNumbersRemovingADigit)

print(Solution().removeDigit('1','1'))