def insertion_sort(arr):
    # Проходим по всем элементам начиная со второго (индекс 1)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Перемещаем элементы arr[0..i-1], которые больше, чем key, на одну позицию вперед 
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f'Шаг {i}: {arr}')  # вывод текущего состояния массива

arr = [8, 3, 5, 4, 6]
insertion_sort(arr)
print(f'Отсортированный массив: {arr}')

# Теперь разберем каждый шаг:

# Мы начинаем с первого элемента (8), предполагая, что он отсортирован.

# Далее берем следующий элемент - 3. Сравниваем его с 8. Так как 3 меньше 8, мы сдвигаем 8 вправо и вставляем 3 перед ним. Получаем [3, 8, 5, 4, 6].

# Следующий элемент - 5. Он меньше 8, но больше 3, поэтому мы вставляем его между 3 и 8. Получаем [3, 5, 8, 4, 6].

# Следующий элемент - 4. Он меньше 8 и 5, но больше 3, поэтому вставляем его между 3 и 5. Получаем [3, 4, 5, 8, 6].

# Последний элемент - 6. Он меньше 8, но больше 5, поэтому вставляем его между 5 и 8. Получаем [3, 4, 5, 6, 8].

# Итак, мы получили отсортированный массив [3, 4, 5, 6, 8].
