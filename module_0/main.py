import numpy as np
def my_programm(number):
    count = 0
    left = 1
    right = 100
    predict = (right + left) // 2
    while number != predict:
        count+=1
        if number > predict: 
            left = predict + 1
        elif number < predict: 
            right = predict - 1
        predict = (right + left) // 2
    return(count)
