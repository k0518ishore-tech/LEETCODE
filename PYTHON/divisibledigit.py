//Smallest Divisible Digit Product I

class Solution(object):
    def mul(self,h):
        m=1
        k=h
        rem = 0
        while(k > 0):
           rem = k%10
           m*=rem
           k=k//10
        return m

    def smallestNumber(self, n, t):
        while True:
            if self.mul(n)%t==0:
                    break
            else:
                n+=1
        return n
        
