from urllib import request

class RequestHandler():
    def __init__(self,searchItem):
        self.header = {}
        self.MakeRequest(searchItem)

    def InitHeader(self,searchitem):
        self.header['Orgin'] = "https://www.pinterest.com/"
        self.header['sec-ch-ua'] = "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"
        self.header['sec-ch-ua-platform'] = "Windows"
        self.header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"
        #self.header['q'] = str(searchitem)
        #self.header['rs'] = 'typed'


    def MakeRequest(self,searchItem):
        pinterestSearchUrl = "https://www.pinterest.com/search/pins/"
        url = "https://www.pinterest.com/search/pins/?q=anime&rs=typed&term_meta[]=anime%7Ctyped"
        self.InitHeader(searchItem)
        req = request.Request(url,headers=self.header)
        print(req.full_url)
        print(req.get_full_url())
        print(req.header_items())
        pinterest = request.urlopen(req)
        print(pinterest.readlines())

