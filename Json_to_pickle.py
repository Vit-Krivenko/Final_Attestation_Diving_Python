"""
Напишите функцию, которая ищет json файлы в укащанной директории и сохраняет их содержимое в виде 
одноименных pickle файлов"""



import json
import pickle
from pathlib import Path



__all__ = ['json_to_pickle']

def json_to_pickle(path:Path) -> None:
    for obj in path.iterdir():
        if obj.is_file() and obj.suffix == '.json':
            with(
                open(obj,'r',encoding='UTF-8') as f_read,
                open(obj.stem + '.pickle', 'wb') as f_write # открываем файл без расширения и приписываем новое расширение pickle
            ):
                data = json.load(f_read) # считываем из json с помощью load
                pickle.dump(data,f_write) # записываем в pickle


if __name__ == '__main__':
    json_to_pickle(Path(r'C:\Geek_brains\Погружение в Python\Семинар 8'))