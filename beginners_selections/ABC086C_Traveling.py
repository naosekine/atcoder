# -*- coding: utf-8 -*-
# 整数の入力
n = int(input())
# スペース区切りの整数の入力*n
travels = []
for i in range(n):
    t, x, y = map(int, input().split())
    travels.append((t, x, y))

if n == 1:
    if travels[0][1] + travels[0][2] == 1:
        print("Yes")
    else:
        print("No")
    exit()

for i in range(n-1):
    t_diff = travels[i+1][0] - travels[i][0]
    x_diff = abs(travels[i+1][1] - travels[i][1])
    y_diff = abs(travels[i+1][2] - travels[i][2])
    
    if x_diff + y_diff > t_diff:
        print("No")
        exit()
    
    t_odd_even = t_diff % 2
    xy_odd_even = (x_diff + y_diff) % 2
    if t_odd_even != xy_odd_even:
        print("No")
        exit()

print("Yes")
