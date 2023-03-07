for row in range(7):
    for col in range(5):
        if row==0 and col in {0,1,2,3,4}:
            print('J',end=' ')
        
        elif row in {1,2,3,4,5} and col==2:
            print('J',end=' ')
        elif row==6 and col in {1,2}:
            print('J',end=' ')
        elif row==5 and col==0:
            print('J',end=' ')
            
       
        else:
            print(' ',end=' ')
    print()