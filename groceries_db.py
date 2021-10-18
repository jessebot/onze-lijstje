#!/usr/bin/env python3
# script by jessebot@linux.com to get the groceries and do the things
import argparse
import subprocess
import pymongo


def add_new_grocery(grocery):
    """
    Takes a str of a groceries name and adds it to a sqlite3 db
    returns True if it all worked out
    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # the name of the db
    mydb = myclient["mygroceries"]
    # collection - like a table?
    mycol = mydb["groceries"]
    # insert a grocery
    my_groceries_dict = {"name": grocery,
                         "category": "fruit"}
    x = mycol.insert_one(my_groceries_dict)
    return True


def get_all_groceries():
    """
    grabs all the groceries from sqlite3 db
    - returns a list of tuples with 2 strings of grocery_name, and time_stamp
    """
    # TODO: make a mongodb base class
    # we're using localhost for now
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # the name of the db
    mydb = myclient["mygroceries"]
    # collection - like a table?
    mycol = mydb["groceries"]
    all_groceries = mycol.find()

    return all_groceries 


def main():
    """
    Let's get this bread (or other grocery item)
    """
    parser = argparse.ArgumentParser(description='Document grocery list.')
    parser.add_argument('--add-grocery', dest='grocery', nargs='?', type=str,
                        help='a COOL grocery name')
    parser.add_argument('--get-all', dest='get_all', action='store_true',
                        help='list all cool grocery names')

    args = parser.parse_args()

    if args.grocery:
        print(add_new_grocery(args.grocery))

    if args.get_all:
        print(get_all_groceries())


if __name__ == "__main__":
    main()
