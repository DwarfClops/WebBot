import Project.WebSites.Instagram.Query_Hash_Functions as QHF
import Project.WebSites.Instagram.URL_Request_Functions as URF
import json

#InstaGram scraper Script
#uses two objects
#one for InstaGram profiles (InstaScraper)
#another for HashTags (HashScraper)
#both objects are similar with some differences in grabbing the json data and query strings
#this progam works using the urllib library (request)
####this is to get the initial page (profile or hashtag)
####Instagram only loads so many photos at start, to grab more photos request must be sent to the server
####additional request to grab more photos are done through sending graphql queries
#json and beautifulSoup are used for sorting data

class InstagramScraper():
    def __init__(self,hashtag):
        self.hashtag = hashtag.lower()
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        self.photos = []
        self.Hash_Functions = QHF
        self.Request_Fucntions = URF

    def Startup(self):
        initurl = URF.initialURL(self.hashtag)
        req = self.Request_Fucntions.request_url(initurl, self.header)
        soup = self.Request_Fucntions.makeSoup(req)
        jsData = self.jsonExtract(soup)
        end_cursor = jsData['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
        self.end_cursor = end_cursor.replace("==",'')
        print(self.end_cursor)
        photodata = jsData['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']
        self.CreatePostData(photodata)
        self.jsData = jsData

    def jsonExtract(self,sOBJ):
        print(sOBJ)
        body = sOBJ.find('body')
        first_script = str(body.find('script'))
        raw_str = first_script.split('sharedData =')[1]
        raw_str = raw_str.replace(";</script>",'')
        main_JS_data = json.loads(raw_str)
        scripts = str(body.find_all('script'))
        self.hashId,self.container = self.Hash_Functions.grab_Query_Hash_Script(scripts)
        print(main_JS_data)
        return main_JS_data

    def EdgePositionData(self,jsData):
        print(jsData.keys())
        end_cursor = jsData['data']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
        self.end_cursor = end_cursor.replace("==",'')

    def CreatePostData(self,photos):
        for pic in photos:
            url = pic['node']['display_url']
            idp = pic['node']['id']
            iduser = pic['node']['owner']
            liked =pic['node']['edge_liked_by']
            p = {'photo':url,'photoid':idp,'likes':liked ,'userid':iduser}
            print(p)
            self.photos.append(p)

    def Get_More_Photos(self):
        req = self.Request_Fucntions.request_more_photos(self.hashId,self.hashtag,self.end_cursor,header=self.header)
        jdata = json.load(req)
        self.EdgePositionData(jdata)
        photos = jdata['data']['hashtag']['edge_hashtag_to_media']['edges']
        self.CreatePostData(photos)