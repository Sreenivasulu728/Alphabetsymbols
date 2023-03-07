for row in range(7):
    for col in range(5):
        if row in {0,6} and col in {1,2,3}:
            print('O',end=' ')        
        elif row in {1,2,3,4,5} and col in {0,4}:
            print('O',end=' ')
           
        else:
            print(' ',end=' ')
    print()