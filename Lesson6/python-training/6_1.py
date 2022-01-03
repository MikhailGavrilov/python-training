# 1.Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
with open('nginx_logs.txt', 'r', encoding = "utf-8") as f:
    requests_line = []
    for line in f:
        remote_addr = line[:line.find('  ')]
        request_type = line[line.find('"') + 1:line.find('"') + 4]
        request_resource = line[line.find('/d'):line.find('HTTP') - 1]
        tuple_requests = (remote_addr, request_type, requested_resource)
        request_list.append(tuple_requests)
        print(tuple_requests)