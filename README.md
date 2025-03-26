# TASK

Create a database program that store books and takes a file as the first command line
argument.
E.g.
`python my_library_db.py library.txt`

The file contains rows, which each keep information of name of book, name of the writer, ISBN
and publishing year.
E.g.

```
Idiot/Fyodor Dostoyevsky/9780850670356/1971
Moby Dick/Herman Melville/9781974305032/1981
```

After reading the file, program shows UI, where is option to 
```
1) Add new book, 
2) Print current database content in ascending order by publishing year or
Q) Exit the program
```

With first option program should ask user the book’s name, writer’s name, book’s ISBN and publishing year.
Then show the results to user and ask, does user want to update the database.
If user selects to update the database program should add the new book’s information into file given as command line input argument.
And otherwise return to main menu.

The Input file should be kept in numerical order based on publishing year.
Also if user choose to print current database content, program should print out to screen all information from database, old and new information.

The visual user interface or printing out the database can be freely chosen, but should be human readable format (new line feeds and some kind of separators are recommended).

# Program
