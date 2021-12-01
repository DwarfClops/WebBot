from WebSites.Selenium.MySeleniumDriver import LoadEdgeWithUserData

class PintrestBot():
    def __init__(self):
        self.htmlTags = {}
        self.driver = LoadEdgeWithUserData()

    def MainLoop(self):
        self.initRequest()


a = PintrestBot()

a.MainLoop()
