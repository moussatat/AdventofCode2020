def txt_to_list(filename) :
    my_list = []
    for line in open(filename) :
        if len(line) > 0 and line[-1] == '\n' :
            line = line[:-1]
        my_list.append(line)
    return my_list

passwords = txt_to_list("Day_02_input")

# Part 1
counter = 0
for mot in passwords :
    splitpass = mot.replace("-", " ").replace(":","").split()
    low = int(splitpass[0])
    high = int(splitpass[1])
    word = list(splitpass[3])
    count = word.count(splitpass[2])
    if low <= count <= high :
        counter = counter + 1
print(counter)


# Part 2
counter = 0
for mot in passwords :
    splitpass = mot.replace("-", " ").replace(":","").split()
    first = int(splitpass[0])
    second = int(splitpass[1])
    word = list(splitpass[3])
    if (word[first-1]==splitpass[2]) != (word[second-1]==splitpass[2]) :
        counter = counter + 1

print(counter)