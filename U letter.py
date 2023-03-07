for row in range(5):
    for col in range(5):
        if row in {0,1,2,3} and col in {0,4}:
            print('U',end=' ')        
        elif row==4 and col in {1,2,3}:
            print('U',end=' ')
        else:
            print(' ',end=' ')
    print()