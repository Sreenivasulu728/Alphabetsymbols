for row in range(7):
    for col in range(5):
        if row in {0,6} and col in [1,2,3,4]:
            print('C',end=' ')
        elif row in [1,2,3,4,5] and col==0:
            print('C',end=' ')
        else:
            print(' ',end=' ')
    print()