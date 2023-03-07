for row in range(7):
    for col in range(5):
        if row in {0,3,4,5,6} and col==0:
            print('R',end=' ')        
        elif row in {1,2} and col in {0,4}:
            print('R',end=' ')
        elif row==4 and col in {2}:
            print('R',end=' ')
        elif row==5 and col in {3}:
            print('R',end=' ')
        elif row==6 and col==4:
            print('R',end=' ')
        elif row==0 and col in {0,1,2,3}:
            print('R',end=' ')
        elif row==3 and col in {1,2,3}:
            print('R',end=' ')       
        else:
            print(' ',end=' ')
    print()