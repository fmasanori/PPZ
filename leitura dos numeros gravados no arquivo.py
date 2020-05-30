f = open(r'c:/Users/fmasa/x.txt')
for linha in f.readlines():
  print (linha.strip())
f.close()
