## Usefull Links:
# JSON Formatter: https://jsonformatter.com/
# UUID V4 Generator: https://www.uuidtools.com/v4
print("index for utilities")

import sys
import os

class util_class:
    # Utilities: Screen
    def clear():
        # Check if the operating system is Windows ('nt')
        if os.name == 'nt':
            _ = os.system('cls')  # Use 'cls' for Windows
        else:
            _ = os.system('clear') # Use 'clear' for Linux/macOS
    def test():
        print("this is a test message inside of the index.py of the utilities library")
    def test(param):
        print(f"test subcommand ran with {param}")
        print("this is a test message inside of the index.py of the 'Table library")
        print(f"")

This is a test function, declared as {self}, under the parent {parent}
This test function was declared inside of {file} of the {library} library
        library = "'utilities'"
        path = "'library/utilities/index.py'"
        file = "index.py"
        parent = "'class util_class'"
        self = "'def test(param)'"
        child = "'None'"
        function = "    This is a test function, declared as {self}, under the parent {parent}\n    This test function was declared inside of {file} of the {library} library"
    
    # Utilities: Timer
    #def timer_start():
    #def timer_end()
    #def timer_calculate()
    
    # Utilities: Validation
    #def validate_file():
    #def validate_folder():
    #def validate_input():
    #def validate_length
    #def validate_output():
    

    This is a test function, declared as {self}, under the parent {parent}\n    This test function was declared inside of {file} of the {library} library
    {library}\n    Parent: {parent}\n    Self: {self}\n    Child: {child}
\n    Function:
\n        {function}
#Parent: 'class util_class'
#Self: 'def test(param)'
#Child: 'None'
#Function:
#Print out message to terminal with whatever you inputed for your parameter
#Print out information about the function, parent/class, self/function, child/sub_functions, etc. (This message)