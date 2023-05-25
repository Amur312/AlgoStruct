def is_palindrome(num):
    if num < 0:
        return False

    reversed_num = 0
    original_num = num
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return original_num == reversed_num
# Алгоритм
# Создайте функцию с именем is_palindrome, которая принимает один аргумент num - целое число, для которого нужно определить, является ли оно палиндромом.

# Проверьте, если num меньше нуля, то верните False, так как отрицательные числа не могут быть палиндромами.

# Инициализируйте переменные reversed_num и original_num со значением 0 и num соответственно. reversed_num будет использоваться для хранения обратного числа, а original_num - для сохранения исходного числа.

# Начните цикл, который будет выполняться до тех пор, пока num больше 0.

# В каждой итерации цикла вычислите остаток от деления num на 10 и сохраните его в переменную digit. Это даст вам последнюю цифру числа num.

# Обновите значение reversed_num, умножив его на 10 и добавив к нему значение digit. Это создаст обратное число.

# Разделите num на 10 с использованием оператора целочисленного деления //, чтобы удалить последнюю цифру из num.

# Повторяйте шаги 5-7 до тех пор, пока num не станет равным 0. Каждая итерация цикла добавит новую цифру к reversed_num, основываясь на младших разрядах исходного числа.

# После выхода из цикла сравните original_num с reversed_num. Если они равны, то исходное число является палиндромом, поэтому верните True. В противном случае, если они не равны, верните False.
