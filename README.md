## Зачетное задание для курса DEV-PY110.

____

Зачетное задание представляет из себя модуль main.py, который генерирует случайные книги и сохраняет информацию по ним в json-файл.

Модуль содержит функцию-генератор, которая возвращает словари следующей структуры:

```
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
```
___

1. Установка необходимых пакетов:
 ```
pip install -r requarements.txt
```

2. Запуск проекта:
```
python3 main.py
```
