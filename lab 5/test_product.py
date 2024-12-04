import pytest
import os
from lab_4_base_class import Product  

@pytest.fixture
def valid_product():
    """Фикстура для создания валидного экземпляра Product."""
    return Product(price=100.0, width=10.0, height=20.0, depth=30.0, name="TestProduct")


@pytest.fixture
def invalid_product_data():
    """Фикстура для предоставления некорректных данных."""
    return [
        {"price": -100, "width": 10.0, "height": 20.0, "depth": 30.0, "name": "InvalidPrice"},
        {"price": 100.0, "width": -10.0, "height": 20.0, "depth": 30.0, "name": "InvalidWidth"},
        {"price": "100", "width": 10.0, "height": 20.0, "depth": 30.0, "name": "InvalidType"},
    ]


@pytest.fixture
def test_file():
    """Фикстура для предоставления временного файла."""
    filename = "test_product.json"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


@pytest.mark.parametrize("sale, expected", [
    (10, 90.0),
    (20, 80.0),
    (50, 50.0),
])
def test_discount(valid_product, sale, expected):
    """Тестирование метода discount."""
    assert valid_product.discount(sale) == expected


@pytest.mark.parametrize("sale", [-10, "20", 150])
def test_discount_invalid(valid_product, sale):
    """Тестирование метода discount с некорректными данными."""
    with pytest.raises(ValueError):
        valid_product.discount(sale)


def test_init_valid(valid_product):
    """Тестирование корректной инициализации."""
    assert valid_product.price == 100.0
    assert valid_product.width == 10.0
    assert valid_product.height == 20.0
    assert valid_product.depth == 30.0
    assert valid_product.name == "TestProduct"


def test_init_invalid(invalid_product_data):
    """Тестирование инициализации с некорректными данными."""
    for data in invalid_product_data:
        with pytest.raises(ValueError):
            Product(**data)


def test_write_to_file(valid_product, test_file):
    """Тестирование метода записи в файл."""
    valid_product.write_to_file(test_file)
    assert os.path.exists(test_file)

    with open(test_file, 'r', encoding='utf-8') as file:
        data = file.read()
        assert '"price": 100.0' in data
        assert '"name": "TestProduct"' in data


def test_read_from_file(valid_product, test_file):
    """Тестирование метода чтения из файла."""
    valid_product.write_to_file(test_file)
    product_from_file = Product.read_from_file(test_file)

    assert product_from_file.price == valid_product.price
    assert product_from_file.width == valid_product.width
    assert product_from_file.height == valid_product.height
    assert product_from_file.depth == valid_product.depth
    assert product_from_file.name == valid_product.name


def test_read_from_file_invalid(test_file):
    """Тестирование чтения из некорректного файла."""
    with open(test_file, 'w', encoding='utf-8') as file:
        file.write("Некорректные данные")

    with pytest.raises(ValueError):
        Product.read_from_file(test_file)
