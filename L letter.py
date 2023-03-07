for row in range(7):
    for col in range(5):
        if row in {0,1,2,3,4,5,6} and col==0:
            print('L',end=' ')        
        elif row==6 and col in {1,2,3,4}:
            print('L',end=' ')    
        else:
            print(' ',end=' ')
    print()