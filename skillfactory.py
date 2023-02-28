# ЗАДАНИЕ 12.7.3 (HW-03)
# Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом,
# что ключ — название банка, значение — процент. Напишите программу, в результате которой будет сформирован список
# deposit значений — накопленные средства за год вклада в каждом из банков. На вход программы с клавиатуры вводится
# сумма money, которую человек планирует положить под проценты.

# money = int(input('Введите сумму: '))
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# deposit = [int(money / 100 * per_cent.get('ТКБ')), int(money / 100 * per_cent.get('СКБ')),
#            int(money / 100 * per_cent.get('ВТБ')), int(money / 100 * per_cent.get('СБЕР'))]
# max_profit = max(deposit)
# print(deposit)
# print('Максимальная сумма, которую вы можете заработать —', max_profit)

# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")


# # ЗАДАНИЕ 13.8.19(HW - 03)
# # Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов.
# # Спрашиваем количество необходимых билетов
# tickets = int(input('Сколько билетов вы хотите приобрести?: '))
#
# # Возраст участников
# ages = []
# for i in range(0, tickets):
#     value_age = int(input(f'Возраст участника №{i + 1}: '))
#     ages.append(value_age)
#
#
# # Считаем стоимость билетов, согласно цене в прайсе по возрастным категориям
# def price(ages):
#     if ages < 18:
#         return 0
#     elif 18 <= ages < 25:
#         return 990
#     else:
#         return 1390
#
#
# total_price = int(sum(map(price, ages)))
#
# # Если билетов более 3шт., делаем скидку 10%
# discount_price = total_price * 0.9
# if tickets > 3:
#     print('Стоимость билетов со скидкой: ', discount_price, 'руб.')
# else:
#     print('Стоимость билетов: ', total_price, 'руб.')

# with open(r'C:\Users\User\Desktop\track.txt')as myfile:
#     for line in myfile:
#         print(line)

# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
# Преобразование введённой последовательности в список
# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.

array = [int(x) for x in input("Введите через пробел числа в любом порядке от 1 до 999 : ").split()]

def merge_sort(array):  # разделение введённых чисел
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right): # слияние
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(array))


def binary_search(array, element, left, right):
    if left > right:  # если левая граница больше правой,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # поиск середины
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


while True:
    try:
        element = int(input("Введите число от 1 до 999: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")


print(binary_search(array, element, 0,  len(array)))