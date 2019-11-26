l = [['facebook', 'google', 'uber', 'apple'], ['lyft', 'airbnb', 'paypal', 'yelp']]
w = [4, 4, 3, 2]
k = 4
import math

for i in l:
    ma = -float('inf')
    for j in range(len(w)):
        ma = max(ma, math.ceil(len(i[j]) / w[j]))
    for loop in range(ma):
        s = '|'.join([i[k][loop * w[k]:(loop + 1) * w[k]] for k in range(len(i))])
        # s = '|'.join([i[k][loop * w[k]:(loop + 1) * w[k]] if len(i[k][loop * w[k]:(loop + 1) * w[k]]) == w[k] else i[k][loop * w[k]:(loop + 1) * w[k]]+' '*(w[k]-len(i[k][loop * w[k]:(loop + 1) * w[k]])) for k in range(len(i))])
        print(s)
