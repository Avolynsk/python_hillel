import json
import os
from functools import total_ordering

import yaml
import functools

# Задача-1
# У вас есть список(list) IP адресов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)
#


class IpAddressProcessor(object):

    def __init__(self, arg):
        self.addrlist = arg

    def get_ipaddr_list(self):
        return self.addrlist

    def get_reversed_ipaddr_list(self):
        tmp_list = list()
        for i in self.addrlist:
            tmp_list.append(i[::-1])
        return tmp_list

    def get_ipaddr_tails_list(self):
        tmp_list = list()
        for i in self.addrlist:
            tmp_list.append(i[i.index(".")+1:])
        return tmp_list

    def get_ipaddr_last_octet_list(self):
        tmp_list = list()
        for i in self.addrlist:
            tmp_list.append(i[i.rindex(".")+1:])
        return tmp_list


ipaddr_processor = IpAddressProcessor(["8.8.8.8", "8.8.4.4"])

print(ipaddr_processor.addrlist)
print(ipaddr_processor.get_ipaddr_list())
print(ipaddr_processor.get_reversed_ipaddr_list())
print(ipaddr_processor.get_ipaddr_tails_list())
print(ipaddr_processor.get_ipaddr_last_octet_list())

# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу


class JsonFileProcessor(object):

    def json_to_file(self, output_file, json_str):
        with open(output_file, "w") as dst_file:
            str(json_str).replace("'", "\"")
            dst_file.write(str(json_str).replace("'", "\""))

    def json_load(self, input_file):
        with open(input_file) as input_file:
            curr_json = json.load(input_file)
        return curr_json

    def jsons_unite(self, src_file1, src_file2, dst_file):
        json1 = self.json_load(src_file1)
        json1.update(self.json_load(src_file2))
        self.json_to_file(dst_file, json1)

    def get_rel_file_path(self, src_file):
        return os.path.relpath(src_file)

    def get_abs_file_path(self, src_file):
        return os.path.abspath(src_file)


json_proc = JsonFileProcessor()

print(json_proc.json_load("/home/troy/files/py_taining_hillel/file1.json"))

test = json_proc.json_load("/home/troy/files/py_taining_hillel/file2.json")
print(test)
#json_proc.json_to_file("/home/troy/files/py_taining_hillel/file3.json", test)

json_proc.jsons_unite("/home/troy/files/py_taining_hillel/file1.json", "/home/troy/files/py_taining_hillel/file3.json", "/home/troy/files/py_taining_hillel/file4.json")
print(json_proc.get_rel_file_path("/home/troy/files/py_taining_hillel/file3.json"))
print(json_proc.get_abs_file_path("/home/troy/files/py_taining_hillel/file3.json"))


#
# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.
#
#

class Unit(object):

    def __init__(self, name="new_unit", mac="02:42:91:59:4e:8f", ipaddr="127.0.0.1", login="admin", passwd="12345678"):
        self.name = name
        self.mac = mac
        self.ipaddr = ipaddr
        self.login = login
        self.passwd = passwd

    def __str__(self):
        return str("Unit info: name={}, mac={}, ipaddr={}, login={}, passwd={}".format(self.name, self.mac,
                                                                                       self.ipaddr, self.login,
                                                                                       self.passwd))

    @property
    def unit_name(self):
        return self.name

    @unit_name.setter
    def unit_name(self, input_value):
        self.name = input_value

    @property
    def unit_mac(self):
        return self.mac

    @unit_mac.setter
    def unit_mac(self, input_value):
        self.mac = input_value

    @property
    def unit_ipaddr(self):
        return self.ipaddr

    @unit_ipaddr.setter
    def unit_ipaddr(self, input_value):
        self.ipaddr = input_value

    @property
    def unit_login(self):
        return self.login

    @unit_login.setter
    def unit_login(self, input_value):
        self.login = input_value

    @property
    def unit_passwd(self):
        return self.passwd

    @unit_passwd.setter
    def unit_passwd(self, input_value):
        self.passwd = input_value


unit1 = Unit()
print(unit1.unit_name)
print(unit1.unit_mac)
print(unit1.unit_ipaddr)
print(unit1.unit_login)
print(unit1.unit_passwd)

unit1.unit_name = "New Name"
unit1.unit_mac = "34:f3:9a:f2:70:79"
unit1.unit_ipaddr = "192.168.10.17"
unit1.unit_login = "Admin"
unit1.unit_passwd = "admin123"

print(unit1.unit_name)
print(unit1.unit_mac)
print(unit1.unit_ipaddr)
print(unit1.unit_login)
print(unit1.unit_passwd)

