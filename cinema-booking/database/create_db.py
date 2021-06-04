import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def create_db(table_name):
    my_db = mysql.connector.connect(
        host="localhost",
        user=os.environ["USER"],
        password=os.environ["DB_PASSWORD"])
    cursor = my_db.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {table_name}")


def connect(database):
    db = mysql.connector.connect(
      host="localhost",
      user=os.environ["USER"],
      password=os.environ["DB_PASSWORD"],
      database=f"{database}")
    return db


def create_table(database, table):
    my_db = connect(database)
    cursor = my_db.cursor()
    cursor.execute(f"CREATE TABLE if not exists {table}")


def insert_into_table(database, table, columns, values, values_number):
    my_db = connect(database)
    cursor = my_db.cursor()
    command = f"INSERT INTO {table} {columns} VALUES {values_number}"
    val = values
    cursor.executemany(command, val)
    my_db.commit()
    my_db.close()


create_db("banking")
create_db("cinema")
create_table("cinema", "seat ("
                       "seat_id VARCHAR(5), "
                       "taken INT, "
                       "price INT)")
create_table("banking", "card ("
                        "type VARCHAR(20),"
                        "number INT(8),"
                        "cvc INT(3),"
                        "holder VARCHAR(30),"
                        "balance FLOAT)")

seat_values = [
    ("A1", 1, 120),
    ("A2", 0, 100),
    ("A3", 0, 120),
    ("B1", 0, 100),
    ("B2", 1, 150),
    ("B3", 0, 120)
]

insert_into_table("cinema", "seat",
                  "(seat_id, taken, price)",
                  seat_values,
                  values_number="(%s, %s, %s)")

card_values = [
    ("Master Card", 23456789, 234, "Mary Smith", 2000.0),
    ("Visa", 12345678, 123, "John Smith", 460.0),
    ("Master Card", 87654321, 876, "Hailey Bond", 1100.0)
]

insert_into_table("banking", "card",
                  "(type, number, cvc, holder, balance)",
                  card_values,
                  values_number="(%s, %s, %s, %s, %s)")
