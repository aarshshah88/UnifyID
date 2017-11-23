from urllib2 import Request, urlopen, URLError
from fractions import gcd

def func():
    request = Request('https://www.random.org/integers/?num=1000&min=10000&max=1000000&col=1&base=10&format=plain&rnd=new')

    prime_numbers = []

    try:
        response = urlopen(request)
        numbers = response.read()
        numbers = [int(i) for i in numbers.split()]
    except URLError, e:
        print('No file.', e)


    for x in range(len(numbers)):
        print(numbers[x])
        if len(prime_numbers) < 2 and is_prime(numbers[x]):
            prime_numbers.append(numbers[x])

    print('These are the prime numbers', prime_numbers)
    n = prime_numbers[0] * prime_numbers[1]
    print('This is n', n)
    r = (prime_numbers[0] - 1) * (prime_numbers[1] - 1)
    print('This is r', r)
    e = get_e(n)
    print('This is e', e)
    x, y, z = egcd(e, r)
    d =  y % r
    print('This is d', d)

    print('The public key is ', n, e)
    print('The private key is ', d)


def is_prime(a):
    return all(a % i for i in range(2, a))

def get_e(n):
    for x in range(10, 100):
        if gcd(n, x) == 1:
            return x

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def get_d(e, r):
    x = egcd(e, r)
    print(x)
    return abs(x[1] + r)

def gcdExtended(a, b, x, y):
    # Base Case
    if a == 0 : 
        x = 0
        y = 1
        return b
         
    x1 = 1
    y1 = 1 # To store results of recursive call
    gcd = gcdExtended(b%a, a, x1, y1)
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b/a) * x1
    y = x1
 
    return gcd



func()

