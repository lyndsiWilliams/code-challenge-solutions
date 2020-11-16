def aVeryBigSum(ar):
    sum = 0
    
    for i in ar:
        sum = sum + i

    return sum

# Example
aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])


'''
Time: O(N)
Space: 0(1)
'''