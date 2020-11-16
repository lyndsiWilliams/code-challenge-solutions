def staircase(n):
    for i in range(n):  # O(N)
        print(('#' * (i+1)).rjust(n))  # +1 removes 0    ---look into printf---

# Example
staircase(6)


'''
Time: O(N)
Space: O(1)
'''