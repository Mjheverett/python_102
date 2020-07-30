x = [[1, 3], [2, 4]]
y = [[5, 2], [1, 0]]
new_list = [[0,0],[0,0]]

for i in range (len(x)):
    for j in range (len(x[i])):
        new_list[i][j] = x[i][j] + y[i][j]
print(new_list)