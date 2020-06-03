a = 'Co\u00f1o!'
b = 'Con\u0303o!'
print (a, b, a == b, len(a), len(b))
print ()

import unicodedata
print ('Fully Composed')
a1 = unicodedata.normalize('NFC', a)
b1 = unicodedata.normalize('NFC', b)
print (a1, b1, a1 == b1, len(a1), len(b1))
print ()
print ('Fully Decomposed')
a1 = unicodedata.normalize('NFD', a)
b1 = unicodedata.normalize('NFD', b)
print (a1, b1, a1 == b1, len(a1), len(b1))
print ()

s = 'Cleaning Pýtĥöñ'
print (s)
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
s1 = unicodedata.normalize('NFD', s)
print (s1.translate(cmb_chrs))
print ()
print (s)
s1 = unicodedata.normalize('NFD', s)
print (s1.encode('ascii', 'ignore').decode('ascii'), '(ASCII final)')
print ()

s = 'Dígitos árabes: \u0661\u0662\u0663\u0664\u0665\u0666'
print (s)
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print (s.translate(digitmap))
