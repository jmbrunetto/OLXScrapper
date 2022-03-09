import olx_scrapper.olx_scrapper as olx
from utils import utils

if __name__ == '__main__':
    print("OlxScrapper - Main - Starting Module")
    thread = olx.OlxScrapper()

    # Quilometragem
    # ms = menor KM
    # me = maior KM
    # pe = Valor até
    # ps = Valor de
    # gb = # 1=Manual 2=Automatico 3=Semi-Automático
    # o = pagina

    URL = r'https://rs.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?gb=2&me=80000&ms=30000&pe=70000&ps=40000&re=36&rs=30'
    #result_file = r'/etc/carros.csv'
    result_file = r'C:\Users\BrunettJ\Documents\Jonas\sandbox\ScrapperOLX\etc\carros.csv'
    all_ads = thread.start_get_ads(URL, True)

    all_details = []
    for ad in all_ads:
        print("OlxScrapper - Main - Extracting {}".format(ad["Title"]))
        all_details.append(thread.extract_ad_info(ad))

    print(all_details)
    utils.dict_to_csv(dict_list=all_details, file_path=result_file)

    print("OlxScrapper - Main - Finishing Module")

