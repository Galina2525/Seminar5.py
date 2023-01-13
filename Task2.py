# В файле находятся N натуральных чисел,  записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие А[i] - 1 = A[i-1].
# Найдите это число.
# 5 6 7 9 -> 8

# import pathlib
# from pathlib import Path  
# path = Path('Seminar5','numbers.txt')
path = r'numbers.txt' # путь к файлу - в переменную
with open(path,'r') as data:
    data_list = list(map(int, data.read().split()))
    print(data_list) # [5, 6, 7, 9, 11, 13]
    # for elem in range(data_list[0],data_list[-1]):
    #     if elem not in data_list:
    #         print(elem, end=' ') # 8 10 12 

my_list = []
for i in range(0,len(data_list)-1):
    if data_list[i] + 1 != data_list[i +1]:
        my_list.append(data_list[i]+1)
print(my_list)   #  8 10 12    







