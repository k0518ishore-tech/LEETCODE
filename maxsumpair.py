// Max Sum of a Pair With Equal Sum of Digits
class Solution(object):
    def maximumSum(self, nums):
        def sumso(n):
            t=n
            sum=0
            while t!=0:
                r=t%10
                sum+=r
                t=t//10
            return sum
        c=-1
        l={}
        for i in nums:
            digit_sum= sumso(i)
            if digit_sum in l:
                pair_sum = i+l[digit_sum]
                c=max(c,pair_sum)
                l[digit_sum]=max(l[digit_sum],i)
            else:
                l[digit_sum]=i
        return c
