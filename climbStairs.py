# 你正在爬楼梯。需要 n 步你才能到达顶部。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方式可以爬到楼顶呢？
# 1,2,3,5,8,13,21
class Solution:
    def climbStairs(self, n):
        if n<=3:
            return n
        else:
            a=2
            b=3
            i=4
            while i<=n:
                a,b=b,a+b
                i+=1
            return b

if __name__ == '__main__':
    s=Solution()
    print(s.climbStairs(5))

