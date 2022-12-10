import yaml
from yaml.loader import SafeLoader

data = {
    'list': ['a', 'b', 'c'],
    'integer': 123,
    'dict': {
        'num1': '1€',
        'num2': '2€',
        'num3': '3€'

    },
}

with open('file.yaml', 'w') as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

with open('file.yaml') as f:
    content = yaml.load(f, Loader=SafeLoader)
print(content)
