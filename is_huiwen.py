class Solution:
    def isPalindrome(self, x):
        flag=True
        for i in range(len(str(x))):
            if str(x)[i]==str(x)[len(str(x))-1-i] and i<len(str(x)):
                i+=1
                flag=True
            else:
                flag=False
                break
        return flag
if __name__ == '__main__':
    s=Solution()
    print(s.isPalindrome(12213))


