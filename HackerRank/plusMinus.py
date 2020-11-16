def plusMinus(arr):
    pos_count = 0
    zero_count = 0
    neg_count = 0
    denominator = len(arr)

    for i in arr:  # O(N)
        if i > 0:
            pos_count += 1
        elif i == 0:
            zero_count += 1
        else:
            neg_count += 1
    
    answer = [format(pos_count/denominator, '.6f'), format(neg_count/denominator, '.6f'), format(zero_count/denominator, '.6f')]  # O(6)
    
    for i in answer:  # O(1) - always 3 answers
        print(i)

# Example
plusMinus([-4, 3, -9, 0, 4, 1])


'''
Time: O(N)
Space: O(1)
'''