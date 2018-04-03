# 各位相加
class Solution:
    def addDigits(self, num):
        if num<10 :
            return num
        if num>=10:
            rs=num
            he=0
            while rs !=0:
                he =he + (rs%10)
                rs=rs//10
            return self.addDigits(he)



# 对9取余数也可以



if __name__ == '__main__':
    s=Solution()
    print(s.addDigits(10))