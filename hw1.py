import re
from random import randint
# 1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
# keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ожидаемый результат: {1: 1, 2: 4, 3: 9 …}


def dict_generator(keys_list):
    result = {i: i for i in keys_list}
    return result


keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(dict_generator(keys))


# 2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.

def list_generator():
    result = [i for i in range(0, 100) if i % 2 == 0]
    return result


print(list_generator())

# 3) Заменить в произвольной строке согласные буквы на гласные.


def replace_consonants(input_str):
    result = ""
    vowels = ["a", "e", "i", "o", "u"]
    input_str.lower()
    for i in input_str:
        if re.match("[a-z]", i) and i not in vowels: # to be sure that curr char is a letter
            result = "".join([result, vowels[randint(0, len(vowels) - 1)]])
        else:
            result = "".join([result, i])
    return result


print(replace_consonants("hello"))

# 4) Дан массив чисел.
# [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
#
# 4.1) убрать из него повторяющиеся элементы

list2 = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]


def remove_duplicate(input_list):
    return list(set(input_list))


print(remove_duplicate(list2))

# 4.2) вывести 3 наибольших числа из исходного массива


def get_three_max(input_list):
    return sorted(input_list)[-3:]


print(get_three_max(list2)) # в результате потенциально получим дублирующиеся числа, т.к. из условия не совсем ясно,
                            # нужна нам уникальность или нет


# 4.3) вывести индекс минимального элемента массива

def get_min_index(input_list):
    return input_list.index(min(input_list))


print(get_min_index(list2))

# 4.4) вывести исходный массив в обратном порядке


def list_reverse(input_list):
    rev_list = input_list
    rev_list.reverse()
    return rev_list


print(list2)
print(list_reverse(list2))

# 5) Найти общие ключи в двух словарях:
# dict_one = { ‘a’: 1,
#                     ‘b’: 2,
#                     ‘c’: 3,
#                     ‘d’: 4 }
#
# dict_two = { ‘a’: 6,
#                     ‘b’: 7,
#                     ‘z’: 20,
#                     ‘x’: 40 }
#

dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}


def get_dicts_keys_intersection(dict1, dict2):
    return set(dict_one.keys()).intersection(set(dict_two.keys()))


print(get_dicts_keys_intersection(dict_one, dict_two))


# 6) Дан массив из словарей
data = [{'name': 'Viktor', 'city': 'Kiev', 'age': 30},
             {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
             {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
             {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
             {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
             {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]


# 6.1) отсортировать массив из словарей по значению ключа ‘age'

def sort_by_age(input_list):
    return sorted(input_list, key=lambda kv: kv["age"])


print(sort_by_age(data))


# 6.2) сгруппировать данные по значению ключа 'city'
#        вывод должен быть такого вида :
#        {
#           ‘Kiev’: [ {‘name’: ‘Viktor’, ‘age’: 30 },
#                        {‘name’: ‘Andrey’, ‘age’: 34}],
#           ‘Dnepr’: [ {‘name’: ‘Maksim’, ‘age’: 20 },
#                           {‘name’: ‘Artem’, ‘age’: 50}],
#           ‘Lviv’: [ {‘name’: ‘Vladimir’, ‘age’: 32 },
#                        {‘name’: ‘Dmitriy’, ‘age’: 21}]
#        }
#

def group_by_city(input_list):
    cities = set()
    for i in input_list:
        cities.add(i.get("city"))
    result = dict()
    for i in cities:
        result[i] = list()
        for k in input_list:
            if k.get("city") == i:
                result[i].append({"name": k.get("name"), "age": k.get("age")})
    return result


print(group_by_city(data))
