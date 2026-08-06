// problem no 76

class Solution(object):
    def minWindow(self, s, t):
        d={}
        l=0
        r=0
        minlen=float("inf")
        sidx=-1
        n=len(s)
        cnt=0

        for i in t:
            d[i]=d.get(i,0)+1

        while r<n:
            if s[r] in d:
                
                
                if d[s[r]]>0:
                    cnt+=1
                d[s[r]]-=1
            while cnt==len(t):
                if r-l+1<minlen:
                    minlen=r-l+1
                    sidx=l
                

                if s[l] in d:
                    d[s[l]]+=1
                    if d[s[l]]>0:
                        cnt-=1
                l+=1
            r+=1
        if sidx==-1:
            return ""
        return s[sidx:sidx+minlen]
                    
