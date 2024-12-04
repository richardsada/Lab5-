from lab_4_base_class import Product
class Apple(Product):
    @classmethod
    def __check_value(self, x): # проверка чтобы был тип инт или флоат
        return (type(x) == int or type(x) == float) and x > 0

    def __init__(self, price, width, height, depth,name):
        if self.__check_value(width) and self.__check_value(height) and self.__check_value(depth):
            Product.__init__(self, price, width, height, depth,name)
        else:
            raise ValueError("Недопустимое значение парамеров")

    def tasty(self):
        
        return "Yes"


    def discount(self, sale):
        return super().discount(2*sale)
    def __str__(self): # Вывод
        return f"({self.name }, {self.price}, {self.width}, {self.height}, {self.depth})"