# 给定一个数组和一个值，在这个数组中原地移除指定值和返回移除后新的数组长度。
# 不要为其他数组分配额外空间，你必须使用 O(1) 的额外内存原地修改这个输入数组。
# 元素的顺序可以改变。超过返回的新的数组长度以外的数据无论是什么都没关系。
class Solution:
    def removeElement(self, nums, val):
        # nums.sort()
        i=0
        while i<len(nums):
            if nums[i]==val:
                del nums[i]
            else:
                i+=1

        return len(nums)


if __name__ == '__main__':
    s=Solution()
    print(s.removeElement([3,3],3))
