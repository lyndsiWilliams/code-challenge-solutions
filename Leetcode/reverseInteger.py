def reverseInteger(x):
    '''  [::-1]
    This slice statement will start at the
    end of the string and end at position 0,
    moving with the step -1'''

    num_str = str(x)
    answer = 0

    if x == 0:
        answer = 0
    elif num_str[0] == "-":
        # Remove - from end of reversed string, add to front
        answer = int("-" + num_str[:0:-1])
    else:
        # Normal reversal
        answer = int(num_str[::-1])
        
    if answer not in range(-2**31, 2**31):
        print(0)
    else:            
        print(answer)

reverseInteger(120)