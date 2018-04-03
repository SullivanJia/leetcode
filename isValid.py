# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 括号必须以正确的顺序关闭，"()" 和 "()[]{}" 是有效的但是 "(]" 和 "([)]" 不是。
class Solution:


    def isValid(self, a):
        if len(a)%2==1:
            return False
        i=0
        b=list()
        # print(a)
        while i<len(a):
            if a[i]=='(' or a[i]=='{' or a[i]=='[':
                b.append(a[i])
            if b == []:
                return False
            print(b)
            if a[i]==')':
                # print(a[i])
                if '('==b[len(b)-1] and b !=[]:
                    b.pop()
                    # print("pop"+str(i))
                else:
                    return False
            if a[i]==']':
                if '['==b[len(b)-1] and b !=[]:
                    b.pop()
                else:
                    return False
            if a[i]=='}':
                if '{'==b[len(b)-1] and b !=[]:
                    b.pop()
                else:
                    return False
            i+=1


        if b==[]:
            return True
        else:
            return False




if __name__ == '__main__':
    s=Solution()
    print(s.isValid("[()](())"))




