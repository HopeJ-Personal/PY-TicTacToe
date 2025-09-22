horizontal = 3
padding = 1
cell_width = 2

parts = []
for _ in range(horizontal):
    parts.append("-" * (cell_width + 2 * padding))
line = "+" + "+".join(parts) + "+"

print(parts)
print(line)