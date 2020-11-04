def staircase(n):
    for i in range(n+1):
        if i == 0:
            continue
        else:
            print(('#' * i).rjust(n))

# Example
staircase(6)