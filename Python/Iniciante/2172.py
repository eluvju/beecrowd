N = 1

while (N > 0):
    A,B = list(map(int,input().split(' ')))
    if (A == 0) and (B == 0):
        N -= 1
    else:
        print(f'{A*B}')