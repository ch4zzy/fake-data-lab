from models import *
import random
from csv_manage import * 
from faker import Faker
import pandas as pd
from constants import genres


def generate_data_author(data_class, n: int) -> csv:
    try: 
        create_csv_file(data_class, data_class.__name__)
    except FileExistsError:
        pass

    fake = Faker()
    data = []
    for _ in range(n):
        mapping = {
            "author_id": _,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birth": fake.date_between(start_date="-70y", end_date="-18y"),
            "phone": fake.phone_number(),
        }
        data.append(mapping)
    write_csv_file(data_class, data_class.__name__, data)

#generate_data_author(Author, 10000)


def generate_data_book(data_class, n: int) -> csv:
    try: 
        create_csv_file(data_class, data_class.__name__)
    except FileExistsError:
        pass

    fake = Faker()
    used_isbns = set()
    data = []
    for _ in range(n):

        isbn = fake.unique.isbn10()
        while isbn in used_isbns:
            isbn = fake.unique.isbn10()
        used_isbns.add(isbn)

        mapping = {
            "isbn": isbn,
            "name": fake.word(),
            "genre": random.choice(genres),
            "release_date": fake.date_between(start_date="-30y", end_date="today"),
            "price": fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            "publisher_id": 0,
        }
        data.append(mapping)
    write_csv_file(data_class, data_class.__name__, data)

#generate_data_book(Book, 100000)


def generate_data_customer(data_class, n: int) -> csv:
    try: 
        create_csv_file(data_class, data_class.__name__)
    except FileExistsError:
        pass

    fake = Faker()
    data = []
    for _ in range(n):
        address = fake.address().replace("\n", " ")
        current_address = address.replace(",", " ")
        mapping = {
            "customer_id": _,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": current_address,
        }
        data.append(mapping)
    write_csv_file(data_class, data_class.__name__, data)

#generate_data_customer(Customer, 10000)


def generate_data_order(data_class, n: int) -> csv:
    try: 
        create_csv_file(data_class, data_class.__name__)
    except FileExistsError:
        pass

    fake = Faker()
    data = []
    for _ in range(n):
        mapping = {
            "order_id": _,
            "customer_id": random.randint(0, 9999),
            "date": fake.date_between(start_date="-15y", end_date="today"),
            "status": random.randint(0, 1),
        }
        data.append(mapping)
    write_csv_file(data_class, data_class.__name__, data)

# generate_data_order(Order, 100000)


def generate_data_book_author(data_class, n: int) -> csv:
    try: 
        create_csv_file(data_class, data_class.__name__)
    except FileExistsError:
        pass

    fake = Faker()
    data = []
    isbn = pd.read_csv("output/Book.csv")["isbn"].tolist()
    author_id = pd.read_csv("output/Author.csv")["author_id"].tolist()
    for _ in range(n):
        mapping = {
            "isbn": random.choice(isbn),
            "author_id": random.choice(author_id),
        }
        data.append(mapping)
    write_csv_file(data_class, data_class.__name__, data)

generate_data_book_author(BookAuthor, 100000)


def generate_data_book_order(data_class, n: int) -> csv:
    try: 
        create_csv_file(data_class, data_class.__name__)
    except FileExistsError:
        pass

    fake = Faker()
    data = []
    isbn = pd.read_csv("output/Book.csv")["isbn"].tolist()
    order_id = pd.read_csv("output/Order.csv")["order_id"].tolist()
    for _ in range(n):
        mapping = {
            "isbn": random.choice(isbn),
            "order_id": random.choice(order_id),
        }
        data.append(mapping)
    write_csv_file(data_class, data_class.__name__, data)

generate_data_book_order(OrderBook, 100000)
