# Primary Dependencies
import sys
import os

# Set Library Path
library_path = os.path.abspath(f'{os.getcwd()}/library')
sys.path.insert(0, library_path) 

# Secondary Dependencies
import textwrap
import lib_loader

# Load the libraries
lib_loader.libraryhandler()
from lib_loader import *

# shortcuts
util = util_class
table = table_class

# Main Code

#util.test()
#util.clear()

print("Welcome to tictactoe")
table.test("abc")
#table.generate_table(3, 3)
#table.generate_table(3, 3, 10, 5, 1, "This is a sample string to demonstrate the table generation functionality.")
#table.generate(3,2)
table.generate(3, 3, 2, 2, 1, "xoooxooox")
