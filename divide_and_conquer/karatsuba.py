x = 5678
y = 1234

# multiply two integers
def karatsuba(x, y):
    n = min(len(str(x)), len(str(y)))
    
    if n == 1:
        return int(x*y)

    a = int(x/(10**(n/2)))
    b = int(x - a*10**(n/2))
    
    c = int(y/(10**(n/2)))
    d = int(y - c*10**(n/2))

    c1 = karatsuba(a, c)
    c2 = karatsuba(b, d)
    c3 = karatsuba(a+b, c+d)
    c4 = c3 - c2- c1
    
    return int(c1 * 10**n + c4 * 10**(n/2) + c2)

if __name__ == '__main__':
    print(karatsuba(x, y))
