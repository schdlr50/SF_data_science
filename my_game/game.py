"""Итоговое задание"""

import numpy as np

def random_predict(number:int=1) ->int:
    number = np.random.randint(1, 101) # загадываем число
    count = 0 # ставим счетчик на ноль
    minimum = 0 # добавил нижнюю границу, которыю в последствии буду двигать для минимизации поиска загаданного числа
    maximum = 101 # добавил верхнюю границу, которыю в последствии буду двигать для минимизации поиска загаданного числа
    predict_number = np.random.randint(1, 101) # предполагаемое число

    while True: # создаем цикл
        count +=1 # увеличиваем количество попыток
        if predict_number > number: # условие, если сгенерированное число больше загаданного
            minimum =+1
            predict_number = (minimum+predict_number)/2
            
        if number == predict_number: # условие, если угадали
            break 
        return(count)
print(f'Количество попыток: {random_predict()}')