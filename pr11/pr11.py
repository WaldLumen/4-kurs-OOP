def print_vector(arr):
    if not arr:
        print("Вектор порожній")
        return
    for item in arr:
        print(item, end=" ")
    print()

def main():
    SIZE = 10
    # Створюємо порожній список (аналог порожнього вектора)
    array = []

    # Заповнюємо (аналог push_back)
    for i in range(SIZE):
        array.append(i)

    print("Вихідний вектор")
    print_vector(array)

    # Видаляємо 5-й елемент (індекс 4, значення 4)
    # В Python: del або pop(index)
    if len(array) > 4:
        del array[4]
    print("Після видалення числа 4")
    print_vector(array)

    # Видаляємо діапазон [6, 9) за значеннями (в оригіналі це числа 6, 7, 8)
    # В Python використовуємо зрізи (slices)
    # Після видалення '4', числа 6, 7, 8 знаходяться на нових позиціях
    # Для точності логіки C++: array.begin()+5 відповідає 6-му елементу
    del array[5:8]
    print("Після видалення чисел 6, 7 й 8")
    print_vector(array)

    # Максимальний розмір (в Python обмежений лише пам'яттю)
    import sys
    print(f"Максимальний розмір (теоретичний) = {sys.maxsize}")

    # Розмір (size)
    print(f"Розмір вектора = {len(array)}")

    # Ємність (capacity)
    # Python керує пам'яттю автоматично, але можна подивитись розмір в байтах
    print(f"Об'єм пам'яті об'єкта в байтах = {sys.getsizeof(array)}")

    # Вставка в діапазон: чотири п'ятірки, починаючи з індексу 1
    # [1:1] означає вставку перед індексом 1 без видалення елементів
    array[1:1] = [5] * 4
    print("Після вставки чотирьох п'ятірок у діапазон [1,5)")
    print_vector(array)

    # Видаляємо останній елемент
    print("Після видалення останнього елемента")
    array.pop()
    print_vector(array)

    # Копіювання вмісту в новий список
    new_array = list(array)
    print("Вектор newArray")
    print_vector(new_array)

    # Заповнюємо newArray сімками (вставляємо на початок стільки сімок, скільки елементів)
    new_array[:0] = [7] * len(new_array)
    print("Після вставки сімок")
    print_vector(new_array)

    # Присвоєння (аналог assign) - повна заміна вмісту
    new_array = list(array)
    print("Після присвоєння вектора array")
    print_vector(new_array)

    # Очищення
    new_array.clear()
    print("Спроба вивести порожній вектор")
    print_vector(new_array)

    # Порівняння
    array.clear()
    for i in range(SIZE):
        array.append(i)
        new_array.append(i + 1)

    print("Вектор array:", end=" ")
    print_vector(array)
    print("Вектор newArray:", end=" ")
    print_vector(new_array)

    if array == new_array: print("array == newArray")
    if array > new_array:  print("array > new_array")
    if array >= new_array: print("array >= new_array")
    if array < new_array:  print("array < new_array")
    if array <= new_array: print("array <= new_array")

if __name__ == "__main__":
    main()