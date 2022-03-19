import time
from Project.WebSites.Bing.Methods import ListFunctions
from Project.Selenium.MySeleniumDriver import LoadEdgeWithUserData

class AutoBingSearch():
    def __init__(self):
        self.bingFormTags = {'Search_Bar':'input','mainpage_search_icon':'search_icon','Next_Search':'sb_form_go','Tag_With_Links':'b_content','href':'href','a':'a'}
        self.exception = ['javascript:void(0);','javascript:void(0)']
        self.driver = LoadEdgeWithUserData()
        self.listfnc = ListFunctions()
        self.searchList = self.listfnc.ReadSearchList()
        self.linkListFile = self.listfnc.MakeLinkList()

    def MainBingPage(self):
        self.driver.get("https://www.bing.com")
        time.sleep(2)
        searchstring = self.searchList[0]
        forminput = self.driver.find_elements_by_tag_name(self.bingFormTags['Search_Bar'])
        forminput[0].send_keys(searchstring)
        searchicon = self.driver.find_elements_by_id(self.bingFormTags['mainpage_search_icon'])
        searchicon[0].click()

    def SearchPage(self, searchitem):
        forminput = self.driver.find_elements_by_tag_name(self.bingFormTags['Search_Bar'])
        forminput[0].clear()
        forminput[0].send_keys(searchitem)
        searchicon = self.driver.find_elements_by_id(self.bingFormTags['Next_Search'])
        searchicon[0].click()

    def GrabLinks(self):
        body = self.driver.find_elements_by_id(self.bingFormTags['Tag_With_Links'])
        print(body)
        links = body[0].find_elements_by_tag_name('a')
        print(links)
        listOfLinks = []
        for a in links:
            try:
                data = a.get_attribute(self.bingFormTags['href'])
                #text = a.get_attribute('text')
                listOfLinks.append(data)
            except:
                continue
        return listOfLinks

    def PCLoop(self):
        self.MainBingPage()
        for searchItem in self.searchList[1:]:
            self.linkListFile.writelines(searchItem+"\n")
            time.sleep(2.5)
            self.SearchPage(searchItem)
            data = self.GrabLinks()
            self.listfnc.InputLinks(data,self.exception,self.linkListFile)
            time.sleep(2.5)
        self.driver.close()

if __name__ == '__main__':
    bing = AutoBingSearch()
    bing.PCLoop()