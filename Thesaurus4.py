#Задание 4
def thesaurus(*args):
    new_dict = {}
    for i in args:
        key = i[0].capitalize()
        if key not in new_dict:
            new_dict[key] = []
        new_dict[key].append(i)
    return new_dict


def thesaurus_adv(*names):
    res_full_names = {}
    for i in names:
        full_names = i.split()
        full_names.reverse() #полное имя начиная с фамилии
        if res_full_names.get(full_names[0][0]): # если существует ключ с первой буквой фамилии
            res_full_names[full_names[0][0]].append(i)
        else:
            res_full_names[full_names[0][0]] = [i]
    for key in res_full_names:
        res_full_names[key] = thesaurus(*res_full_names[key])
    print(res_full_names)


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

