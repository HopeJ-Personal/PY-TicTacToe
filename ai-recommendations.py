# AI Keeps spamming with recommendations which im trying to ignore but some of them are pretty good so im going to keep them here for future refrence
# I will try to keep them in this file called ai-recommendations.py

def generate_table(rows, cols):
    table = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("-")
        table.append(row)
    for row in table:
        print(" | ".join(row))
    return table

#def generate_table(variables...):
def generate_table_0():
    print("generate_table function called")
    # Placeholder implementation
    # Actual implementation would generate a table based on provided parameters

def generate_table_1(param1):
    print(f"generate_table function called with param1: {param1}")
    # Placeholder implementation
    # Actual implementation would generate a table based on provided parameters
    # This is an example of function that states a parameter of itself.

def generate_table(horizontal, vertical):
    print(f"Generating a table with {horizontal} columns and {vertical} rows.")
    table = []
    for r in range(vertical):
        row = []
        for c in range(horizontal):
            row.append("-")
        table.append(row)
    for row in table:
        print(" | ".join(row))
    return table

while len(chunks) % (horizontal * vertical) != 0:
    chunks.append("") # type: ignore

# it started generating notes for my breakddown then code so i just let it to see what it makes lol
        for row in rows:
            wrapped_cells = [textwrap.wrap(cell, width=cell_width) or [""] for cell in row]
            # [Breakdown] explanations of parts:
            # textwrap.wrap(cell, width=cell_width):
            #   This splits each cell's content into multiple lines if it exceeds cell_width.
            #   If the cell is empty, it returns an empty list, so we use "
            # or [""] to ensure there's at least one empty string for empty cells.
            max_lines = max(len(cell) for cell in wrapped_cells)
            for i in range(max_lines):
                line_parts = []
                for cell in wrapped_cells:
                    if i < len(cell):
                        content = cell[i]
                    else:
                        content = ""
                    line_parts.append(" " * padding + content.ljust(cell_width) + " " * padding)
                print("|" + "|".join(line_parts) + "|")
            print(divider())
            
            # This is a fallback to ensure that even empty cells have at least one line (an empty string).
            # This is python shorthand for "if the result of textwrap.wrap is empty, use [""] instead".
            
            # or [""]
            # This is a fallback to ensure that even empty cells have at least one line (an empty string).
            # This is python shorthand for "if the result of textwrap.wrap is empty, use [""] instead".
            # This is Python Shorthand:
            # It is a concise way to provide a default value when the primary expression evaluates to a falsy value (like an empty list).
                        # If the left side (textwrap.wrap...) is falsy (like an empty list), use the right side ([""]) instead.
