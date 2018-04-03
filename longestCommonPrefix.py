# 编写一个函数来查找字符串数组中最长的公共前缀字符串。
class Solution:
    def longestCommonPrefix(self, a):
        i=1
        j=0
        key=1
        k=0 #最短字符串的位置
        m=1
        if a ==[]:
            return ""
        else:
            for l in range(len(a)):
                if a[l]=="":
                    return ""
            if len(a)==1:
                return a[0]

            for m in range(len(a)):
                if a[m][0]!=a[m-1][0] and len(a[m])==1 and len(a[m-1])==1:
                    # print("haha")
                    return ""


            while key<len(a):
                if len(a[key])>k:
                    k=key
                key+=1
                print(k)

            for j in range(len(a[k])):

                while i < len(a):
                    # print(i,j)
                    if a[i][j] == a[i - 1][j]:
                        i += 1
                    else:
                        break

            if j==0:
                return a[k][0]
            else:
                return a[k][:j]

if __name__ == '__main__':
    a=["aa","aaa"]
    s=Solution()
    print(s.longestCommonPrefix(a))
