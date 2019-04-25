# -*- coding: utf-8 -*-
# @Author: Chen Zhiquan
# @Date:   2019-04-25 19:39:58
# @Last Modified by:   octavian
# @Last Modified time: 2019-04-25 19:57:56
def lps_1(s):
    '''longest palindromic substring'''
    n = len(s)

    if n == 0:
        return 0

    # dp[i][j] the length of from position i to position j, length=j-i+1
    dp = [[1 for _ in range(n)] for _ in range(n)]

    start=0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                if j == i+1:
                    dp[i][j] = 2
                    start = i
                elif dp[i+1][j-1] != j-i-1:
                    dp[i][j] = dp[i+1][j-1]
                    start = i+1
                else:
                    dp[i][j] = j - i + 1
                    start = i

            else:
                dp[i][j] = dp[i+1][j-1]
                start = i + 1

    return dp[0][n-1], s[start:start+dp[0][n-1]]

def lps_2(s):
    s_rev = s[::-1]
    
