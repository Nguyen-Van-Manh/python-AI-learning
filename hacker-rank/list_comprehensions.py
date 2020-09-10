x = int(input())
y = int(input())
z = int(input())
n = int(input())
result = []
sum = 0
for i in range(x+1):
    sum = i
    print('I {}'.format(i))
    for j in range(y+1):
        print('Y {}'.format(j))
        sum += j
        for k in range(z+1):
            print('Z {}'.format(k))
            sum += k
            if sum != n:
                result.append([i, j, k])
            sum -= k
        sum -= j
print(result)