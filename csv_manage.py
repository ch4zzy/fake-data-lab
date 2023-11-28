import csv 
from models import *


def create_csv_file(data_class, db_name: str) -> None: 
    fields = data_class.__dataclass_fields__.keys()
    with open(f"output/{db_name}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)


def write_csv_file(data_class, db_name: str, data: list) -> None:
    fields = data_class.__dataclass_fields__.keys()
    with open(f"output/{db_name}.csv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        for row in data:
            writer.writerow(row)
