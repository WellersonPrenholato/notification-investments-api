import requests
from bs4 import BeautifulSoup

def get_fii_quote(sigla_fii):
    # headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    # 'Referer': 'https://www.google.com'
    # }
    
    url = f'https://www.fundsexplorer.com.br/funds/{sigla_fii}'
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quote_element = [] 
    div_element =  soup.find('div', class_='headerTicker__content__price')
    
    if div_element:
        p_element = div_element.find('p')
        quote_element.append(p_element.text.replace('\n', ' ').strip())
    else:
        print("Elemento não encontrado. Verifique a página ou a classe CSS.")

    dict_payload = {
        'Valor da Cota': "R$" + quote_element[0] if quote_element else "Valor não disponível",
    }

    return dict_payload

def imprime_dict(dict_values: dict):
    for chave, valor in dict_values.items():
        print(chave, ":", valor)
    
if __name__ == "__main__":
    sigla_fii = input("Insira o identificador do FII: ")
    fiis_dict_values = get_fii_quote(sigla_fii)
    
    print("*** FUNDS EXPLORER ***")
    if fiis_dict_values is not None and len(fiis_dict_values) >= 1:
        print(f"O valor atual do {sigla_fii.upper()}")
        imprime_dict(fiis_dict_values)
    else:
        print(f"Não foi possível obter o valor do {sigla_fii.upper()}")
