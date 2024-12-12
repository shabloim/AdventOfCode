with open('input.txt', 'r') as file:
    content = file.read() # Reads the entire file
print(content)


def part1(directions):
    # location array = [N, E, S, W]
    # north (^), south (v), east (>), or west (<)
    # location needs current coordinates and destination coordinates
    """
    (x, y) cordinates
    if ^ is seen it means the starting coordinates are (0, 0) and destination coordinates are (0, 1)
    now to track if the house has been visited in a coordinate we need dictionary
    Everytime a new coordinate is visited it will be added to the dictionary, if visited again we can just pass without adding it in

    """
    house_visited = [[0,0]]
    directions = [char for char in directions] # each item in list is a direction
    x = 0
    y = 0
    for i in directions:
        if i == "^": # north
            y += 1
        elif i == ">": # east
            x += 1
        elif i == "v": # south
            y -= 1
        else: # west
            x -= 1
        if (x, y) not in house_visited:
            house_visited.append([x, y])

    unique_homes = [list(x) for x in set(tuple(x) for x in house_visited)]
    print(len(unique_homes))
part1(content)


def part2(directions):
    # santa and robo-santa
    santa_directions = [i for i in directions[::2]]
    robo_santa = [i for i in directions[1::2]]
    # print(santa_directions)
    santa_house_visited = [[0,0]]
    robo_santa_house_visited = [[0,0]]
    """
    starts with santa so if the index of the direction string is odd then add coordinate
    to santa list and if it is even then add coordinate to robo-santa list

    x,y for santa
    a,b for robo-santa
    """
    a = 0
    b = 0
    x = 0
    y = 0
    index = 0 # to denote whose turn it is to hear elf and give out present, if odd then santa goes and if even robo-santa goes
    for i in directions:
        if index%2 == 0:
            if i == "^": # north
                b += 1
            elif i == ">": # east
                a += 1
            elif i == "v": # south
                b -= 1
            else: # west
                a -= 1
            robo_santa_house_visited.append([a,b])
        else:
            if i == "^": # north
                y += 1
            elif i == ">": # east
                x += 1
            elif i == "v": # south
                y -= 1
            else: # west
                x -= 1
            santa_house_visited.append([x,y])
        index += 1

    all_homes = santa_house_visited + robo_santa_house_visited
    unique_homes = [list(x) for x in set(tuple(x) for x in all_homes)]
    print(len(unique_homes))
part2(content)