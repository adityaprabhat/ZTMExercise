def fib(number):
    a,b = 0,1
    for i in range(number):
        yield a
        temp = a
        a=b
        b+=temp


for x in fib(21):
    print(x)

