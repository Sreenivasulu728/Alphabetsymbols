for x in range(7):
    for y in range(5):
        if x in {0,6} and y in {0,1,2,3}:
            print('B',end=' ')
        elif x in {1,2,4,5} and y in (0,4):
            print('B',end=' ')
        elif x==3 and y in {0,1,2,3}:
            print('B',end=' ')
        else:
            print(' ',end=' ')
    print()