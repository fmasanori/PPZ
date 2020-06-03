#Pi Generator ref https://mail.python.org/pipermail/edu-sig/2015-September/011317.html
def pi_digits():
  k, a, b, a1, b1 = 2, 4, 1, 12, 4
  while True:
    p, q, k = k*k, 2*k+1, k+1
    a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
    d, d1 = a//b, a1//b1
    while d == d1:
      yield int(d)
      a, a1 = 10*(a%b), 10*(a1%b1)
      d, d1 = a//b, a1//b1

pi = pi_digits()
print (''.join([str(next(pi)) for i in range(100)]))
