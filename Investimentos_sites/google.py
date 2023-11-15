import requests
from bs4 import BeautifulSoup

def get_fii_quote(fii_id:str):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    #     'Referer': 'https://www.google.com'
    # }
    
    url = f'https://www.google.com/finance/quote/{fii_id}:BVMF'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Erro ao acessar a página: {response.status_code}")
        return None
    
    # print(response)
    soup = BeautifulSoup(response.text, 'html.parser')

    quote_element = []
    for item in soup.find_all('div', attrs={'class': 'YMlKec fxKbKc'}):
        quote_element.append(item.text.replace('\n', ' ').strip())

    return quote_element

def main(fii_name: str):
    quote = get_fii_quote(fii_name)
    
    if quote is not None and len(quote) >= 1:
        quote[0] = quote[0].replace("R$", "")
        return fii_name.upper(), quote[0] # (f"O VALOR DO FII *{fii_name.upper()}*: {quote[0]}")
    else:
        return fii_name.upper(), 0 #(f"Não foi possível obter o valor do {fii_name.upper()}")
    

if __name__ == "__main__":
    valor1, valor2 = main("MXRF11")
    
    print(f"{valor1} -- {valor2}")
