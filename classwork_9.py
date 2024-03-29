# from io import TextIOWrapper
#
#
# class Category(object):
#     categories: list[str] = []
#
#     @classmethod
#     def add(cls, category: str) -> int:
#         """Add new category
#
#         :param category: New Category Name
#         :return: New Category Index in category list
#         :raise ValueError: Category exist
#         """
#         if not isinstance(category, str):
#             raise TypeError
#
#         category = category.title()
#         if category not in cls.categories:
#             cls.categories.append(category)
#             return cls.categories.index(category)
#         raise ValueError(f"category: {category} exist")
#
#     @classmethod
#     def get(cls, pk: int) -> str:
#         """Get category by ID
#
#         :param pk: Category ID
#         :return: Category Name
#         :raise IndexError: Category not presented in category list
#         """
#         try:
#             return cls.categories[pk]
#         except IndexError:
#             raise IndexError("category not found")
#
#     @classmethod
#     def delete(cls, pk: int) -> None:
#         """Delete category by ID
#
#         :param pk: Category ID
#         """
#         try:
#             del cls.categories[pk]
#         except IndexError:
#             ...
#
#     @classmethod
#     def update(cls, pk: int, category: str) -> None:
#         """Update category by ID
#
#         :param pk: Category ID
#         :param category: New Category Name
#         :raise ValueError: If category exist
#         """
#         category = category.title()
#         try:
#             cls.get(pk=pk)
#         except IndexError:
#             cls.add(category=category)
#         else:
#             if category not in cls.categories:
#                 cls.categories[pk] = category
#             else:
#                 raise ValueError("category not unique")
#
#
# # LESSON 9 - FILES
#
#
# # file = open(file="./output.txt", mode="w", encoding="utf-8")
# # from time import sleep
# #
# # while ...:
# #     file.write("Hello\n")
# #     file.flush()
# #     sleep(1)
# # file.write("Hello World\n")
# # file.writelines("Hello World\n")
# # print(file.writable())
# # print(file.read())
# # file.seek(0)
# # print(file.read())
# # print(file.readline())
# # print(file.readlines())
# # print(file.readable())
# # print(file.closed)
# # lines = [line.strip() for line in file if line.strip()]
# # print(lines)
# # file.close()
# # print(file.closed)
#
#
# # with (
# #     open(file="./input.txt", mode="rt", encoding="utf-8") as file,
# #     open(file="./output.txt", mode="wt", encoding="utf-8")
# # ):
# #     print(file.closed)
# # print(file.closed)
#
#
# class DatabaseSession(object):
#
#     def __init__(self):
#         self.is_close = False
#
#     def close(self):
#         self.is_close = True
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is ValueError:
#             return True
#         self.close()
#
#
# # with DatabaseSession() as session:  # type: DatabaseSession
# #     print(session.is_close)
# #     raise ValueError("1")
# # print(session.is_close)
# # try:
# # from orjson import loads, dumps
# # except ImportError:
# #     from json import load, loads, dumps, dump
#
# # with open(file="./input.json", mode="rt", encoding="utf-8") as file:
# #     data = load(file)
# #     print(data.get("referrer"))
# #
# # data = {
# #     "id": 1,
# #     "name": "Кофе",
# #     "price": 5.5
# # }
# # with open(file="./output.json", mode="wt", encoding="utf-8") as file:
# #     text = dumps(data)
# #     file.write(text.decode())
# # from yaml import safe_load
# #
# # with open("./config.yaml", "rt", encoding="utf-8") as file:
# #     data = safe_load(file)
# #     print(data)
#
# # from configparser import ConfigParser
# #
# #
# # parser = ConfigParser()
# # parser.read("./config.ini")
# # print(parser.get(section="SECTION1", option="key1"))
# # print(parser.sections())
#
# from csv import reader, writer, DictReader, DictWriter
#
# with open("./output.csv", "wt", encoding="utf-8") as file:
#     # r = reader(file)
#     # for line in r:
#     #     print(line)
#     # r = DictReader(file)
#     # for line in r:
#     #     print(line)
#     data = [
#         {
#             "id": 1,
#             "name": "Coffee"
#         },
#         {
#             "id": 2,
#             "name": "Pancake"
#         }
#     ]
#     w = DictWriter(file, fieldnames=["id", "name"])
#     w.writeheader()
#     w.writerows(data)
# from bz2 import compress
# from datetime import datetime
# from ujson import load
#
# with open("./user_register.json", "rt", encoding="utf-8") as file:
#     data = load(file)

