import requests
from bs4 import BeautifulSoup

class YahooFinances:
    def __init__(self, sigla_fii: str):
        self.sigla_fii = sigla_fii
        
    def get_fii_quote(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Referer': 'https://www.google.com'
        }
    
        url = f'https://finance.yahoo.com/quote/{self.sigla_fii}.SA/'
        response = requests.get(url, headers=headers)
        
        print(f"O resultado da request: {response}")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        quote_element = []
        for item in soup.find_all('fin-streamer', attrs={'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}):
            quote_element.append(item.text.replace('\n', ' ').strip())
            
        result_to_string = ''.join(quote_element)
        return result_to_string
    
    def make_get_fii_quote(self):
        print("*** YAHOO FINANCES ***")
        fii_value = self.get_fii_quote()
        
        print(f"O valor da cota {self.sigla_fii.upper()} atualmente é: R${fii_value}\n")