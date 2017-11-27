# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:53:47 2017

@author: caibo
两者求和直接遍历
三者求和设置一次遍历，然后设置i，j向内判断
下面的例子中target=0
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res
             

"""

class solution:
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
#通过递归来实现
#在递归中设置两个求和，迭代的终止条件是2者求和。    
        results = []
        findNsum(sorted(nums), target, 3, [], results)
        return results

    def combinationSum(self, candidates, target):
        """
        提升一下，可以重复使用candidate中的元素来构成target
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        lres=[]
        for i in res:
            if i not in lres:
                lres.append(i)
        return lres
    #输入有重复的元素但是，解中不能有重复的解
    #直接return res则是返回所有的解，可能有重复
    #另外一种解法：
    def combinationSum2(self, candidates, target):
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
        return list(map(list, table[target]))
    #python3 中map等高阶函数需要使用list返回结果，
    #因为这些函数作用的结果都是返回一个list
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)
#如果将self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
#改为self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)
#那么将不允许重复使用
#此外通过修改if target == 0 and  len(path)==2
#可以控制几个数相加，解决了N-sum问题从另外一个角度
a= solution()
nums=[10,1,2,7,6,1,5]
target=8
res=a.fourSum(nums,target)
res1=a.combinationSum2(nums,target)
print (res1)