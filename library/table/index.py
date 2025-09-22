## Usefull Links:
# JSON Formatter: https://jsonformatter.com/
# UUID V4 Generator: https://www.uuidtools.com/v4
print("index for tables")

import sys
import os
import textwrap
class table_class:
    #def test():
    #def test(self, param):
    def test(param):
        print(f"test subcommand ran with {param}")
        print("this is a test message inside of the index.py of the 'Table library")

    def generate(horizontal, vertical, cell_width, input_width, padding, string):
        # Step 1: Prepare the string and chunks
        # Split string into pieces (chunks), that each are up to {input_width} characters long
        chunks = textwrap.wrap(string, width=input_width) # type: ignore
        while len(chunks) < (horizontal * vertical):
            chunks.append(" " * input_width)
        
        # Debugging Print: Print the chunks after initial wrapping
        print(f"Chunks after initial wrapping:\n{chunks}\n")
        
        # Step 2: Padding empty cells



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