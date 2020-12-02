import math

data = open("Day_01a_input", "r")
line_array = []
lines = data.read().splitlines()

for line in lines :
    line_array.append(int(line))
data.close()

line_array.sort()
l = len(line_array)

# Part 1
i = 0
while line_array[i] <=2020 and i < l-1 :
    j = 0
    while line_array[j] <=2020-line_array[i] and j < l-1 :
        if line_array[i] +line_array[j]  == 2020 :
            print(f"{line_array[i]}*{line_array[j]}={line_array[i] *line_array[j]}")
        j = j + 1
    i = i + 1

# Part 2
counter = 0
i = 0
while line_array[i] <=2020 and i < l-1 :
    j = i+1
    while line_array[j] <=2020-line_array[i] and j < l :
        k = j+1
        while line_array[k] <= 2020 - line_array[i] - line_array[j] and k < l :
            counter = counter+1
            if line_array[i] +line_array[j] +line_array[k]  == 2020 :
                print(f"{line_array[i]}*{line_array[j]}*{line_array[k]}={ line_array[i] *line_array[j] *line_array[k] }")
            k = k + 1
        j = j + 1
    i = i + 1

print(counter)

