from urllib.parse import urlencode
from urllib.request import Request,urlopen,urlretrieve
import bs4

class UrlRequestHandler():
    def __init__(self,Site="https://www.bing.com"):
        self.urlBase = Site

    def MakeUrlString(self,queryStrings=None):
        if queryStrings:
            query = urlencode(queryStrings)
            urlString = self.urlBase+query
        else:
            urlString = self.urlBase
        return urlString

    #this returns a BeautifulSoup OBJ
    def MakeRequest(self,urlString=None):
        try:
            req = Request(urlString)
            site = urlopen(req)
            sitedata = bs4.BeautifulSoup(site, features="html.parser")
            return sitedata
        except:
            print("Bad Request")
            return False

    def Retrieve(self,url,imagename):
        image = urlretrieve(url,imagename)
        return image