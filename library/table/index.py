print("index for table")

# example from my external border thingy just so i remember how
class border_class:
    def create():
        print("test")
    
    def test(self, param):
        print(f"test subcommand ran with {param}")
    
    def set(self, param):
        print("test")
    
    def style(self, param):
        print("test")

class table_class:
    def test():
        print("test")
    def generate1(width, height, top, left, bottom, right, cell_width, cell_strings):
            # t = "ABC"
            # l = "123"
            # b = ""
            # l = ""
            # strings = "xy","zo"
            # Example table.generate(3, 3, t, l, b, r, 1, strings)
            # > |   | A | B | C |
            # > | 1 |
            print("test")
    def generate(horizontal, vertical, cell_width, input_width, padding, string, highlight_cells=None, highlight_color=GREEN):
        #
        # horizontal: Number of columns
        # vertical: Number of rows
        # cell_width: Character width inside each cell
        # input_width: How many characters to split from the string before putting in cells
        # padding: Spaces on each side of the text
        # string: Text to display
        # highlight_cells: List of (row, col)
        # highlight_color: Color
        
        # Future highlighting idea, idk
        #   - Optional Parameter support
        if highlight_cells is None:
            highlight_cells = []
        
        # Split Text
        #   * string="xxooxx", input_width=2 ---> ["xx","oo","xx"]
        chunks = textwrap.wrap(string, width=input_width)
        # printing to see progress live
        print(chunks)