for row in range(5):
    for col in range(5):
        if row in {0,4} and col in {0,1,2,3,4}:
            print('Z',end=' ')  
        elif row==1 and col in {3}:
            print('Z',end=' ')
        elif row==2 and col in {2}:
            print('Z',end=' ') 
        elif row==3 and col==1:
            print('Z',end=' ')     
        else:
            print(' ',end=' ')
    print()