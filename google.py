import requests
from bs4 import BeautifulSoup


def union_dict_list (fii_values:list):
    dict_payload = {
            "Liquidez Diária":0,
            "Último Rendimento":0,
            "Dividend Yield":0,
            "Patrimônio Líquido":0,
            "Valor Patrimonial":0,
            "Rentab. no mês":0,
            "P/VP":0
        }

    for key, value in zip(dict_payload.keys(), fii_values):
        dict_payload[key] = value
        # print(f"{key}:{value}")
        
    return dict_payload

def get_fii_quote(fii_id:str):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    #     'Referer': 'https://www.google.com'
    # }
    
    url = f'https://www.google.com/finance/quote/{fii_id}:BVMF'
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')

    quote_element = []
    for item in soup.find_all('div', attrs={'class': 'YMlKec fxKbKc'}):
        quote_element.append(item.text.replace('\n', ' ').strip())
        
    return quote_element

def imprime_dict(dict_values: dict):
    for chave, valor in dict_values.items():
        print(chave, ":", valor)

if __name__ == "__main__":

    fii_string = input("Insira o identificador do FII: ")
    dict_a = {}
    quote = get_fii_quote(fii_string)
    print(quote)
    # dict_a = union_dict_list(quote)
    # imprime_dict(dict_a)
