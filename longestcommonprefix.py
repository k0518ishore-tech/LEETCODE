class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        res = ""
        i=0
        length = len(strs)
        while i<len(strs[0]):
            if strs[0][i]==strs [length-1][i]:
                res+=strs[0][i]
            else:
                break
            i+=1
        return res
