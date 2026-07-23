"""338. Counting Bits"""

class Solution(object):
    def countBits(self, n):
        def dtb(n):
            if n==0:
                return '0'
            binary=''
            while n>0:            
                binary=str(n%2)+binary
                n=n//2
            return binary
        
        l=[]
        for i in range(0,n+1):
            sum=0
            nums=dtb(i)
            n3=len(nums)
            for j in range(n3):
                if nums[j]=='1':
                    sum+=1
                else:
                    sum+=0
            l.append(sum)
        return l
