# 给定一个非负整数组成的非空数组，给整数加一。
# 可假设整数不包含任何前导零，除了数字0本身。
# 最高位数字存放在列表的首位。
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=""
        for i in digits:
            num+=str(i)
        nums=int(num)+1
        return list(map(int,str(nums)))


if __name__ == '__main__':
    s=Solution()
    print(s.plusOne([0]))