# from typing import *
# from annotated_types import Annotated, Predicate
# from pydantic import BaseModel, EmailStr, Field, PlainValidator, validate_call
# from pydantic.types import Decimal, PositiveInt
#
# AlphaStr = Annotated[str, Predicate(func=str.isalpha)]
#
#
# class UserRegisterForm(BaseModel):
#     first_name: AlphaStr = Field(min_length=2, max_length=32)
#     last_name: Optional[AlphaStr] = Field(default=None)
#     email: EmailStr
#     age: int = Field(ge=18, lt=100)
#     date_register: datetime
# lang: list[Union[int, float]]
# role: Literal[
#     "user",
#     "admin",
#     "superuser"
# ]


# data = UserRegisterForm.parse_file(path="./user_register.json")
# print(data.model_dump(mode="json", exclude={"date_register"}))
# from datetime import datetime
# print(datetime.now().isoformat())

# class Product(BaseModel):
#     id: PositiveInt
#     price: Decimal = Field(max_digits=5, decimal_places=2)
#
#
# class Category(BaseModel):
#     id: PositiveInt = Field(default=...)
#     name: AlphaStr = Field(default=...)
#     products: Optional[list[Product]] = Field(default=None)
#     parent: Optional["Category"] = Field(default=None)
#
#
# data = {
#     "id": 1,
#     "name": "Coffee",
#     "products": [
#         {
#             "id": 1,
#             "price": 12341234.234
#         }
#     ],
#     "parent": {
#         "id": -5,
#         "name": "Pancake"
#     }
# }
# # cat = Category.model_validate(data)
#
#
# @validate_call()
# def is_palindrome(text: str) -> bool:
#     return text.lower() == text.lower()[::-1]

# class Car(object):
#    cars: list[dict]
#
#     def __init__(self, cars: list[dict]) -> None:
#         self.cars = cars
#
#     @classmethod
#     def get_cars(cls) -> None:
#         for car in cls.cars:
#             print(car.get("Number"))
#
#     def print_cars(self) -> None:
#         for car in self.cars:
#             print(car.get("Number"))
#
#
# cars_list = [
#     {
#         "Brand": "Iveco",
#         "Model": "35c12",
#         "Number": "AT1698-7",
#     },
#     {
#         "Brand": "Iveco",
#         "Model": "35c13",
#         "Number": "AC8054-5",
#     },
# ]
#
# Car.cars = cars_list
# Car.get_cars()
#
# a = Car(cars_list)
# a.print_cars()

# miro.com
# У классов метод .mro


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height


r = Rectangle(10, 5)
print(r.area)  # Output: 50

a = Rectangle(20, 30)
print(a.area)  # Output: 50


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


p = Person("John", 25)
print(p.name)  # Output: John
print(p.age)  # Output: 25

p.name = "Alex"
p.age = 30

print(p.name)  # Output: Alex
print(p.age)  # Output: 30


class A:
    __hidden: str

    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, value):
        self.__hidden = value

    def __init__(self, val):
        self.__hidden = val


a = A('value')
print(a.hidden)
a.hidden = 123
print(a.__dict__)
print(a.hidden)

with open(file="./test.txt", mode="rt", encoding="utf-8") as file:
    print(file.closed)


class DatabaseSession(object):
    def __init__(self):
        self.is_close = False

    def close(self):
        self.is_close = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ValueError:
            return True
        self.close()


with DatabaseSession() as session:  # DatabaseSession
    print(session.is_close)
    raise ValueError
print(session.is_close)

# pip install ujson
# pip install orjson
# pip install pyyaml

# pip install pydantic
# pip install email-validator


try:
    from ujson import load, loads, dumps, dump
except ImportError:
    from json import load, loads, dumps, dump

from pydantic import BaseModel, EmailStr, Field


