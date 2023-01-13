# Дан список чисел. Создайте список,  в который попадают числа,описываемые возрастающую последовательность
#[1,5,2,3,4,61,7] -> [1,5,6,7]
#lst = [1,5,2,3,4,6,7] 
# lst_ =list( map(int,lst))
# i=0
# while lst_[i] < lst_[i + 1]:
#     my_lst = [lst_[i] for lst_[i] in lst_ if lst_[i] < (lst_[i + 1])]
#     i +=1
#     print(my_lst)    №не работает[1, 2, 3, 4]

# i = 1
# while i < len(lst):
#     if lst[i-1] < lst[i]:
#         i += 1
#     else: lst.remove(lst[i])
# print(lst) # [1, 5, 6, 7]

lst = [1,5,2,3,4,6,7] 
new_lst = [lst[0]]
for i in range (1, len(lst)):
    if lst[i] > new_lst[-1]:# обращаемся к поседнему элементу создаваемого листа
        new_lst.append(lst[i])
print(new_lst)        #[1, 5, 6, 7]
 
