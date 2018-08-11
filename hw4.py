import logging
import os
import json
import shutil

# *Задача-1*
# Познакомьтесь с модулем logging. Напишите функцию инициализации логгера.
# Используйте логгирование во всех задания ниже. Определите файл в который будет писать ваш логгер.
# Внимательно следите за уровнями логгирования.
#


# add filemode="w" to overwrite

def logger_init(file_path, file_mode, log_level):
    logging.basicConfig(filename=file_path, filemode=file_mode, level=log_level, format="%(asctime)s %(levelname)s: %(message)s")
    # logging.debug("This is a debug message")
    # logging.info("Informational message")
    # logging.error("An error has happened!")


logger_init("/home/troy/files/tmp/python_logger.log", "a", logging.INFO)


# *Задача-2*
#
# У вас есть 2 файла. В каждом файле произвольные символы(строки). Ваша задача обьединить эти строки,
# преобразовать их в поток байт и записать поток байт в файл 3 с именем «Result.bin»

def read_from_file(input_file):
    with open(input_file, "r") as src_file:
        content = src_file.readlines()
        logging.info("Reading file {} content".format(input_file))
    return content


def write_bytes_to_file(new_file, str):
    with open(new_file, "wb") as dst_file:
        logging.info("Writing to file {}".format(new_file))
        dst_file.write(str)


def files_unite(src_file1, src_file2, dst_file):
    logging.info("Files '{}' and '{}' unite execution".format(src_file1, src_file2))
    str_buffer = ""
    for str in read_from_file(src_file1):
        str_buffer = "".join([str_buffer, str])
    for str in read_from_file(src_file2):
        str_buffer = "".join([str_buffer, str])

    print(str_buffer.encode("utf-8"))
    write_bytes_to_file(dst_file, str_buffer.encode("utf-8"))


files_unite("/home/troy/files/tmp/hw_tmp/file1", "/home/troy/files/tmp/hw_tmp/file2", "/home/troy/files/tmp/hw_tmp/Result.bin")


#
# *Задача-3*
#
# У вас есть файл. Ваша функция на вход принимает путь к этому файлу. Вам необходимо определить имя файла,
# название каталога и абсолютный путь. Внутри функции выполните все возможные проверки.
#

def get_file_properties(input_file):
    logging.info("Getting file {} parameters".format(input_file))
    print("Filename is {}, it is located at {}. Absolute path is {} .".format(os.path.basename(input_file),
                                                                              os.path.dirname(input_file),
                                                                              os.path.abspath(input_file)))
    with open(input_file, "r") as curr_file:
        print(curr_file.readable())
        print(curr_file.writable())
        print(curr_file.closed)
        print(curr_file.isatty())
        print(curr_file.seekable())


get_file_properties("/home/troy/files/tmp/hw_tmp/file2")

# *Задача-4*
#
# У вас есть строка вида «Name: Peter, Age: 20, Country: USA».
# Вам необходимо преобразовать эти данные и записать их в файл result.json
#


def write_str_to_json(input_str, dst_file):
    logging.info("writing json to file '{}'".format(dst_file))
    content = input_str.split(",")
    content_dict = {}
    for i in content:
        content_dict[i.split(":")[0].strip()] = i.split(":")[1].strip()
    json1 = json.dumps(content_dict)
    with open(dst_file, "w") as result:
        result.write(json1)


write_str_to_json("Name: Peter, Age: 20, Country: USA", "/home/troy/files/tmp/hw_tmp/result.json")


# *Задача-5*
#
# Напишите функцию копирования файлов и каталогов. На вход ваша функция принимает два аргумента:
# -  путь файла или каталога который необходимо скопировать
# - путь каталога куда этот файл необходимо скопировать

def copy_object(src_file, dst_file):
    logging.info("Copying '{}' to '{}'".format(src_file, dst_file))
    if os.path.isdir(src_file):
        shutil.copytree(src_file, dst_file)
    else:
        shutil.copy(src_file, dst_file)

copy_object("/home/troy/files/tmp/hw_tmp2/result.json", "/home/troy/files/tmp/hw_tmp2/COPY2_result.json")