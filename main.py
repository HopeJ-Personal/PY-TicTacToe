# Primary Dependencies
import sys
import os

# Set Library Path
library_path = os.path.abspath(f'{os.getcwd()}/library')
sys.path.insert(0, library_path) 

# Secondary Dependencies
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