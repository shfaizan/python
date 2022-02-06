def test(n):

    if n>1:
        test(n/2)
    
    print(n%2)


test(8)