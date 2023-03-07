for row in range(7):
    for col in range(5):
        if row in {0,6} and col in {0,4}:
            print('K',end=' ')
        
        elif row in {1,2,3,4,5} and col==0:
            print('K',end=' ')
        elif row in {3} and col==1:
            print('K',end=' ')
        elif row in {2,4} and col==2:
            print('K',end=' ')
        elif row in {1,5} and col==3:
            print('K',end=' ')     
        else:
            print(' ',end=' ')
    print()