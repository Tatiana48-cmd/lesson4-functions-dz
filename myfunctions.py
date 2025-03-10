"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def simple_separator():
    stars = '**********'
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    return  stars

print(simple_separator())
print(simple_separator() == '**********')  # True


def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """


    str_separator = "*" * count
    print(str_separator)
    return str_separator

print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    new_symbol = simbol
    str_separator = new_symbol * count
    #print( str_separator)
    return str_separator
print(separator('-', 10))
print(separator('#', 5))
print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    res = print(separator('*', 10), '\nHello World!\n', separator('#', 10), sep='\n')
    return res
print(hello_world())
'''
**********

Hello World!

##########
'''
hello_world()


def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    res = print(separator('*', 10), f'\nHello {who}!\n', separator('#', 10), sep='\n')
    return res
print(hello_who())
print(hello_who('Max'))
print(hello_who('Kate'))

'''
**********

Hello World!

##########
'''
hello_who()
'''
**********

Hello Max!

##########
'''
hello_who('Max')
'''
**********

Hello Kate!

##########
'''
hello_who('Kate')


def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    result = 0
    for number in args:
        result += number
        full_result = result ** power
    return full_result

print(pow_many(1, 1, 2))
print(pow_many(1, 2, 3))
print(pow_many(2, 1, 1))
print(pow_many(3, 2))
print(pow_many(2, 1, 2, 3, 4))


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for k, v in kwargs.items():
        result = f'{k} "-->" {v}'
        print(result)
print_key_val(name='Max', age=21)

print_key_val(animal='Cat', is_animal=True)



"""
name --> Max
age --> 21
"""
# print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
# print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """

    new_iterable = []
    for number in iterable:
        if function(number):  # Вызываем переданную функцию
            new_iterable.append(number)
    return new_iterable  # Возвращаем список после цикла

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2))  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3))  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba'))


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
