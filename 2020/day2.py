import re

f = open("day2_input.txt", "r")
lines = f.read()
lines = lines.split('\n')
# test = [1-3 a: abcde,
# 1-3 b: cdefg,
# 2-9 c: ccccccccc]
valid_passwords = []
for i in lines:

	key , value = i.split(": ")
	# print(key,value)
	# print(key)
	atleast, atmost = key.split(" ")[0].split("-")
	character = key.split(" ")[1]
	password = value
	#print(atleast, atmost, character, password)
	count = 0
	for i in password:
		if i == character:
			count+=1
	if count >= int(atleast) and count <= int(atmost):
		valid_passwords.append(password)
		
p2 = []
pos1 = atleast
pos2 = atmost
for i in lines:
	count = 0
	if password[int(pos1)-1] == character:
		count += 1
	if password[int(pos2)-1] == character:
		count += 1
	if count == 1:
		p2.append(password)


print("Part 1 : {}".format(len(valid_passwords)))
print("Part 2 : {}".format(len(p2)))