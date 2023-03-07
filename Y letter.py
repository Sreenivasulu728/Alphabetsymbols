for row in range(5):
    for col in range(5):
        if row in {2,3,4} and col in {2}:
            print('Y',end=' ')  
        elif row==0 and col in {0,4}:
            print('Y',end=' ')
        elif row==1 and col in {1,3}:
            print('Y',end=' ') 
           
        else:
            print(' ',end=' ')
    print()