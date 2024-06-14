#!/usr/bin/python3
""" This  calculates the fewest number of operations needed to result
in exactly n H characters in the file"""


def minOperations(n):
    """This computes the fewest number of operations needed to result in exactly
    n H characters
    """
    if n <= 1:
        return 0
    
    # Initialize an array to store the minimum number of operations
    dp = [0] * (n + 1)
    
    # Iterate from 2 to n
    for i in range(2, n + 1):
        dp[i] = float('inf')  # Initialize with infinity or a large number
        
        # Find the best way to achieve i 'H' characters
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n]



