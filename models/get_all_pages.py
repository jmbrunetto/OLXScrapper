from utils import utils


class GetAllPages:
    def __init__(self):
        print("OlxScrapper - GetAllPages - Get Pages Count")

    def extract_number_of_pages(self, soup):
        page_elements = soup.find_all(class_='sc-1bofr6e-0 iRQkdN')
        last_page = 0
        for e in page_elements:
            link_dict = utils.Utils.extract_url_parameters(self, e.attrs['href'])
            for parameter in link_dict:
                if 'o' in parameter:
                    if last_page < int(parameter['o']):
                        last_page = int(parameter['o'])
        return last_page
