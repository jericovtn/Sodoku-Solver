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

        # Grids
        topFrame.grid(column=5, row=0)
        topFrame2.grid(column=4, row=0)
        topFrame3.grid(column=6, row=0)

    # Converts user input into an array
    def turnToList(self):
        outputList = []

        for row in range(9):
            nestedList = []
            for column in range(9):
                if self.entries[column + (row * 9)].get() == "":
                    nestedList.append(0)
                else:
                    nestedList.append(int(self.entries[column + (row * 9)].get()))
            outputList.append(nestedList)

        return outputList   

    # Backtracking
    def pickEmpty(self, inputBoard, vis):
        self.stack = deque()
        rowIndex = 0
        columnIndex = 0

        while rowIndex < 9:
            columnIndex = 0

            while columnIndex < 9:
                if inputBoard[rowIndex][columnIndex] == 0:
                    
                    #Trys to input num from 1-9
                    index = self.trynum([rowIndex, columnIndex], 1, inputBoard, vis)
                    
                    rowIndex = index[0]
                    columnIndex = index[1]

                columnIndex += 1
            rowIndex += 1

    # If number does not exist in row, column, or square
    def validInput(self, number, boardInput, indexes):
        if (not self.inColumn(number, boardInput, indexes) and not self.inRow(number, boardInput, indexes) and not self.inSquare(number, boardInput, indexes)):
            return True
        return False

    # HELPER FUNCTIONS FOR validInput

    # If number exists in its row
    def inRow(self, number, boardInput, indexes):
        for num in boardInput[indexes[0]]:
            if number == num:
                return True
        return False

    # If number exists in its column
    def inColumn(self, number, boardInput, indexes):
        for row in boardInput:
            if row[indexes[1]] == number:
                return True
        return False 