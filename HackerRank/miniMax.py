def miniMaxSum(arr):
    sorted_list = sorted(arr)  # O(NlogN) - merge sort
    min_list = sorted_list[:-1]  # T: O(N)  S: O(N-1) because taking one value
    max_list = sorted_list[1:]  # T: O(N)  S: O(N-1) because taking one value
    min_sum = 0
    max_sum = 0

    for i in min_list:  # O(N)
        min_sum = min_sum + i

    for i in max_list:  # O(N)
        max_sum = max_sum + i

    print(min_sum, max_sum)


# Example
miniMaxSum([7, 69, 2, 221, 8974])


'''
Time: NlogN + 4N + 3 == O(NlogN)
Space: O(3n) -- O(N) in the end
'''