print(unit1)


# Задача-4
# Для решения этой задачи вам необходимо будет познакомиться
# с форматом данных YAML(YML). Для работы с этим типом данных
# так же существуют библиотеки на Python (например PyYAML).
#
# Создайте класс который будет помогать вам в решении повседневных задач а именно:
# 1)Запись в файл
# 2)Чтение из файла

class YAMLProcessor(object):
    def yaml_to_file(self, output_file, src_yaml):
        with open(output_file, "w") as dst_file:
            yaml.dump(src_yaml, dst_file, default_flow_style=False)

    def yaml_load(self, input_file):
        with open(input_file) as input_file:
            curr_yml = yaml.load(input_file)
        return curr_yml


ymlproc = YAMLProcessor()

print(ymlproc.yaml_load("/home/troy/files/py_taining_hillel/file1.yml"))

yml1 = ymlproc.yaml_load("/home/troy/files/py_taining_hillel/file1.yml")

ymlproc.yaml_to_file("/home/troy/files/py_taining_hillel/file2.yml", yml1)


# *Задача - 5*
# ```Создать класс для представления информации о времени.
# Ваш класс должен иметь  возможности установки времени и изменения его отдельных полей (час, минута, секунда)
# с проверкой допустимости вводимых значений. В случае недопустимых значений полей выбрасываются исключения.
# Создать методы изменения времени на заданное количество часов, минут и секунд.```
#


class MyTime(object):

    def __init__(self, hours_in=12, minutes_in=0, seconds_in=0):
        self.hours_var = hours_in
        self.minutes_var = minutes_in
        self.seconds_var = seconds_in

    def __check_input_params__(self, input_data, low_limit, high_limit):
        if input_data < low_limit or input_data > high_limit:
            raise ValueError("Provided data is out of range: {}. Should be between {} and {}."
                             .format(input_data, low_limit, high_limit))

    @property
    def hours(self):
        return self.hours_var

    @hours.setter
    def hours(self, input_data):
        self.__check_input_params__(input_data, 0, 23)
        self.hours_var = input_data

    @property
    def minutes(self):
        return self.minutes_var

    @minutes.setter
    def minutes(self, input_data):
        self.__check_input_params__(input_data, 0, 59)
        self.minutes_var = input_data

    @property
    def seconds(self):
        return self.seconds_var

    @seconds.setter
    def seconds(self, input_data):
        self.__check_input_params__(input_data, 0, 59)
        self.seconds_var = input_data

    def time_shift(self, input_param):
        self.seconds = (self.seconds + input_param) % 60
        self.minutes = (self.minutes + input_param // 60) % 60
        self.hours = (self.hours + input_param // 3600) % 24

    def __str__(self):
        return str("{}:{}:{}".format(str(self.hours).zfill(2), str(self.minutes).zfill(2), str(self.seconds).zfill(2)))


mytime = MyTime(15, 0, 0)
# print(mytime.hours)
# mytime.hours = 22
# print(mytime.hours)
# mytime.seconds = 33
# print(mytime.seconds)
# mytime.seconds = 53
# print(mytime.seconds)

print(mytime.hours)
print(mytime.hours)
print(mytime)

mytime.time_shift(3661)
print(mytime)


# *Задача - 6*
# ```Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер группы,
# успеваемость (массив из пяти элементов).
# Создать массив(студентов) из десяти элементов такого типа, упорядочить записи по возрастанию среднего балла.
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.```

@total_ordering
class Student(object):
    def __init__(self, name="New Student A.A.", group="1", grades=[0, 0, 0, 0, 0]):
        self.name = name
        self.group = group
        self.grades = grades

    def __str__(self):
        return str("{} from group {}, grades: {}".format(self.name, self.group, self.grades))

    def __hash__(self):
        return sum(self.grades)/len(self.grades)

    def __lt__(self, other):
        return self.__hash__() < other.__hash__()


def get_students_by_grade(students_list, input_param):
    result = list()
    for i in students_list:
        print(set(i.grades))
        if set(i.grades) == {input_param}:
            result.append(i)

    return result


my_student1 = Student()
my_student2 = Student("Mark", "2b", [5, 5, 5, 5, 5])
my_student3 = Student("Roger", "2b", [5, 5, 5, 4, 4])

print(my_student1)
print(my_student2)

students = list()
students.append(my_student1)
students.append(my_student2)
students.append(my_student3)
for i in students:
    print(i)
print()
students.sort()
for i in students:
    print(i)

list5 = get_students_by_grade(students, 5)
for i in list5:
    print(i)
