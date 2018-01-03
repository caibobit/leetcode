# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:42:12 2017

@author: caibo
"""

class Solution(object):
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        # t为所有words中字符串的总长度
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                    # 如果出现 barfoobar时 (words=[foo,bar])
                         #   l        r
                    # 那么就要    l    r 将l 前移一个k(word基本长度)
                if r - l == t:
                    ans.append(l)
    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        # 就是将 words 里面的内容进行统计
        ans = []
        for i in range(min(k, n - t + 1)):  
            # k为最小长度，必须要从最小长度的进行计算
            # n-t+1 为最大长度考虑最差情况
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans
a=Solution()
s='barfoobarthefoobarmanthefoobar'
words=['foo','bar']
result=a.findSubstring(s,words)
print (result)