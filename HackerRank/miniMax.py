def miniMaxSum(arr):
    sorted_list = sorted(arr)
    min_list = sorted_list[:-1]
    max_list = sorted_list[1:]
    min_sum = 0
    max_sum = 0
    
    for i in min_list:
        min_sum = min_sum + i

    for i in max_list:
        max_sum = max_sum + i

    print(min_sum, max_sum)


# Example
miniMaxSum([7, 69, 2, 221, 8974])