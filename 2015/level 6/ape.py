with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

switch_positions = ["turn on ", "turn off ", "toggle "]

"""
need to create action and coordinate:
action: turn on, turn off, toggle
coordinate: (0,0), (999, 999) {start and destination}
"""


# print(lines)
new_lines = []
for i in lines:
    for substring in switch_positions:
        if substring in i:
            end_pos = 0 + len(substring)
            action = i[:end_pos-1]
            cors = i[end_pos:]
            start, dest = cors.split(" through ")
            x1, y1 = start.split(",")
            x2, y2 = dest.split(",")
            # print(f"action: {action}, start cors: {x1, y1} and dest cors: {x2, y2}")
            new_lines.append([action, [x1, y1], [x2, y2]])

# print(new_lines)


"""
new new_lines list contains lists which contain action, starting coordinates and destination coordinates
like so: [['turn on', ['0', '0'], ['999', '999']], ['toggle', ['0', '0'], ['999', '0']], ['turn off', ['499', '499'], ['500', '500']]]
hopefully this makes it easier to navigate 
"""

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for i in new_lines:
    action = i[0]
    x1 = int(i[1][0])
    y1 = int(i[1][1])
    x2 = int(i[2][0])
    y2 = int(i[2][1])

    # x1, x2 = min(x1, x2), max(x1, x2)
    # y1, y2 = min(y1, y2), max(y1, y2)
    if action == "turn on":
        # print(action, (x1, y1), (x2, y2))
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                grid[i][j] = 1
    elif action == "toggle":
        # print(action, (x1, y1), (x2, y2))
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                grid[i][j] ^= 1
    elif action == "turn off":
        # print(action, (x1, y1), (x2, y2))
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                grid[i][j] = 0
lit = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            lit += 1
print(f"number of lights lit: {lit}")
