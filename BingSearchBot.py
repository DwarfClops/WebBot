import time
from Methods import ListFunctions
from MySeleniumDriver import LoadEdgeWithUserData

class AutoBingSearch():
    def __init__(self):
        self.bingFormTags = {'Search_Bar':'input','mainpage_search_icon':'search_icon','Next_Search':'sb_form_go','Tag_With_Links':'b_content','href':'href','a':'a'}
        self.exception = ['javascript:void(0);','javascript:void(0)']
        self.tags = []
        self.driver = LoadEdgeWithUserData()
        self.searchList = ListFunctions().ReadSearchList()
        self.linkList = ListFunctions().MakeLinkList()

    def MainBingPage(self):
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
        links = body[0].find_elements_by_tag_name(self.bingFormTags['href'])
        listOfLinks = []
        for a in links:
            try:
                data = a.get_attribute(self.bingFormTags['a'])
                listOfLinks.append(data)
            except:
                continue
        return listOfLinks

    def MainLoop(self):
        self.MainBingPage()
        for searchItem in self.searchList[1:]:
            self.linkList.writelines(searchItem+"\n")
            time.sleep(2.5)
            self.SearchPage(searchItem)
            data = self.GrabLinks()
            ListFunctions().InputLinks(data,self.exception,self.linkList)
            time.sleep(2.5)
        self.driver.close()

if __name__ == '__main__':
    bing = AutoBingSearch()
    bing.MainLoop()