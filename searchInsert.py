# 给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。
class Solution:
    def searchInsert(self, a, target):
        low=0
        high=len(a)-1
        while low<=high:
            mid=int((low+high)/2)
            if a[mid]==target:
                return mid
            elif target>a[mid]:
                low=mid+1
            elif target<a[mid]:
                high=mid-1


        if target<a[0]:
            return 0
        else:
            return high+1

if __name__ == '__main__':
    s=Solution()
    re=s.searchInsert([1,2,3,4,5,7],6)
    print(re)