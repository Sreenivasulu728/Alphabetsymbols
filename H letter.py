for row in range(7):
    for col in range(5):
        if row in {0,1,2,4,5,6} and col in {0,4}:
            print('H',end=' ')
        
        elif row==3 and col in {0,1,2,3,4}:
            print('H',end=' ')
       
        else:
            print(' ',end=' ')
    print()