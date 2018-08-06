import time

# Задача-1
#
# Написать свой lru_cache  декоратор с аргументом. В качестве аргумента он будет принимать maxsize-
# максимальный размер кеша.
#


def lru_cache_decorator(input_func):
    cache = {}

    def wrapper(arg, cache_max_size):
        print(cache)
        if arg in cache:
            return cache.get(arg).get("func_result")
        else:
            if len(cache) >= cache_max_size:
                oldest_key = 0
                oldest = {}
                for k in cache:
                    if oldest == {}:
                        oldest = cache.get(k)
                        oldest_key = k
                    if cache.get(k).get("timestamp") < oldest.get("timestamp"):
                        oldest = cache.get(k)
                        oldest_key = k
                cache.pop(oldest_key)
            cache[arg] = {"func_result": input_func(arg), "timestamp": time.time()}
            return cache.get(arg).get("func_result")

    return wrapper

@lru_cache_decorator
def func1(input_int):
    return "INPUT parameters: " + str(input_int)


print(func1(1, 2))
print(func1(2, 2))
print(func1(3, 2))
print(func1(4, 2))

# Задача-2
#
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.
#
# def my_func(a):
#         return a * 7

def result_checker_decorator(input_func):
    def wrapper(arg):
        rest = 100 % input_func(arg)
        if rest == 0:
            print("We are OK!")
        else:
            print("Bad news guys, we got " + str(rest))
        return input_func(arg)
    return wrapper


@result_checker_decorator
def func2(input_int):
    return input_int * 7


print(func2(10))

#
# Здача-4
#
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache.
# Если аргумента нет в переменной cache и функция выполняется, вывести сообщение «Function executed with counter = {},
# function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение
# «Used cache with counter = {}» и количество раз обращений в cache.
#
# Def my_func(a):
#         return 10*a
# my_func(1)
# my_func(5)
# my_func(10)
# my_func(1)
# my_func(2)
# my_func(1)
# my_func(20)
# my_func(5)

def cache_decorator(input_func):
    cache = {}
    exec_cnt = 0
    cache_cnt = 0
    def wrapper(arg):
        nonlocal exec_cnt
        nonlocal cache_cnt
        if arg in cache:
            cache_cnt = cache_cnt + 1
            print("Used cache with counter = {}".format(cache_cnt))
            return cache[arg]
        else:
            cache[arg] = input_func(arg)
            exec_cnt = exec_cnt + 1
            print("Function executed with counter = {}, function result = {}".format(exec_cnt, cache[arg]))
            return cache[arg]
    return wrapper

@cache_decorator
def func4(input_int):
    return input_int * 10

func4(1)
func4(5)
func4(10)
func4(1)
func4(2)
func4(1)
func4(20)
func4(5)




#
# Задача-3
#
# Написать декоратор с аргументом который будет замерять скорость работы функции ниже. В качестве аргумента передать
# ему максимальное значение секунд, которое может выполняться ваша функция. Если время вышло или ваша функция
# закончила выполнение работы, вывести результат.
#
# def my_func():
#         return sum(range(100000000))
#
#
# print("\n\n")
#
# def timer(input_func):
#     def wrapper(arg, max_time):
#         def signal_handler(signum, frame):
#             raise Exception("Timeout!")
#
#         signal.signal(signal.SIGALRM, signal_handler)
#         signal.alarm(max_time)  # Three seconds
#         res = 0
#         try:
#             res = input_func(arg)
#         except Exception as msg:
#             print("Timeout!")
#             return res
#         signal.alarm(0)
#
#

        # init_time = time.time()
        # t1 = init_time
        # print("Init time: " + str(init_time))
        # print("Finish time: " + str(init_time + max_time))
        # res = None
        # while t1 < init_time + max_time:
        #     #print(t1)
        #     res = input_func(arg)
        #     t1 = time.time()
        # print(t1 - init_time)
        # #while t1 < t1 +


#         return res
#     return wrapper
#
# @timer
# def func3(param):
#     #time.sleep(10)
#     return sum(range(param))



# @timer
# def func4(param):
#     #print(param)
#     time.sleep(10)
#
# print(func4(1, 3))



#print(func3(100000000, 2)) # очень странно себя ведет, не отбивает по тайм-ауту


