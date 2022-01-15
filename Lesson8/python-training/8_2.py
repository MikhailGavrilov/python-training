# Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
import re


LOG = 'nginx_logs'


def log_parce(src):
    re_list = [r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
               r'\(.*?)\]',
               r'\["([A-Z]{3}',
               r'\s(\/[\w\/]+)',
               r'\s(\d{3})\s',
               r'\s\d{3}\s(\d+)']
    return tuple(re.findall(x,src)[0] for x in re_list)

if __name__ == '__main__':
    with open(LOG) as f:
        count, line = 1100, f.readline()
        while line and count:
            print(log_parse(line))
            count = f.readline()