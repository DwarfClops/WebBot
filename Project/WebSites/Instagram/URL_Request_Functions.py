from urllib import request
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
