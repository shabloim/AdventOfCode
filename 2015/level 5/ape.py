with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

def part1():
    vowels = "aeiou"
    exclude = ["ab", "cd", "pq", "xy"]
    result_list = []
    res1 = [] # this is a list with atleast one letter appearing twice
    res2 = [] # list with atlest 3 vowels
    res3 = [] # list of strings that does not contain exclude strings within 


    # find strings that do not contain exclude strings
    for i in lines:
        if not any(excl in i for excl in exclude):
            res3.append(i)

    print(f"input length before exclusion: {len(lines)}")
    print(f"length of strings that does not contain exclude strings within: {len(res3)}")


    # finding strings that have atleast one letter appear twice
    for i in lines:
        for j in range(len(i) - 1):
            if i[j] == i[j+1]:
                res1.append(i)
                break
    print(f"number of strings with atleast one letter appearing twice: {len(res1)}")

    # strings with atleast 3 vowels
    for i in lines:
        count = 0
        for char in i:
            if char in vowels:
                count += 1
            if count >= 3:
                res2.append(i)
                break
    print(f"number of strings with atleast 3 vowels: {len(res2)}")               

    nice_string = [s for s in res3 if s in res1 and s in res2]

    print(f"Part1 nice strings: {len(nice_string)}")

part1()

def part2():
    nice = []
    res1 = []
    res2 = []
    for i in lines:
        pairs = []
        for j in range(len(i) - 1):
            if j is not len(i) - 2 and i[j] == i[j+1] and i[j+1] == i[j+2]:
                continue
            pairs.append(i[j:j+2])

        occurences = {}
        for item in pairs:
            if item in occurences:
                occurences[item] += 1
            else:
                occurences[item] = 1


        def occ(string):    
            for key, value in occurences.items():
                if value >= 2:
                    res1.append(i)
                    # print(res1)
                    return True

        # this gives at least one letter which repeats with exactly one letter between them 
        def bet(string):
            for j in range(len(i) - 1):
                if j is not len(i) - 2 and i[j] == i[j+2]:
                    res2.append(i)
                    # print(res2)
                    return True


    # print(res1, res2)
        if bet(i) is True and occ(i) is True:
            nice.append(i)
    print(f"Part2 nice strings: {len(nice)}")
part2()