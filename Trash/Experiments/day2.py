N = int(input())
if N%2==0: 
    if 1<N<6 or N>20:
        print('wierd')
    else:
        print('not wierd')
else:
    print('wierd')
