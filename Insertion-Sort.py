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
