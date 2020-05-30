labirinto = '''
+-----+-----+-+
|E    |     | |
| | +-+  -+ | |
| | |     | | |
| |   +---+ | |
| | | |     | S
|   | | | | | |
|-----+ +-+-+ |
|     | | |   |
| +-+   | |  -|
| |-+-|   |-  |
| | | +---+-- |
|             |
+-------------+
'''

ENTRADA, LIVRE, PASSEI, SOLUÇÃO, SAÍDA = 'E .oS'

def saiu(x, y):
    if lab[x][y] == SAÍDA:
        return True
    if lab[x][y] in (ENTRADA, LIVRE):
        lab[x][y] = PASSEI
        if saiu(x-1, y) or saiu(x+1, y) or saiu(x, y-1) or saiu(x, y+1):
            lab[x][y] = SOLUÇÃO
            return True
    else:
        return False

lab = []
for x in labirinto.splitlines():
  if len(x) > 0:
    x = list(x)
    lab.append(x)

for j in range(len(lab)):
  for k in range(len(lab[j])):
    if lab[j][k] == ENTRADA:
      x = j
      y = k
      break

if saiu(x, y):
    for linha in lab:
        print (''.join(linha))
else:
    print ('A formiga irá morrer...')
