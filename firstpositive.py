class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        a=sorted(nums)
        for i in range(len(nums)):
            if a[i]>0:
                res=a[i:]
                break
        res.append(0)
        print(res)
        #各归原位置
        N=len(res)
        for i in range(1,N):
            target =res[i]
            while target < N and target != res[target]:
                tmp = res[target]
                res[target] = target
                target = tmp
        for i in range(1,N):
            if res[i] != i:
                return i
        return N
nums=[3,4,-1,1]
a=Solution()
print()
print(a.firstMissingPositive(nums))
