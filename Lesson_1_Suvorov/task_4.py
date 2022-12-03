data = ['разработка', 'администрирование', 'protocol', 'standard']

for el in data:
    el = el.encode('utf-8')
    print(el)
    el = el.decode('utf-8')
    print(el)
