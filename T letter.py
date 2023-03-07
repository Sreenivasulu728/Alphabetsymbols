for row in range(5):
    for col in range(5):
        if row==0 and col in {0,1,2,3,4}:
            print('T',end=' ')        
        elif row in {1,2,3,4} and col==2:
            print('T',end=' ')
        else:
            print(' ',end=' ')
    print()