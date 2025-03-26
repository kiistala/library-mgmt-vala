#!/usr/bin/env python3

import sys
import pandas as pd

# check command line argument was given
if len(sys.argv) < 2:
  print("Missing argument: filename")
  sys.exit(1)

# read text file
library_file = sys.argv[1]

try:
  books = pd.read_csv(library_file, sep = '/', header=None, names=['title', 'author', 'isbn', 'year'])
except FileNotFoundError:
  print("No such file:", library_file)
  sys.exit(2)

# handle special case: empty file
if len(books) == 0:
  print("No books yet.")
else:
  print(books)
