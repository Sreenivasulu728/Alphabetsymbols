for row in range(7):
    for col in range(5):
        if row in {0,6} and col in {1,2,3}:
            print('Q',end=' ')        
        elif row in {1,2,4,5} and col in {0,4}:
            print('Q',end=' ')
        elif row in {3} and col in {0,2,4}:
            print('Q',end=' ')
        elif row==4 and col==3:
            print('Q',end=' ')
        
           
        else:
            print(' ',end=' ')
    print()