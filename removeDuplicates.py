class Solution:
    def removeDuplicates(self, nums):
        i=0
        while i<(len(nums)-1) :

            if nums[i+1]==nums[i]:
                del nums[i]
            else:
                i+=1
            # print(nums[i])
        return len(nums)





if __name__ == '__main__':
    s=Solution()
    print(s.removeDuplicates([1,1,1,2]))
