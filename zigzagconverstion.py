class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mat = [[] for _ in range(numRows)]
        j = 0
        f = 0
        for i in s:
            mat[j].append(i)
            if f == 1:
                if j <= 0:
                    j += 1
                    f = 0
                else:
                    j -= 1
            else:
                if j >= (numRows-1):
                    j -= 1
                    f = 1
                else:
                    j += 1
        res = ""
        for i in mat:
            res += "".join(i)
        return res

        
