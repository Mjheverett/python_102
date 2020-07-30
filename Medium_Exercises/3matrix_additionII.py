x = [[1, 3], [2, 4]]
y = [[5, 2], [1, 0]]
new_list = [[],[]]

for i in range (len(x)):
    for j in range (len(x[i])):
        new_list[i].append(x[i][j] + y[i][j])
print(new_list)