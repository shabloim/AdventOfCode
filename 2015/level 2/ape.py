with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]  # Returns a list of lines

dimensions = []
for i in lines:
    dimensions.append(list(map(int, i.split("x"))))

# def part1(dim):
#     total = 0
#     for i in dim:
#         l = i[0]
#         w = i[1]
#         h = i[2]
#         slack = min(l*w, w*h, h*l)
#         paper = 2*l*w + 2*w*h + 2*h*l
#         total += paper + slack
#         # print(i, slack, paper, total)
#     print(total)
# part1(dimensions)

def part2(dim):
    total = 0
    for i in dim:
        i = sorted(i)
        perimeter = 2*i[0] + 2*i[1]
        vol = i[0] * i[1] * i[2]
        # print(i, perimeter)
        total += (vol + perimeter)
    print(total)
part2(dimensions)