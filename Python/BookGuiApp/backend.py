import sqlite3

def connectDatabase():
    connection = sqlite3.connect('Books.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
    connection.commit()
    connection.close()

def insertValues(title, author, year, isbn):
    connection = sqlite3.connect('Books.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES (NULL, ?,?,?,?)', (title, author, year, isbn))
    connection.commit()
    connection.close()


def viewValues():
    connection = sqlite3.connect('Books.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    connection.close()
    return rows

def search(title = "", author = "", year = "", isbn = ""):
    connection = sqlite3.connect('Books.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?', (title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows

def deleteValues(id):
    connection = sqlite3.connect('Books.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?',(id,))
    connection.commit()
    connection.close()

def updateValues(id, title, author, year, isbn):
    connection = sqlite3.connect('Books.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?',(title,author,year,isbn,id))
    connection.commit()
    connection.close()


connectDatabase()
# insertValues('sun', "leo", 2004, 2024202)
# updateValues(1, 'moon', 'leo', 2002, 20020202)
# deleteValues(4)
# print(search(author = "leo"))

#print(viewValues())
