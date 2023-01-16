import json
import random
from typing import List

from faker import Faker

from conf import MODEL


fake = Faker()


def read_books_titles(file_to_read: str) -> List[str]:
    """
    Читает переданный файл и возвращает список книг.
    :param file_to_read: файл для чтения в формате txt
    :return: список из названий книг
    """

    with open(file_to_read, "r") as file:
        list_of_titles = [title.strip() for title in file.readlines()]

    return list_of_titles


def get_book_title(titles: list) -> str:
    """
    Из переданного списка книг возвращает название книги, выбранное случайным образом.
    :param titles: список книг
    :return: название книги
    """

    idx = random.randint(0, len(titles) - 1)
    return titles[idx]


def get_year() -> int:
    """Возвращает год, сгенерированный случайным образом."""

    return random.randint(1850, 2022)


def get_pages() -> int:
    """Возвращает колчество страниц, сгенерированные случайным образом."""

    return random.randint(300, 1000)


def get_isbn(fake_obj) -> str:
    """
    Принимает экземпляр класса Faker() и возвращает isbn13.
    :param fake_obj: экземпляр класса Faker()
    :return: isbn13
    """

    return fake_obj.isbn13()


def get_rating() -> float:
    """Возвращает рейтинг книги, сгенерированный случайным образом."""

    return round(random.uniform(0, 5), 1)


def get_price() -> float:
    """Возвращает стоимость книги, сгенерированную случайным образом."""

    return round(random.uniform(400, 2000), 1)


def get_author(fake_obj) -> List[str]:
    """
    Принимает экземпляр класса Faker() и возвращает список из авторов книги.
    Количество авторов генерируется случайным образом от 1 до 3.
    :param fake_obj: экземпляр класса Faker()
    :return: список из авторов книги
    """

    number_of_authors = random.randint(1, 3)
    return [fake_obj.name() for _ in range(number_of_authors)]


def gen_function(counter=1) -> dict:
    """
    Функция-генератор, возвращает словарь заданного типа.
    :param counter: счетчик, по умолчанию равен 1
    :return: словарь типа:
    {
       "model": "shop_final.book",
       "pk": 1,
       "fields": {
           "title": "test_book",
           "year": 2020,
           "pages": 123,
           "isbn13": "978-1-60487-647-5",
           "rating": 5,
           "price": 123456.0,
           "author": [
               "test_author_1",
               "test_author_2"
           ]
       }
    }
    """

    book_titles = read_books_titles("books.txt")

    while True:

        dict_ = {"model": MODEL,
                 "pk": counter,
                 "fields": {
                     "title": get_book_title(book_titles),
                     "year": get_year(),
                     "pages": get_pages(),
                     "isbn13": get_isbn(fake),
                     "rating": get_rating(),
                     "price": get_price(),
                     "author": get_author(fake)
                 }
                 }

        yield dict_
        counter += 1


def main() -> None:
    """С помощью функции-генератора создает список из 100 словарей и сохраняет его в json-файл."""

    gen = gen_function()

    list_of_100 = [next(gen) for _ in range(100)]

    with open("output.json", "w") as f:
        json.dump(list_of_100, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()




