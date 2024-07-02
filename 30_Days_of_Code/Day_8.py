n = int(input())
d = {}
for _ in range(n):
    x, y = input().split()
    d[x] = int(y)
try:
    element = input()
    while True:
        if element in d:
            print(f"{element}={d[element]}")
        else:
            print('Not found')
    
        element = input()
except EOFError:
    print()
