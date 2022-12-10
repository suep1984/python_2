import chardet
import os
import re
import csv

file_list = [name for name in os.listdir(".") if re.match(r'info_\d', name)]


def get_data():
    main_data = [['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in range(len(file_list)):
        main_data.append([])
        with open(f'{file_list[i]}', "rb") as f:
            content = f.read()
            res_cod = chardet.detect(content)
        with open(f'{file_list[i]}', "r", encoding=res_cod['encoding']) as f:
            for line in f:
                if re.match(fr'^{main_data[0][0]}:', line):
                    main_data[i + 1].append(line.split(':')[1].strip())
                if re.match(fr'^{main_data[0][1]}:', line):
                    main_data[i + 1].append(line.split(':')[1].strip())
                if re.match(fr'^{main_data[0][2]}:', line):
                    main_data[i + 1].append(line.split(':')[1].strip())
                if re.match(fr'^{main_data[0][3]}:', line):
                    main_data[i + 1].append(line.split(':')[1].strip())
    return main_data


def write_to_csv(file):
    with open(file, 'w') as f:
        data = get_data()
        for row in data:
            csv.writer(f).writerow(row)


write_to_csv('test.csv')
