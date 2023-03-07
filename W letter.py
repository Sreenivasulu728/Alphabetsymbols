for row in range(5):
    for col in range(5):
        if row in {0,1,2,3,4,5,6} and col in {0,4}:
            print('W',end=' ')  
        elif row==4 and col in {1,3}:
            print('W',end=' ')
        elif row==3 and col in {2}:
            print('W',end=' ')      
        else:
            print(' ',end=' ')
    print()