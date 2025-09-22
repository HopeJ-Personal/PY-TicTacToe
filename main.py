# Primary Dependencies
import sys
import os

# Set Library Path
library_path = os.path.abspath(f'{os.getcwd()}/library')
sys.path.insert(0, library_path) 

# Secondary Dependencies
import lib_loader # pyright: ignore[reportMissingImports]

# Load the libraries
lib_loader.libraryhandler()
from lib_loader import * # pyright: ignore[reportMissingImports]

# shortcuts
util = util_class # pyright: ignore[reportUndefinedVariable]
table = table_class # pyright: ignore[reportUndefinedVariable]

# Main Code

#util.test()
#util.clear()

print("Welcome to tictactoe")
table.test("abc")
#table.generate_table(3, 3)
#table.generate_table(3, 3, 10, 5, 1, "This is a sample string to demonstrate the table generation functionality.")
#table.generate(3,2)
#table.generate(3, 3, 2, 2, 1, "xoooxooox")
#ico_x = "x   x  x  x   x"
#ico_o = "  o  o   o  o  "

#ico_x = '\\   /  x  /   \\'
#ico_x = '╲  /  x  /  ╲'
#ico_x = "╔═╗║  ║╚═══╝"

#x   x  x  x   x
#  o  o   o  o  
#table.generate(4, 4, 5, 15, 1, f"{ico_x}{ico_o}{ico_x}{ico_x}{ico_o}{ico_o}{ico_o}{ico_o}{ico_o}{ico_o}{ico_x}{ico_x}")
#table.generate(3, 3, 5, 15, 1, f"{ico_x}{ico_o}{ico_x}{ico_x}{ico_o}{ico_o}{ico_o}{ico_o}{ico_o}")
#{ico_x}

ico_x = "\\ / x / \\"
ico_o = "╔═╗║ ║╚═╝"
table.generate(3, 3, 3, 9, 1, f"{ico_x}{ico_o}{ico_x}{ico_x}{ico_o}{ico_o}{ico_o}{ico_o}{ico_o}")
table.generate(3, 3, 3, 9, 1, f"{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}")

ico_x = "\\   /  x  /   \\"
ico_o = "╔═══╗║   ║╚═══╝"
table.generate(3, 3, 5, 15, 1, f"{ico_x}{ico_o}{ico_x}{ico_x}{ico_o}{ico_o}{ico_o}{ico_o}{ico_o}")
table.generate(3, 3, 5, 15, 1, f"{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}")

ico_x = "x"
ico_o = "o"
table.generate(3, 3, 1, 1, 1, f"{ico_x}{ico_o}{ico_x}{ico_x}{ico_o}{ico_o}{ico_o}{ico_o}{ico_o}")
table.generate(3, 3, 1, 1, 1, f"{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}{ico_x}")

# ico_x = "\\   /  x  /   \\"
# \   /
#   x  
# /   \

# ico_o = "╔═══╗║   ║╚═══╝"
# ╔═══╗
# ║   ║
# ╚═══╝