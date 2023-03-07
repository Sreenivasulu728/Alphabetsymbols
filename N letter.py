for row in range(5):
    for col in range(5):
        if row in {0,1,2,3,4,5,6} and col in {0,4}:
            print('N',end=' ')        
        elif row==1 and col==1:
            print('N',end=' ')
        elif row==2 and col==2:
            print('N',end=' ')
        elif row==3 and col==3:
            print('N',end=' ')
        # elif row in {1,5} and col==3:
        #     print('K',end=' ')     
        else:
            print(' ',end=' ')
    print()