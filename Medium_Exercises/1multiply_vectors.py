x = [2, 4, 5]
y = [2, 3, 6]

i = 0
vector_sum = []
while i < len(x):
    vector_sum[i] = x[i] * y[i]
    i += 1
print(vector_sum)