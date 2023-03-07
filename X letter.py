for x in range(5):
    for y in range(5):
        if x in {0,4} and y in {0,4}:
            print('X',end=' ')
        elif x in {1,3} and y in {1,3}:
            print('X',end=' ')
        elif x==2 and y==2:
            print('X',end=' ')
        else:
            print(' ',end=' ')
    print() 
   