import os

settings = {}
with open('config1.yaml') as f:
    lines = dict(map(str.split, f.readlines())) #{'base':'my_project', 'settings':' init... .py,dev.py,prod.py, ....}

basedir = lines.pop('base') #{my_project} ->{'settings':'  init   .py,dev.py,prod.py, ....}
for k, v in lines.items():
    os.makedirs(os.path.join(os.curdir, basedir, k), exist_ok=True)
    print(f'Создан каталог: {k}')
    for i in v.split(','):
        with open(os.path.join(os.curdir, basedir, k, i), "w") as f: гг
            print(f'Создан файл: {i} в каталоге {k}')