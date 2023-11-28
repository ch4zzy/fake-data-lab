from dataclasses import dataclass


@dataclass
class Author:
    author_id: int
    first_name: str
    last_name: str
    date_of_birth: str
    phone: str


@dataclass
class Book:
    isbn: str 
    name: str 
    genre: str 
    release_date: str
    price: float
    publisher_id: int


@dataclass
class Publisher:
    publisher_id: int 
    name: str 
    address: str
    email: str 
    phone: str


@dataclass
class Customer:
    customer_id: int 
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    

@dataclass
class Order:
    order_id: int 
    customer_id: int
    date: str
    status: bool


@dataclass
class OrderBook:
    order_id: int
    isbn: str


@dataclass
class BookAuthor:
    isbn: str
    author_id: int
