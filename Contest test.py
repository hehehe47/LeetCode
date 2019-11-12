x = 3
target = 365
y1, y2 = 0, 0

if target % x != 0:
    y1 = target % x
    target -= y1
count = 0
while target % x == 0:
    count += 1
    target //= x
y2 = target if target != 1 else 0
# t1 = (count*(x-y2+1)+1 if y2 > x / 2 else count*y2) if y2!=0 else count 逻辑错误
# t2 = (y1*2 if y1 < x / 2 else (x - y1)*2+1) if y1!=0 else y1 逻辑错误

t1 = (y1 * 2 if y1 * 2 < (1 + (x - y1) * 2) else 1 + (x - y1) * 2) if y1 != 0 else y1
t2 = (count * y2 if count * y2 < count * (x - y2 + 1) + 1 else count * (x - y2 + 1) + 1) if y2 != 0 else count

print(t1, t2)
