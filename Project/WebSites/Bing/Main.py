from Project.WebSites.Bing.BingImages import BingImageScraper

imageList = "D:\Programs\Python_Programs\WebBot\ListofInterest\BIng-Image-List"
imgaeListFile = open(imageList,'r')

for i in imgaeListFile:
    print(i)
    BingImageScraper(i)
