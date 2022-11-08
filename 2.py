stream = list(input())
lower = input().split()
count = [] 

for j in lower:
    cnt = stream.count(j) + stream.count(chr(ord(j)-32))
    count.append(cnt)

for l in lower:
    print(l, end='')
print()

for k in range(max(count)):
    for i in range(len(lower)):
        if count[i] == 0:
            print(' ', end='')
        else:
            print('*', end='')
            count[i] -= 1
    print()
