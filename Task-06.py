def maximum(*args):
    a = None
    for b in args:
        if a is None or b > a:
            a =b
    print(a)

maximum(20,40,10,39,90,100)
