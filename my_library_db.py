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
new_item = pd.DataFrame()
update_file = False

# check command line argument was given
if len(sys.argv) < 2:
  print("Missing argument: filename")
  sys.exit(1)

# command line book adding (temporary)
if len(sys.argv) > 2:
  given_item = sys.argv[2].split('/')
  new_item = pd.DataFrame([given_item], columns=column_names, dtype='string')
  print("New book:\n", new_item)

# command line file updating (temporary)
if len(sys.argv) > 3:
  if sys.argv[3] == 'update_file':
    update_file = True

# read text file
library_file = sys.argv[1]

try:
  # books = pd.read_csv(library_file, sep = '/', header=None, names=['title', 'author', 'isbn', 'year'])
  books = pd.read_csv(library_file, sep='/', header=None, names=column_names, dtype=column_dtype)
except FileNotFoundError:
  print("No such file:", library_file)
  sys.exit(2)

if len(new_item) > 0:
  books = pd.concat([books, new_item], ignore_index=True)
  books = books.sort_values(by='year')

if update_file:
  books.to_csv(library_file, sep='/', index=False, header=None)

# handle special case: empty file
if len(books) == 0:
  print("No books yet.")
else:
  print(books)
