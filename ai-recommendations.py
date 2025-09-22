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