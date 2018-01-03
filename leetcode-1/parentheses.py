# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:36:32 2017

@author: caibo
"""

class Solution():
    def longestValidParentheses(self, s):
        def isValid(s, i, j):
            s= s[i:j+1]
            stack = []
            for char in s:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if stack == []:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            return stack == []
        max = 0
        for i in range(len(s)):
            for j in range(i+1,len(s),2):
                if isValid(s,i,j):
                    re=j-i+1
                    if re>=max:
                        max=re
        return max
        
        #以上是暴力解决 
        #下面采用动态规划来处理
    def longestValidParentheses1(self, s):   
        maxre = 0
        stack = []
        for i in range(len(s)):
            stack.append(0)
        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    stack[i]= 2 + (stack[i-2] if i>=2 else 0)
                elif i-stack[i-1]>0 and s[i-stack[i-1]-1] =='(':
                    stack[i]=2+stack[i-1]+(stack[i-stack[i-1]-2] if i-stack[i-1]>=2 else 0)
            maxre = max(maxre,stack[i])
        return maxre 
    #采用栈来处理
    def longestValidParentheses2(self, s):
        def empty(st):
            return len(st)==0
        def peek(st):
            st.reverse()
            re=st[0]
            st.reverse()
            return re
        maxre = 0
        stack=[]
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if empty(stack):
                    stack.append(i)
                else:
                    maxre = max(maxre,i-peek(stack))
        return maxre
a=Solution()
s='())((())))'
print(a.longestValidParentheses1(s))
                
                
        