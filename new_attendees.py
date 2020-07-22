import csv
import sqlite3

"""
    Messing around with manipulating CSV files in python.
"""

connection = "/Users/jcksnparsons/coding-practice/csv_manipulation/db.sqlite3"


def post_to_db(my_list):
    for person in my_list:
        with sqlite3.connect(connection) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT INTO Attendees (first_name, last_name, email)
                VALUES (?, ?, ?)""",
                              (person['first_name'], person['last_name'], person['email']))


def get_emails_from_file(file_string):
    """
        Takes in a csv file and returns a list of dictionaries, each containing the contact information for a party attendee.
    """

    with open(file_string) as csv_file:
        reader = csv.DictReader(csv_file)

        list_of_attendees = []

        for row in reader:

            person_dict = {}
            for key, value in row.items():

                person_dict[key] = value

            list_of_attendees.append(person_dict)

        post_to_db(list_of_attendees)


get_emails_from_file('attendees1.csv')
