Assignment is on the [Task page](Task.md).

-----

# Library management program

## Requirements
To run, you need Python 3. The program uses `pandas` library. See [requirements.txt](requirements.txt) for all dependencies (only pandas at the moment).

The program was developed on Linux. If you're having problems running it on Windows, first things to check are line feed characters and character set settings.

## Usage
Start the program with command:
```
python3 my_library.py library.txt
```

# Features

## Basic functionality
In the program Main menu user can choose from 3 options
* Add new book
  * User will be asked for data of the new book:
    - title
    - name
    - ISBN
    - year
  * Book entry will be shown
  * User must choose if they want to update the database with the new data
* List books
  * Books are sorted by year
* Quit


## Some error handling and special cases
* If no argument is given, program reports "Missing argument: filename" and quits
* If the file given as an argument can't be found, program reports "No such file" and quits
* In case of an empty library data file, program reports "No books yet" instead of Pandas library "Empty dataframe" output
  * Try with `python3 my_library.py empty.txt`
