# TIC TAC TOE 

## CONSTANTS

```python
font_X_or_O=("Script MT",38,"bold")
bg_sudoku="#1ABC9C"
```
## FUNCTIONS
```python
board={1:" ", 2:" ", 3:" ",
       4:" ", 5:" ", 6:" ",
       7:" ", 8:" ", 9:" "}

turn="X"

def checkforwin(player):
    # Horizontal Match
    if board[1]==board[2] and board[2]==board[3] and board[3]==player:
        return True
    
    elif board[4]==board[5] and board[5]==board[6] and board[6]==player:
        return True
    
    elif board[7]==board[8] and board[8]==board[9] and board[9]==player:
        return True
    
    #Vertical Match
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player:
        return True
    
    elif board[2]==board[5] and board[5]==board[8] and board[8]==player:
        return True
    
    elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
        return True
    
    #Diagonal Match
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player:
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
        return True

def play(event):
    global turn
    button=event.widget

    button_text=str(button)
    click=button_text[-1]
    if click=="n":
        click=1
    else:
        click=int(click)
        
    if button["text"]==" ":
        if turn=="X":
            button["text"]= "X"
            board[click]=turn
            if checkforwin(turn):
                print(f"{turn}'s win the Game")
                print("game over")
            turn="O"              
        else:
            button["text"]= "O"
            board[click]=turn
            if checkforwin(turn):
                print(f"{turn}'s win the Game")
                print("game over")
            turn="X"
    print(board)          
    
```

## MAIN
```python
from tkinter import *
from functions import *
from constants import *

root=Tk()
root.geometry("350x440")
# root.resizable(False,False)
root.configure(bg="orange")
root.title("TIC TAC TOE")

frame1=Frame(root).pack()

Titlelabel=Label(frame1, text="Tic Tac Toe", font=("Areal",34,"bold"), fg="black", bg="orange").pack()

turns=Label(frame1, text=f"{turn}'s Turn", font=("Areal",20,"bold"), fg="black", bg=bg_sudoku).pack()

frame2=Frame(root)
frame2.pack()


button1=Button(frame2, text=" ", width=3, height=1, bg=bg_sudoku, font=font_X_or_O, border=3, relief="raised")
button1.grid(row=0, column=0)
button1.bind("<Button-1>", play)
button1=Button(frame2, text=" ", width=3, height=1, bg=bg_sudoku, font=font_X_or_O, border=3, relief="raised")
button1.grid(row=0, column=1)
button1.bind("<Button-1>", play)
button1=Button(frame2, text=" ", width=3, height=1, bg=bg_sudoku, font=font_X_or_O, border=3, relief="raised")
button1.grid(row=0, column=2)
button1.bind("<Button-1>", play)

button1=Button(frame2, text=" ", width=3, height=1, bg=bg_sudoku, font=font_X_or_O, border=3, relief="raised")
button1.grid(row=1, column=0)
button1.bind("<Button-1>", play)
button1=Button(frame2, text=" ", width=3, height=1, bg=bg_sudoku, font=font_X_or_O, border=3, relief="raised")
button1.grid(row=1, column=1)
button1.bind("<Button-1>", play)
button1=Button(frame2, text=" ", width=3, height=1, bg=bg_sudoku, font=font_X_or_O, border=3, relief="raised")
button1.grid(row=1, column=2)
button1.bind("<Button-1>", play)

button1=Button(frame2, text=" ", width=3, height=1, bg=bg_sudoku, font=font_X_or_O, border=3, relief="raised")
button1.grid(row=2, column=0)
button1.bind("<Button-1>", play)
button1=Button(frame2, text=" ", width=3, height=1, bg=bg_sudoku, font=font_X_or_O, border=3, relief="raised")
button1.grid(row=2, column=1)
button1.bind("<Button-1>", play)
button1=Button(frame2, text=" ", width=3, height=1, bg=bg_sudoku, font=font_X_or_O, border=3, relief="raised")
button1.grid(row=2, column=2)
button1.bind("<Button-1>", play)

root.mainloop()
```
