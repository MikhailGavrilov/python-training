#Задание 5
# реализовать функцию get_jokes, возвращающую n шуток,
# сформированных из трех случайный слов, взятых из трех списков (по одному из каждого):
from random import randrange


def get_jokes(n):
    joke_list = []
    for _ in range(n):
        joke = ' '.join([nouns[randrange(len(nouns))], adv[randrange(len(adv))], adj[randrange(len(adj))]])
        joke_list.append(joke)
    print(joke_list)



nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adv = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adj = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(8))