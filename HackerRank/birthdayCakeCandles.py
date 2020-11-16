def birthdayCakeCandles(candles):
    count = {}

    for i in candles:  # O(N)
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for i in count:  # O(N) - worst
        if i == max(candles):
            print(count[i])

# Example
birthdayCakeCandles([4, 4, 1, 3])


'''
Time: O(N+1) to O(2N) - O(N) in the end
Space: O(1) (if they were all dupes or empty case) to O(N) - O(N) in the end
'''