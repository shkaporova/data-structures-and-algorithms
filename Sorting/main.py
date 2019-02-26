from sorting import bubble_sort

UNSORTED_ARRAY = [1, 4, 1, 5, 2, 10, 14, 7, 1, 3]

def main():
    # Делаем копию, иначе изначальный массив изменится,
    # и мы его не сможем использовать
    a = UNSORTED_ARRAY.copy()
    bubble_sort(a)
    print(a)

    # Копируем массив
    # Применяем функцию
    # print
    # X2


if __name__ == '__main__':
    main()
