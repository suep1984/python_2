import json


def write_order_to_json(item, quantity, price, buyer, date):
    data: dict = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json', 'w') as f:
        json.dump(data, f, indent=4)


write_order_to_json('lemon', 3, 100, 'Ivan', '23.12.22')
