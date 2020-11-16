def compareTriplets(a, b):
    alice_count = 0
    bob_count = 0

    for i in range(3):  # always going to be looping 3x
        if a[i] > b[i]:
            alice_count = alice_count + 1
        elif a[i] < b[i]:
            bob_count = bob_count + 1
        
    return (alice_count, bob_count)

# Example
compareTriplets([5, 6, 7], [3, 6, 10])


'''
Time: O(1) inputs are constant and nothing is changing them
Space: O(1)
'''