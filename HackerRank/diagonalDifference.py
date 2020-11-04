def diagonalDifference(arr):
    # Write your code here
    primary_sum = 0
    secondary_sum = 0
    length = len(arr[0])
    
    # primary_sum formula takes the values diagonally from topLeft to bottomRight
        # [0][0], [1][1], [2][2]
    # secondary_sum formula takes the values diagonally from bottomRight to topLeft
        # [0][2], [1][1], [2][0]
    for i in range(length):
        primary_sum = primary_sum + arr[i][i]
        secondary_sum = secondary_sum + arr[i][length-i-1]

    return abs(primary_sum - secondary_sum)

# Example
diagonalDifference([3, 11, 2, 4, 4, 5, 6, 10, 8, -12])