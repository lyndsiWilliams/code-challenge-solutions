def diagonalDifference(arr):
    # Write your code here
    primary_sum = 0
    secondary_sum = 0
    length = len(arr[0])
    
    # primary_sum formula takes the values diagonally from topLeft to bottomRight
        # [0][0], [1][1], [2][2]
    # secondary_sum formula takes the values diagonally from bottomRight to topLeft
        # [0][2], [1][1], [2][0]
    for i in range(length):  # O(2log N) - only considering a fraction of the numbers
        primary_sum = primary_sum + arr[i][i]
        secondary_sum = secondary_sum + arr[i][length-i-1]

    return abs(primary_sum - secondary_sum)  # T = O(2): Subtract is O(1), abs is O(1)

# Example
diagonalDifference([3, 11, 2, 4, 4, 5, 6, 10, 8, -12])


'''
Time: O(log N)
Space: O(1)  (O(3))
'''