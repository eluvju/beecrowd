
while True:
    A,B = list(map(int,input().split(' ')))
    if A > B:
        print('Decrescente')
    elif A < B:
        print('Crescente')
    elif A == B:
        break
