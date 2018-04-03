# 二进制求和
class Solution:
    def addBinary(self, a, b):
        num1=int(a,2)
        # print(type(num1))
        num2=int(b,2)
        s=num1+num2
        res=bin(s)
        # print()
        return res.replace('0b','')

if __name__ == '__main__':
    t=Solution()
    print(t.addBinary("11","1"))