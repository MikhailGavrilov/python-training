# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
class Road:
    _length, _width = 0, 0

    def __init__(self, length, width, weight_sq_mt, thickness):
        self._width_sq_mt, self._thickness, self._length, self.width = weight_sq_mt / 1000, thickness, length, width


        def asphalt()(self):
            return self._lenghth * self._width * self._width_sq_mt * self._thickness


calc = Road(20, 5000, 25, 5)
print(calc.asphalt())
