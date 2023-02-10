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

        
