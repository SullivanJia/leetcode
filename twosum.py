# leetcode : 题目1 两个数的和 two sum
import datetime
class Solution:
    def twoSum(self, nums, target):
        # for i in  range(0,len(nums)):
        #     j=i+1
        #     k=len(nums)-1
        #     while j<k:
        #         if nums[i]+nums[j] ==target :
        #             a=[i,j]
        #             return a
        #         if nums[i]+nums[k]==target:
        #             b=[i,k]
        #             return b
        #         j += 1
        #         k -= 1
        #     if j==k:
        #         if nums[i]+nums[j] ==target :
        #             c=[i,j]
        #             return c
        #   注释部分代码效率较低
        for i in  range(len(nums)):
            num=target-nums[i]
            j=i+1
            for j in range(j,len(nums)):
                if nums[j]==num:
                    a=[i,j]
                    return a

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    b=[-3,4,3,90]
    s=Solution()
    so=s.twoSum(b,0)
    print(so)
    endtime = datetime.datetime.now()
    print((endtime - starttime))