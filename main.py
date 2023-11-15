from yahoo_finance import YahooFinances
from funds_explorer import FundsExplorer
from infomoney import Investing

if __name__ == "__main__":
    
    name_fii = 'mxrf11'
    
    investiment_yahoo = YahooFinances(name_fii)
    investiment_yahoo.make_get_fii_quote()
    
    print('*' * 30)
    
    investiment_funds_explorer = FundsExplorer(name_fii)
    investiment_funds_explorer.make_get_fii_quote()
    
    print('*' * 30)
    
    investiment_investing = Investing(name_fii)
    investiment_investing.make_get_fii_quote()