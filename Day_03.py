def txt_to_list(filename) :
    my_list = []
    for line in open(filename) :
        if len(line) > 0 and line[-1] == '\n' :
            line = line[:-1]
        my_list.append(line)
    return my_list

map = txt_to_list("Day_03_input")


# Part 1
height = len(map)
width = len(map[0])
i = 0
j = 0
counter = 0
for i in range(height-1) :
    i = i + 1
    j = (j + 3) % width
    if map[i][j]=='#' :
        counter = counter + 1

print(counter)

# Part 2


def trees(a,b) :
    counter = 0
    x , y = a , b
    while x < height :
        if map[x][y]=='#' :
            counter = counter + 1
        x = x + a
        y = (y + b) % width
    return(counter)

print(trees(1,1)*trees(1,3)*trees(1,5)*trees(1,7)*trees(2,1))