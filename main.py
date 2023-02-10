# Name: Jerico James F. Viteño
# Final Project: Sodoku Solver
# February 18, 2023

from collections import deque
import tkinter

root = tkinter.Tk
root.title("SodokuSolver")

class Solver:
    def __init__(self, master):
        
        # Initializing Objects
        self.cells = {}
        self.entries = []

        for row in range(1, 10):
            for column in range (1, 10):
                if ((row in (1,2,3,7,8,9) and column in (4,5,6)) or (row in (4,5,6) and column in (1,2,3,7,8,9))):
                    color='gray20'
                else:
                    color='gray80'
                cell = tkinter.Frame(master, highlightbackground=color, highlightcolor=color, highlightthickness=2, width=50, height=50, padx=3,  pady=3, background='black')
                cell.grid(row=row, column=column)
                self.cells[(row, column)] = cell

                e = tkinter.Entry(self.cells[row, column], justify='center')
                e.place(height=40, width=40)
                
                self.entries.append(e)

        # Creates buttons 
        topFrame = tkinter.Frame(master)
        topFrame2 = tkinter.Frame(master)
        topFrame3 = tkinter.Frame(master)

        solveButton = tkinter.Button(topFrame, text="SOLVE", command=self.solve)
        solveButton.pack()
        
        visualButton = tkinter.Button(topFrame2, text="VISUAL", command=self.visualbacktrack)
        visualButton.pack()

        resetButton = tkinter.Button(topFrame3, text="CLEAR", command=self.reset)
        resetButton.pack()
   
