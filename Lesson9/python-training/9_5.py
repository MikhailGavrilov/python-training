# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
...
Stationery class (Канцелярия)
...

class Staionary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):
    def draw(self):
        print('Рисуем ручкой', self.title)

class Pencil(Stationary):
    def draw(self):
        print('Рисуем карандашом', self.title)

class Handle(Stationary):
    def draw(self):
        print('Рисуем маркером', self.title)

if __name__ == '__main__':

    pn = Pen('Bсic')
    p1 = Pencil('Сакко и Ванцетти')
    h1 = Handle('Flip Chart')


    pn.draw()
    p1.draw()
    p1.draw()