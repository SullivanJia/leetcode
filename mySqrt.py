# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根。
import math
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # for i in range(x):
        #     if i*i==x:
        #         return i
        #     elif i*i<x and i*i>(x-1):
        #         return i
        return int(math.sqrt(x))


if __name__ == '__main__':
    s=Solution()
    print(s.mySqrt(8))