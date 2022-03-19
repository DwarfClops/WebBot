from Project.URLRequest.Main import UrlRequestHandler
from Project.Methods import SaveImages
import time
import json

class BingImageScraper():
    def __init__(self,searchitem = "Anime"):
        self.url = "https://www.bing.com/images/async?"
        self.requesthandlers = UrlRequestHandler(self.url)
        self.searchitem = searchitem.strip('\n')
        self.listofImages = []
        queryStrings = {"q": searchitem, "first": "38", "count": "35", "qft": "+filterui:imagesize-wallpaper", "tsc": "ImageBasicHover", "datsrc": "I", "layout": "RowBased_Landscape", "mmasync": "1"}
        initURLString = self.requesthandlers.MakeUrlString(queryStrings)
        self.Scrape(initURLString)

    def MakeRequest(self,url):
        sitesoup = self.requesthandlers.MakeRequest(url)
        data = False
        if sitesoup:
            data = sitesoup.find_all('a', href=True)
        return data

    def AquireimgURL(self,url):
        sitesoup = self.requesthandlers.MakeRequest(url)
        imgwindow = sitesoup.find("div",{"id":"b_content"})
        data = imgwindow.find("div")
        data = data.attrs['data-firstimg']
        print(data)
        img = json.loads(data)['thumbnailUrl']
        return img

    def Scrape(self,url):
        startT = time.time()
        els = self.MakeRequest(url)
        pageLinks = self.sort(els)
        endT = time.time()
        print(endT - startT)
        #self.ContinueScrape(pageLinks)
        set(self.listofImages)
        print("Saving Images")
        SaveImages(self.searchitem,self.listofImages)
        print("end")

    def ContinueScrape(self,pageLinks):
        print("amount of images Scrapped " + str(self.listofImages.__len__()))
        print("amount of Pages Found " + str(pageLinks.__len__()))
        inpu = input("continue?")
        if inpu == "y":
            print("Scrapping more Images ")
            if pageLinks.__len__() > 1:
                self.Scrape(pageLinks[-1])
        else:
            print("Ending Scrapping ")

    def sort(self,Aels):
        print("starting sort")
        nextpagelinks = []
        if Aels is not False:
            for i in Aels:
                getHref = i.get('href')
                if "/images/" in getHref:
                    if "?view=" in getHref:
                        data = "https://www.bing.com" + getHref
                        print(data)
                        img = self.AquireimgURL(data)
                        if img not in self.listofImages:
                            print("adding image " +getHref)
                            self.listofImages.append(img)
                    else:
                        nextpagelinks.append(getHref)
            return nextpagelinks
        else:
            print("No Links Found")
            return False

