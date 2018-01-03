# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:24:22 2017

@author: caibo
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        positive = (dividend < 0) is (divisor < 0)
        #判断正负
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                #  << =  1  相当于乘以 2
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

a=Solution()
dividend,divisor= 65,-8
result=a.divide(dividend,divisor)
print (result)
