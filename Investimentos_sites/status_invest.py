# DESENVOLVER WEB SCRAPING PARA O SITE https://statusinvest.com.br/fundos-imobiliarios/mxrf11
import requests
from bs4 import BeautifulSoup


def get_fii_quote(fii_id:str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Referer': 'https://www.google.com'
    }
    
    url = f'https://statusinvest.com.br/fundos-imobiliarios/{fii_id}/'
    response = requests.get(url, headers=headers)
    # print(response)
    
    if response.status_code != 200:
        print(f"Erro ao acessar a página: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    quote_element = []
    valores_cota_element = soup.find_all('div', attrs={'class': 'info'})
    for div in valores_cota_element:
        valores_cota_element = div.find_all('strong', class_='value')
        
        for valor in valores_cota_element:
            quote_element.append(valor.text.replace('\n', ' ').strip())

    # print(f"QUOTE: {quote_element}")
    if len(quote_element) > 0:
        valor_cota = "R$" + str(quote_element[0])
    else:
        valor_cota = "Valor não disponível"

    if len(quote_element) > 6:
        p_vp = str(quote_element[6])
    else:
        p_vp = "P/VP não disponível"

    informacoes_fundo = {
        'Valor da Cota': valor_cota,
        'P/VP': p_vp,
    }

    return informacoes_fundo

def imprime_dict(dict_values: dict):
    for chave, valor in dict_values.items():
        print(chave, ":", valor)

if __name__ == "__main__":

    fii_string = input("Insira o identificador do FII: ")
    dict_a = {}
    quote = get_fii_quote(fii_string)
    
    print("*** PESQUISA STATUS INVEST ***")
    if quote is not None and len(quote) >= 1:
        print(f"O valor atual do {fii_string.upper()}")
        imprime_dict(quote)
    else:
        print(f"Não foi possível obter o valor do {fii_string.upper()}")
