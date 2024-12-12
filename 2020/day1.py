# Day  1

# test = [1721,
# 979,
# 366,
# 299,
# 675,
# 1456]
p1 = 0
p2 = 0
f = open("day1_input.txt", "r")
lines = f.read()
x = lines.split('\n')
test = [int(i) for i in x]
print(test)

for i in range(len(test)):
	for j in range(i+1, len(test)):
		if test[i] + test[j] == 2020:
			p1 = test[i]*test[j]
			break

for i in range(len(test)):
	for j in range(i+1, len(test)):
		for k in range(j+1, len(test)):
			if test[i] + test[j] + test[k] == 2020:
				p2 = test[i]*test[j]*test[k]
				break

print("Part1 : {}".format(p1))
print("Part2 : {}".format(p2))
