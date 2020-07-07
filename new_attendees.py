import csv

"""
    Messing around with manipulating CSV files in python.
"""


def get_emails_from_file(file_string):
    """
        Takes in the name of a file, which is opened, read, and set to a variable.
        Variable is then looped over and emails in variable are added to a set.
    """

    opened = open(file_string)
    read = csv.reader(opened)

    set_of_emails = set()

    for line in read:
        set_of_emails.add(line[2])

    return set_of_emails


first_year_emails = get_emails_from_file('attendees1.csv')
second_year_emails = get_emails_from_file('attendees2.csv')

"""
    Function has been performed on the 2 files, now I am finding the difference between the 2 files and printing that as output.
"""

print(second_year_emails.difference(first_year_emails))