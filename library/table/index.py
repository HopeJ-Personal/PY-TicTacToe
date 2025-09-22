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
        chunks = textwrap.wrap(string, width=input_width)
        while len(chunks) < horizontal * vertical:
            chunks.append(" " * input_width)
        
        # Debugging Print: Print the chunks after initial wrapping
        #print(f"Chunks after initial wrapping:\n{chunks}\n")
        
        # Step 2: Padding empty cells
        while len(chunks) % (horizontal * vertical):
            chunks.append(" " * input_width)
        
        # Debugging Print: Print the chunks after padding
        #print(f"Chunks after padding:\n{chunks}\n")
        
        # Step 3: Reshaping chunks into rows
        rows = [chunks[i * horizontal:(i + 1) * horizontal] for i in range(vertical)]
        # [Breakdown] normal loop:
        ## for i in range(vertical):  
        ## start = i * horizontal          # where this row starts
        ## end = (i + 1) * horizontal      # where this row ends
        ## row = chunks[start:end]         # slice that part out
        ## rows.append(row)      
        
        # [Example] Input
        ## horizontal = 3
        ## vertical = 3
        ## chunks = ["a","b","c","d","e","f","g","h","i"]
        
        # [Example] [Breakdown] Iteration:
        # i = 0:
        #   start = 0, end = 3
        #   row = ["a","b","c"]
        #   rows = [["a","b","c"]]
        # i = 1:
        #   start = 3, end = 6
        #   row = ["d","e","f"]
        #   rows = [["a","b","c"], ["d","e","f"]]
        # i = 2:
        #   start = 6, end = 9
        #   row = ["g","h","i"]
        #   rows = [["a","b","c"], ["d","e","f"], ["g","h","i"]]
        
        # Step 4: Making divider lines
        def divider():
            return "+" + "+".join(["-" * (cell_width + 2 * padding) for _ in range(horizontal)]) + "+"
        
        # [Breakdown] normal loop:
        ## parts = []
        ## for _ in range(horizontal):
        ##     parts.append("-" * (cell_width + 2 * padding))
        ## line = "+" + "+".join(parts) + "+"
        
        # Step 5: Print the table
        print(divider())
        for row in rows:
            wrapped_cells = [textwrap.wrap(cell, width=cell_width) or [""] for cell in row]
            # [Breakdown] explanations of parts:
            
            # textwrap.wrap(cell, width=cell_width)
            #   This takes a string and breaks it into lines no longer than {cell_width}.
            #   [Example] [Breakdown]
            #       textwrap.wrap("hellothere", width=4)
            #       ["hell", "othe", "re"]
            
            # or [""]
            #   This is Python Shorthand:
            #   If the left side (textwrap.wrap...) returns an empty list, use the right side ([""]) instead.
            #   [Example] [Breakdown]
            #       textwrap.wrap("", width=4)  -->  []
            #       An empty list would break later code, so instead we make it a list with one empty string: [""].
            
            # for cell in row
            #   This means for each piece of text (cell) inside the current row, do something.
            #   [Example] [Breakdown]
            #       So if row = "abc", "def", "ghi"], we'll loop through "abc", "def", and "ghi".
        
            max_height = max(len(cell) for cell in wrapped_cells)
            for line_index in range(max_height):
                row_line = "|"
                for cell in wrapped_cells:
                    text = cell[line_index] if line_index < len(cell) else ""
                    row_line += " " * padding + text.ljust(cell_width) + " " * padding + "|"
                print(row_line)
            print(divider())