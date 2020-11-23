# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Notes
sorted_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def binary_search(arr, target):
    
    mid_idx = None
    # [0, 1, 2] [0, 1] [0]
    left_idx = 0
    right_idx = len(arr)-1

    while True:
        # Reassign mid_idx every loop
        mid_idx = (left_idx + right_idx) // 2
        
        if arr[mid_idx] == target: return True
        # If != and there's only 1, target doesn't exist
        if left_idx == right_idx: return False

        if target > arr[mid_idx]: 
            if mid_idx == 0 and arr[1] != target: return False # crutch
            # cut corner if possible to locate taht list doesn't contain possibility of value
            if target < arr[mid_idx+1]: return False

            left_idx = mid_idx+1
            continue

        if target < arr[mid_idx]: 
            if mid_idx == 0: return False
            # cut corner if possible to locate taht list doesn't contain possibility of value
            # as long as there's more than 2 items
            if left_idx != mid_idx and target > arr[mid_idx-1]: return False
            # we need to go left
            if left_idx == mid_idx: return False

            right_idx = mid_idx-1

print(binary_search(sorted_list, 11))