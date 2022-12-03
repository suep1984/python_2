data = ['attribute', 'класс', 'функция', 'type']


for el in data:
    try:
        print(eval(f'b"{el}"'))
    except SyntaxError:
        print(f'"{el}" невозможно представить в байтовом типе')
