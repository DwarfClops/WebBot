import Project.WebSites.Instagram.Query_Hash_Functions as QHF
import Project.WebSites.Instagram.URL_Request_Functions as URF
from Project.Methods import WriteListofLinks
import json
import os

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

class HashScraper():
    def __init__(self,hashtag):
        self.hashtag = hashtag.lower()
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        self.photos = []
        self.Hash_Functions = QHF
        self.Request_Fucntions = URF
        self.Startup()
        for i in self.photos:
            print(i)

    def Startup(self):
        initurl = URF.initialURL(self.hashtag)
        req = self.Request_Fucntions.request_url(initurl, self.header)
        soup = self.Request_Fucntions.makeSoup(req)
        jsData = self.jsonExtract(soup)
        print(jsData)
        end_cursor = jsData['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
        self.end_cursor = end_cursor.replace("==",'')
        print(jsData['entry_data']['TagPage'])
        photodata = jsData['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']
        self.GetPhotoData(photodata)
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
        return main_JS_data

    def EdgePositionData(self,jsData):
        #print(jsData.keys())
        end_cursor = jsData['data']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
        self.end_cursor = end_cursor.replace("==",'')

    #GetPhotoData
    def GetPhotoData(self,photos):
        for pic in photos:
            url = pic['node']['display_url']
            idp = pic['node']['id']
            iduser = pic['node']['owner']
            liked =pic['node']['edge_liked_by']
            p = {'photo':url,'photoid':idp,'likes':liked ,'userid':iduser}
            self.photos.append(p)

    def Get_More_Photos(self):
        req = self.Request_Fucntions.request_more_photos(self.hashId,self.hashtag,self.end_cursor,header=self.header)
        jdata = json.load(req)
        self.EdgePositionData(jdata)
        photos = jdata['data']['hashtag']['edge_hashtag_to_media']['edges']
        self.GetPhotoData(photos)

class ProfileSccraper():
    def __init__(self,profile):
        print(os.listdir)
        self.profile = profile
        profileURL = URF.ProfileUrl(profile)
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        req = URF.request_url(profileURL,self.header)
        soup = URF.makeSoup(req)
        data = self.jsonExtract(soup)
        print(data.keys())
        end_cursor = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        self.end_cursor = end_cursor.replace("==",'')
        print(self.end_cursor)
        self.photodata = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
        self.userID = data['entry_data']['ProfilePage'][0]['graphql']['user']['id']
        self.Get_More_Photos()
        self.WriteData(self.photodata)

    def jsonExtract(self,sOBJ):
        body = sOBJ.find('body')
        first_script = str(body.find('script'))
        raw_str = first_script.split('sharedData =')[1]
        raw_str = raw_str.replace(";</script>",'')
        main_JS_data = json.loads(raw_str)
        scripts = str(body.find_all('script'))
        self.hashId,self.container = QHF.grab_Query_Hash_Script(scripts)
        return main_JS_data

    def Get_More_Photos(self):
        req = URF.Request_User_Photos(self.hashId,self.userID,self.end_cursor,self.header)
        print(req)
        soup = URF.makeSoup(req)
        print(soup)
        jdata = json.load(soup.string)
        print(jdata)
        # self.EdgePositionData(jdata)
        # photos = jdata['data']['hashtag']['edge_hashtag_to_media']['edges']
        # self.GetPhotoData(photos)


    def WriteData(self,photoData):
        photolist = []
        for i in photoData:
            photolist.append(i['node']['display_url'])
        WriteListofLinks(self.profile, photolist)

#HashScraper("Tattoo")
ProfileSccraper("mrioes")