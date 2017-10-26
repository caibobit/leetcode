# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:00:08 2017

@author: caibo
"""
class Sum():
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]],i]
            d[nums[i]]=i
#计算两个值得sum，使用一个dictionary来进行记录，没有就放进去
#有就返回               
nums=[-1,1,0,2,2,1,3]
target= 0
if  __name__ =='__main__':
    sum=Sum()
    res=sum.twoSum(nums,target)
    print (res)