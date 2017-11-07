# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:43:06 2017

@author: caibo
"""

class Solution(object):
    def strStr(self,haystack,needle):
        """
        self.haystack=haystack
        self.needle=needle
        hlen=len(haystack)
        nlen=len(needle)
        if hlen < nlen:
            return -1
        elif needle not in haystack:
            return -1
        else:
            j=0
            for i in range(hlen):
                if haystack[i]==needle[j]:
                    if haystack[i:i+nlen]==needle:
                        return i
            return -1
            
"""
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
a=Solution()
haystack='caibocaitao'
needle='caitao'
result=a.strStr(haystack,needle)
print (result)
             
"""
优化代码：其实并不需要遍历所有，只要首字母就可以了
for i in range(len(haystack) - len(needle)+1):
    if haystack[i:i+len(needle)] == needle:
        return i
return -1
"""                