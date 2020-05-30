plist = [2]

def primes(min, max):
        global plist
        if 2 >= min: yield 2
        i = 3
        while i <= max:
            for p in plist:
                if i%p == 0 or p*p > i: break
            if i%p:
                plist.append(i)
                if i >= min: yield i
            i = i+2
        
def factors(number):
        for prime in primes(2, number):
            if number % prime == 0:
                number = number / prime
                yield prime
            if number == 1:
                raise StopIteration

print max(factors(600851475143))
