def contagem(n):
    print (n)
    if n == 0:
        return
    else:
        contagem(n-1)
contagem(10)

def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n-1)
print (fat(4))

def pot(x, n):
  if n == 0:
    return 1
  else:
    return x * pot(x, n - 1)
print (pot(2, 3))

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(4))

def mdc(a, b):
    if a % b == 0:
        return b
    else:
        return mdc(b, a%b)
print (mdc(24, 15))

def soma(n):
    if n < 10:
        return n
    else:
        return n%10 + soma(n//10)
print(soma(123))

def inv(s):
    if s == '':
        return s
    else:
        return inv(s[1:]) + s[0]
print(inv('abacate'))











