#==================================================
# Cotacao do dolar
#==================================================
import requests
import re

def pegar_cotacao_dolar():
    """
    Funcao para pegar a cotacao do dolar.
    Retorna uma tupla com o : valor de compra e o valor de venda
    do dia.
    """
    
    # pegando o conteudo da pagina    
    pagina = requests.get( 'http://www.bc.gov.br/htms/infecon/taxas/taxas.htm').read()
    
    # obtendo os valores de compra e venda do dolar
    taxa_compra, taxa_venda = re.findall( '[0-9],[0-9][0-9][0-9]', pagina )
    
    # retornando esses valores
    return ( taxa_compra, taxa_venda )
    
print (pegar_cotacao_dolar())
