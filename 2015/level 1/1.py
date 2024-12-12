"""
An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.


For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.

"""

with open('input.txt', 'r') as file:
    lines = file.readlines()

# part 1
# for i in lines:
#     up = 0 # "( means go up one floor"
#     down = 0 # ") means go down one floor"
#     for j in i:
#         if j == "(":
#             up += 1
#         else:
#             down -= 1

#     print(up + down)

# part 2
for i in lines:
    level = 0
    pos = 0
    for j in i:
        if j == "(":
            level += 1
            pos += 1
            if level == -1:
                print(pos)
                break
        else:
            level -= 1
            pos += 1
            if level == -1:
                print(pos)
                break
print(pos)