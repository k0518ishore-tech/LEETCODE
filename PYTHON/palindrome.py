class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
             res = False
        else:
            rem = 0
            rev = 0
            t=x
            while(t > 0):
                rem = t % 10
                rev = rev*10+rem 
                t=t//10
            if rev==x:
                res = True
            else:
                res = False
        return res
