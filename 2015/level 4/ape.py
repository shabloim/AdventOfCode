import hashlib


with open('input.txt', 'r') as file:
    secret = file.read()
print(f"given secret: {secret}")

# part 1
def part1():
    target_zeros = 5
    number = 0  
    while True:
        combined = secret + str(number)
        byte_string = combined.encode('utf-8')
        result = hashlib.md5(byte_string).hexdigest()

        if result.startswith('0' * target_zeros):
            print(f"Part1 Found number: {number}")
            print(f"Part1 Hash: {result}")
            break
        number += 1
part1()

# part2 
def part2():
    target_zeros = 6
    number = 0
    while True:
        combined = secret + str(number)
        byte_string = combined.encode('utf-8')
        result = hashlib.md5(byte_string).hexdigest()

        if result.startswith('0' * target_zeros):
            print(f"Part2 Found number: {number}")
            print(f"Part2 Hash: {result}")
            break
        number += 1
part2()