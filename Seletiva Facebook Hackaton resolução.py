'''
Selection Test 2013 Facebook Hackaton
Given two positive integers n and k,
generate all binary integer between
0 and 2 ** n-1, inclusive.
These binaries will be drawn in
descending order according to the
number of existing 1s.
If there is a tie choose the lowest
numerical value.
Return the k-th element from the
selected list.
Eg n = 3 and k = 5
['0 b111 ', '0 b11', '0 B101 ',
'0 b110', '0 b1 ', '0 b10',
'0 b100 ', '0 b0']
fifth element '0 b1 '
'''
def hack1(n, k):
  def f(s): return s.count('1')
  binários = []
  for x in range(2**n):
    binários.append(bin(x))
  binários.sort(key=f, reverse=True)
  return binários[k - 1]

def hack(n, k):
  return sorted(
    [bin(x) for x in range(2**n)],
     key=lambda s: s.count('1'),
     reverse = True)[k-1]

print (hack1(3, 5))
print (hack(3, 5))
