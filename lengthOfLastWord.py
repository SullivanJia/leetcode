# 给定一个字符串， 包含大小写字母、空格 ' '，请返回其最后一个单词的长度。

# 如果不存在最后一个单词，请返回 0 。
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.strip().split(' ')
        # print(words)
        return len(words[len(words)-1])


if __name__ == '__main__':
    s=Solution()
    print(s.lengthOfLastWord("a "))