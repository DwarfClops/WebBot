# This is a Pop Price guide scraper
# searches for most valuable item of declared subject for Funko Pops
# sorts from Highest Value to lowest
from urllib import request
from urllib.parse import urlencode
import json
from WebSites.PPG.Methods import ReadPopData



class PPG:
    def __init__(self,item='pop'):
        self.url = "https://www.hobbydb.com/api/catalog_items?"
        self.Headers = {'authority' : 'www.hobbydb.com',
                'method': 'GET',
                'path': '/api/catalog_items?filters=%7B%22in_collection%22:%22all%22,%22in_wishlist%22:%22all%22,%22on_sale%22:%22all%22%7D&include_cit=true&include_count=false&include_last_page=true&include_main_images=true&market_id=poppriceguide&order=%7B%22name%22:%22last_value%22,%22sort%22:%22desc%22%7D&page=4&per=6&q=pops&serializer=CatalogItemPudbSerializer&subvariants=true',
                'scheme': 'https',
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cookie':'_ga=GA1.2.1804669284.1637281225; _gid=GA1.2.1676470573.1637281225; _hobbydb_session=b6eb611dc9f6b701d4df95d4590b27b7; __gads=ID=ff34b98024f4dc9f:T=1637281229:S=ALNI_MZAtafVCtu03AG_qVhHyserFLDS-g; XSRF-TOKEN=IkKS6Bt4R%2BngkIF0OKq04W7h1PmSZ%2FlVmQWfp%2Bmx930RsW2scW8y0ZpZpg08CaOPz5MjetI%2Bc%2B0MZDk%2B%2Bw9jTQ%3D%3D',
                'referer':' https://www.hobbydb.com/marketplaces/poppriceguide/catalog_items?filters[in_collection]=all&filters[in_wishlist]=all&filters[on_sale]=all&order[name]=last_value&order[sort]=desc&page=4&q=pops&subvariants=true',
                'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile' : '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest' :'empty',
                'sec-fetch-mode':'cors',
                'sec-fetch-site':' same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
                'x-xsrf-token': 'IkKS6Bt4R+ngkIF0OKq04W7h1PmSZ/lVmQWfp+mx930RsW2scW8y0ZpZpg08CaOPz5MjetI+c+0MZDk++w9jTQ==}'}
        self.item = item

    def MakeQuery(self,pagenum,):
            query = {'filters': '{"in_collection":"all","in_wishlist":"all","on_sale":"all"}',
                     'include_cit': 'true',
                     'include_count': 'false',
                     'include_last_page': 'true',
                     'include_main_images': 'true',
                     'market_id': 'poppriceguide',
                     'order': '{"name":"last_value","sort":"desc"}',
                     'page': pagenum,
                     'per': '6',
                     'q': self.item,
                     'serializer': 'CatalogItemPudbSerializer',
                     'subvariants': 'true'}
            return query

    def InitRequest(self):
            data = []
            for x in range(1,5):
                query = self.MakeQuery(x)
                querystring = urlencode(query)
                fullURL = self.url + querystring
                req = request.Request(fullURL,headers=self.Headers)
                resp = request.urlopen(req)
                xdata = json.loads(resp.read())
                data.append(xdata)
            return data

#EX Returns most valuable pops
if __name__ == "__main__":
        A = PPG('Goku')
        data = A.InitRequest()
        ReadPopData(data)
