# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"{self.color} {self.name} повернула на Хыудаювшкусешщт")

    def show_speed(self):
        print(f"Скорость: {self.speed}")

    def check_police(self):
        print(f"Полицейская: {self.is_police}")

По
c, t, w, p = Car(40, "Белая", "Белая", "Audi"), TownCar(70, "Черная", "BMW"), SportCar(40, "Красная", "ferrari"),\
             WorkCar(40, "Вишневая", "Lada'), PoliceCar(40, "Серая", "Skoda")
t.go(), t.turn("право"), t.stop()
t.show_speed(), t.check_police()
print(f"Марка: {c.name}, Цвет: {c.color}, Скорость: {c.speed}, Полицейская: {c.is_police} \n")


