def birthdayCakeCandles(candles):
    count = {}

    for i in candles:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for i in count:
        if i == max(candles):
            print(count[i])

# Example
birthdayCakeCandles([4, 4, 1, 3])