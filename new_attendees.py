import csv
import sqlite3
import timeit

"""
    Messing around with manipulating CSV files in python.
"""

connection = "/Users/jcksnparsons/coding-practice/csv_manipulation/db.sqlite3"


def memoize(etl_func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache
        result = etl_func(*args)
        cache[args] = result
        return result

    return memoized_func


def post_to_db(my_list):
    for person in my_list:
        with sqlite3.connect(connection) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT INTO Attendees (first_name, last_name, email)
                VALUES (?, ?, ?)""",
                              (person['first_name'], person['last_name'], person['email']))

@memoize
def get_emails_from_file(file_string):
    """
        Takes in csv filename, which is parsed into a list of dictionaries. The function then uses the function above to iterate over that
        list and export each dict into a sql database.
    """

    with open(file_string) as csv_file:
        reader = csv.DictReader(csv_file)

        list_of_attendees = []

        for row in reader:

            person_dict = {}
            for key, value in row.items():

                person_dict[key] = value

            list_of_attendees.append(person_dict)

        return list_of_attendees

print(timeit.timeit("get_emails_from_file('MOCK_DATA.csv')", globals=globals(), number=5000))

