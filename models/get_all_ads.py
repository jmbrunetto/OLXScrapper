class GetAllAds:

    def extract_ad_urls(self, ad_elements):
        ad_to_extract = []
        for ad in ad_elements:
            ad_href = ad.find('a', class_='fnmrjs-0')
            if ad_href:
                ad_link = ad_href.attrs['href']
                ad_title = ad_href.attrs['title']
                ad_result = {"Link": ad_link, "Title": ad_title}
                ad_to_extract.append(ad_result)
                # print("Anuncio \"{}\" \t \t Link -> {}".format(ad_title, ad_link))

        return ad_to_extract
