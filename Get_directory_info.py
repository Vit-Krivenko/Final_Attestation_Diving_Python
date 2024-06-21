"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
 Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных 
файлов и директорий."""


import os
import json
import csv
import pickle


__all__ = ['get_directory_info']


def get_directory_info(directory_path):
    def get_size(start_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def walk_and_save(directory_path, output_file):
        data = []
        for root, dirs, files in os.walk(directory_path):
            for f in files:
                file_path = os.path.join(root, f)
                file_info = {
                    "name": f,
                    "parent_directory": root,
                    "type": "file",
                    "size_bytes": os.path.getsize(file_path)
                }
                data.append(file_info)

            for d in dirs:
                dir_path = os.path.join(root, d)
                dir_info = {
                    "name": d,
                    "parent_directory": root,
                    "type": "directory",
                    "size_bytes": get_size(dir_path)
                }
                data.append(dir_info)

        with open(output_file + ".json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        with open(output_file + ".csv", "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["name", "parent_directory", "type", "size_bytes"])
            for item in data:
                csv_writer.writerow([item["name"], item["parent_directory"], item["type"], item["size_bytes"]])

        with open(output_file + ".pickle", "wb") as pickle_file:
            pickle.dump(data, pickle_file)

    walk_and_save(directory_path, "directory_info")

if __name__ == '__main__':
    get_directory_info('C:/Geek_brains/Погружение в Python')
