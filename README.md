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
    - author
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

-----
# Afterthought

What I got was a refreshing dive into plain-old Python and Pandas. Along the way I was grateful for my choice of technology stack, as Pandas silently tackled many potential problems regarding data handling.

The task was designed so that I had freedom to succeed with tools I wanted. I chose Python and Pandas and considered Textual for programming the user interface. A TUI library would've been an overkill here as everything could be handled with Python's input().

My first task was to just list the books. I didn't get into the UI part because I needed to re-master Pandas after some time. This kept me out the UI bubble and made me aware of potential problems regarding data files and program execution. I temporarily added functionality to add a book using a command line argument, which showcased potential problems with year column. Eventually I chose to treat all columns as strings.
