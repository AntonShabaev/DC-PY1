# Дан целочисленный список, состоящий из 10 элементов. Поменять местами первый максимальный и последний элементы.

list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index = 0
for i in range(len(list_numbers)):  # ищем номер максимального элемента
    max_number = list_numbers[max_index]
    if max_number < list_numbers[i]:
        max_index = i
list_numbers[max_index], list_numbers[len(list_numbers) - 1] = list_numbers[len(list_numbers) - 1], \
                                                               list_numbers[max_index]  # множественное присваивание
print(list_numbers)
