from tkinter import *
import backend

app = Tk()

def getSelected(event):
    
    try: 
        global selectedRow

        index = outputArea.curselection()[0]
        selectedRow = outputArea.get(index)
        
        titleInput.delete(0, END)
        titleInput.insert(END,selectedRow[1])

        authorInput.delete(0, END)
        authorInput.insert(END,selectedRow[2])

        yearInput.delete(0, END)
        yearInput.insert(END,selectedRow[3])

        isbnInput.delete(0, END)
        isbnInput.insert(END,selectedRow[4])
    
    except IndexError:
        pass
   

def viewCommand():
    
    outputArea.delete(0, END)

    for row in backend.viewValues():
        outputArea.insert(END, row)


def searchCommand(title = "", author = "", year = "", isbn = ""):
    
    outputArea.delete(0, END)

    for row in backend.search(titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get()):
        outputArea.insert(END, row)

def addCommand():

    backend.insertValues(titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())
    outputArea.delete(0, END)
    outputArea.insert(END, (titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get()))


def updateCommand():
    backend.updateValues(selectedRow[0], titleValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())

def deleteCommand():
    backend.deleteValues(selectedRow[0])


''' Título App '''
app.wm_title('BookStore')
    

''' Botões '''
viewButton = Button(app, text = 'View All', width = 12, command = viewCommand)
viewButton.grid(row = 2, column = 3)

searchButton = Button(app, text = 'Search Entry', width = 12, command = searchCommand)
searchButton.grid(row = 3, column = 3)

addButton = Button(app, text = 'Add Entry', width = 12, command = addCommand)
addButton.grid(row = 4, column = 3)

updateButton = Button(app, text = 'Update Selected', width = 12, command = updateCommand)
updateButton.grid(row = 5, column = 3)

deleteButton = Button(app, text = 'Delete Selected', width = 12, command = deleteCommand)
deleteButton.grid(row = 6, column = 3)

closeButton = Button(app, text = 'Close', width = 12, command = app.destroy)
closeButton.grid(row = 7, column = 3)

''' Input '''
titleValue = StringVar()
titleInput = Entry(app, textvariable = titleValue)
titleInput.grid(row = 0, column = 1)

yearValue = StringVar()
yearInput = Entry(app, textvariable = yearValue)
yearInput.grid(row = 1, column = 1)

authorValue = StringVar()
authorInput = Entry(app, textvariable = authorValue)
authorInput.grid(row = 0, column = 3)

isbnValue = StringVar()
isbnInput = Entry(app, textvariable = isbnValue)
isbnInput.grid(row = 1, column = 3)

''' Output '''
outputArea = Listbox(app, width = 40, height = 10)
outputArea.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

''' Barra de rolagem/Config '''
scroll = Scrollbar(app)
scroll.grid(row = 3, column = 2, rowspan = 6)

outputArea.configure(yscrollcommand = scroll.set)
scroll.configure(command = outputArea.yview)

outputArea.bind('<<ListboxSelect>>', getSelected)

''' Títulos '''
titleLabel = Label(app, text = 'Title: ')
titleLabel.grid(row = 0, column = 0)

yearLabel = Label(app, text = 'Year: ')
yearLabel.grid(row = 1, column = 0)

authorLabel = Label(app, text = 'Author: ')
authorLabel.grid(row = 0, column = 2)

isbnLabel = Label(app, text = 'ISBN: ')
isbnLabel.grid(row = 1, column = 2)

app.mainloop()