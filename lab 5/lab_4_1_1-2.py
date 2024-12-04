from lab_4_base_class import Product
from lab_4_size import Sizeble
from lab_4_apple import *

milk = Product(200, 3, 2, 1,"milk")

try:
    price = int(input("цена товара - "))
    width = int(input("Ширина - "))
    height = int(input("Длина - "))
    depth = int(input("Глубина - "))
    name = str(input("Имя - "))
    newproduct = Product(price,width,height,depth,name)
    print(newproduct)
except:
    print("Недопустимое значение\n\n")



try:
    c = int(input("Введите цену товара: "))
    d = int(input("Введите скидку на  товар: "))
    eggs = Product(c, 8, 6, 4,"eggs")
    if d >= 100:
        raise iskl
    print("Цена товара со скидкой" , eggs.discount(d))
    
except :
    print("Недопустимое значение\n\n")

print("Количество упаковок в транспортировочной коробке: ")
egg = Sizeble(200, 8, 6, 4,"egg")
count = egg.counts_in_box(16, 36, 8)
print(count)
try:
    pie = Sizeble(100, 4, 3, 2,"pie")
    a = int(input("Введите длину транспортировочной коробки: "))
    b = int(input("Введите ширину транспортировочной коробки: "))
    h = int(input("Введите высоту транспортировочной коробки: "))
    print("Количество упаковок в транспортировочной коробке: ")
    print(pie.counts_in_box(a, b, h))
except:
    print("Недопустимое значение параметров коробки")
apple = Apple(100, 4, 3, 2,"apple")
print(apple.tasty())
#print(Apple(100, 4, 3, 2,"apple"))

