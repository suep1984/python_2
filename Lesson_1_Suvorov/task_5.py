import chardet
import subprocess

args = ['ping', 'yandex.ru']
ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
