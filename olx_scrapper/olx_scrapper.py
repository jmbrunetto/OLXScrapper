import requests
from bs4 import BeautifulSoup
from models.get_all_ads import GetAllAds
from models.get_all_pages import GetAllPages
from utils.ad_list import ad_list

class OlxScrapper:

    def __init__(self):
        print("OlxScrapper - OlxScrapper - Getting All Ads from URL")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.114 Safari/537.36'}

    def start_get_ads(self, url, get_new_ads):
        all_adds = []
        if get_new_ads:
            page = requests.get(url, headers=self.headers)
            # print(page.content.decode())
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(id='ad-list')
            number_of_pages = GetAllPages.extract_number_of_pages(self, soup)
            ad_elements = soup.find_all(class_='sc-1fcmfeb-2')
            all_adds = GetAllAds.extract_ad_urls(self, ad_elements)

            for pages in range(1, number_of_pages+1):
                new_url = url + "&o=" + str(pages)
                page = requests.get(new_url, headers=self.headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                ad_elements = soup.find_all(class_='sc-1fcmfeb-2')
                page_ads = GetAllAds.extract_ad_urls(self, ad_elements)
                all_adds = all_adds + page_ads

        else:
            all_adds = ad_list
        return all_adds

    def extract_ad_info(self, ad):
        page = requests.get(ad["Link"], headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        car_details = soup.find_all(class_ = 'sc-57pm5w-0 XtcoW')
        result = {"Link": ad["Link"], "Title": ad["Title"]}
        for detail in car_details:
            if detail.previous == "Modelo":
                result["Modelo"] = detail.contents[0]
            elif detail.previous == "Marca":
                result["Marca"] = detail.contents[0]
            elif detail.previous == "Ano":
                result["Ano"] = detail.contents[0]
        car_details_opt = soup.find_all(class_ = 'sc-ifAKCX cmFKIN')
        for detail_opt in car_details_opt:
            if detail_opt.previous == "Quilometragem":
                result["Quilometragem"] = detail_opt.contents[0]
        price_element = soup.find_all(class_ = 'sc-1leoitd-0 cIfjkh sc-ifAKCX cmFKIN')
        for price in price_element:
            result["Preço"] = price.contents[0]

        return result
