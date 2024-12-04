from lab_4_base_class import Product
class Sizeble(Product):
    @classmethod
    def __check_value(self, x): # проверка чтобы был тип инт или флоат
        return (type(x) == int or type(x) == float) and x > 0

    def __init__(self, price, width, height, depth,name):
        if self.__check_value(width) and self.__check_value(height) and self.__check_value(depth):
            Product.__init__(self, price, width, height, depth,name)
        else:
            raise ValueError("Недопустимое значение парамеров")

    def v_product(self): # объем товара
        return self.width * self.height * self.depth

    def v_box(self, box_width, box_height, box_depth): # объем коробки
        return box_width * box_height * box_depth

    def counts_in_box(self, box_width, box_height, box_depth):
        if self.__check_value(box_width) and self.__check_value(box_height) and self.__check_value(box_depth):
            v_box = self.v_box(box_width, box_height, box_depth)
            v_product = self.v_product()
            return v_box // v_product
        else:
            raise ValueError("Недопустимое значение парамеров")

# ПЕРЕГРУЗКА
    def __add__(self, other):
        p = self.price + other.price
        a = self.width + other.width
        b = self.height + other.height
        h = self.depth + other.depth
        return Size(p, a, b, h)



    def __str__(self): # Вывод
        return f"({self.name }, {self.price}, {self.width}, {self.height}, {self.depth})"

