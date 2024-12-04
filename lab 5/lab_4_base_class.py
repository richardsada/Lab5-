import json

class Product:
    @classmethod
    def __check_value(cls, x):  # проверка чтобы был тип int или float
        return (type(x) == int or type(x) == float) and x > 0

    def __init__(self, price, width, height, depth, name):
        if self.__check_value(price) and self.__check_value(width) and self.__check_value(height) and self.__check_value(depth):
            self.price = price
            self.width = width
            self.height = height
            self.depth = depth
            self.name = name
        else:
            raise ValueError("Недопустимое значение параметров")

    def discount(self, sale):
        if self.__check_value(sale):
            sale = self.price - (self.price * sale / 100)
            return round(sale, 2)
        else:
            raise ValueError("Недопустимое значение скидки")

    def __str__(self):  # Вывод
        return f"({self.name}, {self.price}, {self.width}, {self.height}, {self.depth})"

    def read_from_file(cls, filename):
        """
        Метод считывает данные о продукте из файла.
        Ожидается формат JSON с ключами: price, width, height, depth, name.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # Проверяем наличие всех ключей
            required_keys = {'price', 'width', 'height', 'depth', 'name'}
            if not required_keys.issubset(data):
                raise ValueError(f"Некорректный формат данных в файле. Ожидались ключи: {required_keys}")

            # Создаем экземпляр класса Product
            return cls(
                price=data['price'],
                width=data['width'],
                height=data['height'],
                depth=data['depth'],
                name=data['name']
            )
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден.")
        except json.JSONDecodeError:
            raise ValueError("Некорректный формат файла. Ожидается JSON.")
        except Exception as e:
            raise RuntimeError(f"Произошла ошибка при чтении файла: {e}")

    def write_to_file(self, filename):
        """
        Метод записывает данные о продукте в файл в формате JSON.
        """
        try:
            
            data = {
                'price': self.price,
                'width': self.width,
                'height': self.height,
                'depth': self.depth,
                'name': self.name
            }
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise RuntimeError(f"Произошла ошибка при записи в файл: {e}")
