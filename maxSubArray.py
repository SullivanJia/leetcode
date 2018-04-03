# 给定一个序列（至少含有 1 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=-100000000000
        sum=0

        if len(nums)==0 :
            return 0
        i=0
        while i<len(nums):
            if sum<0:
                sum=nums[i]
            else:
                sum += nums[i]
            if sum>max:
                max=sum
            i+=1
        return max

if __name__ == '__main__':
    s=Solution()
    print(s.maxSubArray([-1]))

