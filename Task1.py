# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Я люблю Джавуабв абви Питон ->
# Я люблю Питон
text = 'Я люблю Джавуабв абви Питон'

# my_str = [elem for elem in a.split('абв')  if elem != 'абв']
# print(my_str) #['Я люблю Джаву', ' ', 'и Питон']


#str = text.split()
# my_list = []
# for i in str:
#         if 'абв' not in i:
#             my_list.append(i)
# print(my_list)     #['Я', 'люблю', 'Питон']       

## ИЛИ ВКЛЮЧЕНИЕМ

# my_list = [word for word in text.split() if 'абв' not in word]
# print(my_list)  #['Я', 'люблю', 'Питон']
# print(*my_list)  # Я люблю Питон (можно через join)

my_list = list(filter(lambda word:"абв" not in word, text.split()))
print(*my_list) #Я люблю Питон



