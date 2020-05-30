texto = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone. Our community is based on mutual respect,
   tolerance, and encouragement, and we are working to help
   each other live up to these principles. We want our
   community to be more diverse: whoever you are, and
   whatever your background, we welcome you.'''.lower()

import string
for c in string.punctuation:
  texto = texto.replace(c, ' ')
  
def pitônica(x):
  for c in x:
    if c in 'python':
      return True
  return False

resp = [p for p in texto.split()
        if pitônica(p) and len(p) > 4]
print (resp)
print (len(resp))
