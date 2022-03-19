from urllib import request
from urllib.parse import urlencode
from bs4 import BeautifulSoup

def initialURL(hashtag):
    url = 'https://www.instagram.com/explore/tags/' + hashtag
    return url

def request_url(url, header):
    init = request.Request(url, headers= header)
    req = request.urlopen(init)
    return req

def makeSoup(req):
    soup = BeautifulSoup(req, 'html.parser')
    return soup

def request_more_photos(hashId, hashtag, end_cursor, header):
    requeststring = "https://www.instagram.com/graphql/query/?query_hash="+hashId+"&variables=%7B%22tag_name%22%3A%22"+hashtag+"%22%2C%22first%22%3A"+"12"+"%2C%22after%22%3A%22"+end_cursor+"%3D%3D%22%7D"
    print(requeststring)
    initreq = request.Request(requeststring,headers=header)
    req = request.urlopen(initreq)
    return req

# for user profile https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables={"id":"689133468","first":12,"after":"QVFEaUl1dTQ4ZUc3TXZCRkEwYXFrWG9qRUFabWV4V3hrY2drTFJyY1p1NTktN2hvWktwNG1IX01xbW50SU04cHI3OUJSbzhROWpMSy1ZUXN5OHpaa2RRbw=="}
def Request_User_Photos(queryhash,userId,end_cursor,header):
    url = "https://www.instagram.com/graphql/query/?query_hash="+"8c2a529969ee035a5063f2fc8602a0fd"+"&variables={\"id\":\""+userId+"\",\"first\":12,\"after\":\""+end_cursor+"==\"}"
    print(url)
    req = request.Request(url,headers=header)
    photos = request.urlopen(req)
    return photos

def ProfileUrl(profile):
    query = {"utm_source":"ig_seo","utm_campaign":"profiles","utm_medium":""}
    data = urlencode(query)
    #https://www.instagram.com/aselcebloger/?utm_source=ig_seo&utm_campaign=profiles&utm_medium=
    url = "https://www.instagram.com/"+profile+"/?"+data
    print(url)
    return url

