#4. 给定一个范围为 32 位 int 的整数，将其颠倒。
class Solution:
    def reverse(self, x):
        xx=x
        flag=0
        if x<0:
            flag=1
        if flag==1:
            xx=abs(x)
        str0=str(xx)
        str1=str0[::-1]
        if flag==1: #处理负数
            s="-"
            s=s+str1
            if int(s)<=(-2147483648):
                return 0
            return int(s)
        else:
            if int(str1)>=2147483647:
                return 0
            else:
                return int(str1)


if __name__ == '__main__':
    s=Solution()
    print(s.reverse(1534236469))

