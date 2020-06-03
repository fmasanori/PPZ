#traduzido e adaptado de http://blog.trinket.io/writing-poetry-in-python/
from random import choice, randint
    
adjetivos = '''compreensivo temperamental confiável confiável honesto desonesto 
interessante chato carinhoso simpático amigável generoso ciumento invejoso 
inseguro ambicioso ansioso bondoso sensato sensível teimoso preguiçoso 
trabalhador calmo paciente inteligente esperto espirituoso astuto neurótico 
ousado apático cínico sarcástico irônico cético alegre conservador pessimista 
otimista tolerante corajoso educado mal-educado determinado sociável 
solidário arrogante maldoso desajeitado burro independente confiável dependente 
organizado experiente ingênuo sincero responsável retraído reservado 
tímido engraçado leal fiel curioso interesseiro relaxado talentoso autoconfiante 
lindo feio bonita bonito alto baixo pequeno grande enorme gordo obeso magro 
magricelo esbelto musculoso forte religioso dedicado briguento feliz 
contente triste'''.split()
verbos = '''Amar Iluminar Curar Reviver Reatar Prosperar Premiar Enriquecer
Divulgar Enaltecer Abrilhantar Emanar Abençoar Semear Sanar Livrar Irromper
Brotar Florescer Colher Ligar Religar Abastecer Nutrir Suprir Religar Romantizar
Santificar Decorar Limpar Organizar Estabelecer Focalizar Azular Dourar
Rossificar Esverdear Laurear Premiar Compadecer Converter Conscientizar
Aliançar Gestar Criar Blogar Comunicar Doar Receber Estrelar Coroar
Consagrar Decodificar Perdoar Imantar Potencializar Transmutar Consagrar
Caetanear Carnavalizar Decifrar Colorir Deslindar Descobrir Enluarar
Ensolarar Cantar Poetizar '''.lower().split()
nomes = '''água concha palavra poesia face mulher resposta chave
           lua noite luz ponte nuvem ilha atriz autora dama esposa
           ira morte vida solidão barca benção abnegação abolição
           brasa briga canção casa idolatria beleza rima
           alegria tristeza pedra escuridão máquina mente imagem
           cama bicicleta rosa fruta espada brisa palmeira estrela
           terra sombra pomba ilha vela mãe lágrima paz mente
           jornada amizade fraqueza amizade voz alma idade noiva
           saúde lição atmosfera oração felicidade eternidade
           dor conduta esperança paixão confiança inteligência
           razão irmã semente rosa voz fada pessoa roupa separação
           reta curva viagem descoberta cidade vila despedida'''.split()

print ('\n' + '='*16+' Um poema ' + '='*16)
for x in range(randint(5,11)):
    palavras1 = ' '.join([choice(adjetivos) + ', ', choice(adjetivos)])
    palavras2 = ' '.join([choice(nomes), choice(verbos)])
    palavras3 = ' '.join([choice(nomes), choice(nomes), choice(adjetivos), choice(nomes)])
    
    for i in range(randint(2,5)):
        palavras = choice([palavras1, palavras2, palavras3])
        line = ' '*randint(0, 40 - len(palavras)) + palavras
        print (line)
    
    if x % 3 ==0:
        print ()
        print (' '*5 + choice(nomes))
        print (' '*5 + choice(nomes))
        print (' '*5 + 'a ' + choice(nomes) +'!')
        print ()
    
    if x % 7 ==0:
        palavras4 = ' '.join([choice(adjetivos), choice(nomes), choice(verbos)])
        print ()
        print (' '.join(palavras4))
        print ()
