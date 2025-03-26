#!/usr/bin/env python3

import sys
import pandas as pd

column_dtype = {
  'title': 'string',
  'author': 'string',
  'isbn': 'string',
  'year': 'string'
}
column_names = list(column_dtype.keys())

books = pd.DataFrame()
new_item = pd.DataFrame()

# library data file read
def read_data_file():
  try:
    global books
    books = pd.read_csv(library_data_file, sep='/', header=None, names=column_names, dtype=column_dtype)

    # remove unnecessary index number which would be printed for every book
    blank_indexes = [''] * len(books)
    books.index = blank_indexes

  except FileNotFoundError:
    print("No such file:", library_data_file)
    sys.exit(2)

# menu
def menu():
  print("----------------")
  print("Main menu:")
  print(" 1) Add new book")
  print(" 2) List books")
  print(" Q) Quit")
  handle_choice()

def handle_choice():
  choice = input("Your choice:")

  # choice handling
  if choice == "1":
    print("Adding new book")
    new_book = ask_for_book_data()
    display_new_book(new_book)
    ask_to_update_file(new_book)
  elif choice == "2":
    list_books()
  elif choice == "Q" or choice == 'q':
    print("Bye.")
    sys.exit(0)
  else:
    print("Bad choice:", choice)
    handle_choice()

# new book data
def ask_for_book_data():
  print("New book")
  title = input("title:")
  author = input("author:")
  isbn = input("isbn:")
  year = input("year:")
  new_item = pd.DataFrame([[title, author, isbn, year]], columns=column_names, dtype='string')
  new_item.index = ['']
  return(new_item)

def display_new_book(item):
  print(item)

def ask_to_update_file(new_item):
  update_yes = input("Do you want to update data file? Enter Y to update, N to not:")
  if update_yes == 'Y':
    global books
    books = pd.concat([books, new_item], ignore_index=True)
    books = books.sort_values(by='year')
    blank_indexes = [''] * len(books)
    books.index = blank_indexes
    books.to_csv(library_data_file, sep='/', index=False, header=None)
  elif update_yes == 'N':
    print("Not updating the data file then.")
  else:
    print("No such option here:", update_yes)
    ask_to_update_file(new_item)

  menu()

def list_books():
  print('')

  # handle special case: empty file
  if len(books) == 0:
    print("No books yet.")
  else:
    print(books)

  print('')

  menu()


# ---------------------------------------
# main program

# check command line argument was given
if len(sys.argv) < 2:
  print("Missing argument: filename")
  sys.exit(1)

library_data_file = sys.argv[1]
read_data_file()
menu()
