for row in range(7):
    for col in range(5):
        if row in {0,6} and col in {0,1,2,3,4}:
            print('I',end=' ')
        
        elif row in {0,1,2,3,4,5,6} and col==2:
            print('I',end=' ')
       
        else:
            print(' ',end=' ')
    print()