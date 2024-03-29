import requests
from bs4 import BeautifulSoup

class Investing:
    def __init__(self, sigla_fii: str):
        self.sigla_fii = sigla_fii
        
    def get_fii_quote(self):
        # headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        # 'Referer': 'https://www.google.com'
        # }
    
        url = f'https://www.infomoney.com.br/cotacoes/b3/fii/fundos-imobiliarios-{self.sigla_fii}/'
        response = requests.get(url)
        
        print(f"O resultado da request: {response}")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        quote_element = []            
        for item in soup.find_all('span', attrs={'class': ['typography__display--2-noscale typography--numeric spacing--mr1']}):
            quote_element.append(item.text.replace('\n', ' ').strip())
            
        dict_payload = {
            "Valor da Cota": 0,
        }

        for key, value in zip(dict_payload.keys(), quote_element):
            dict_payload[key] = value
            # print(f"{key}:{value}")
            
        return dict_payload
    
    
    def make_get_fii_quote(self):
        name_plataform = "*** INVESTING ***"
        print(name_plataform)
        
        fiis_dict_values = self.get_fii_quote()
        
        print(f"\nO valor da cota {self.sigla_fii.upper()} atualmente é: \n")
        
        for chave, valor in fiis_dict_values.items():
            print(chave, ":", valor)