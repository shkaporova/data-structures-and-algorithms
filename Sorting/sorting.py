def swap(a, b):
    return b, a

def bubble_sort(array):
    # Здесь алгоритм сортировки массива
    for i in range(len(array)):
        for j in range(len(array)-1, i + 1, -1):
            # print(i, j)
            if array[j] < array[j-1]:
                # a = array[j]
                # array[j] = array[j-1]
                # array[j-1] = a
                array[j], array[j-1] = swap(array[j], array[j-1])
    return

# Функция сортровки вставками

# Функция сортировки выбором
