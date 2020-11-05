def subsets(nums):
    length = len(nums)
    solution = []

    '''
    Recursive function
    - If current iteration != length,
    run function again with next number in list
    - If it does, append current subset to solution list
    '''
    def recurse(i, subset):
        if i == length:
            solution.append(subset)
        else:
            recurse(i+1, subset)
            recurse(i+1, subset + [nums[i]])
        
    # First recursion run starts at index 0 and
    # passes through a blank list as the first subset
    recurse(0, [])
    return solution
    

subsets([1, 2, 3])