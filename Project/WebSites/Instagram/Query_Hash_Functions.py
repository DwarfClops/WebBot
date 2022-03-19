from urllib import request

def grab_Query_Hash_Script(script_tag):
    scripts = script_tag.split(",")
    # print(scripts)
    # print(scripts.__len__())
    for i in scripts:
        if ("TagPageContainer.js" in i):
            #print(i)
            pageContainer = i.split(":")[1]
            pageContainer = pageContainer.replace("\"", '')
            pageContainerUrl = "https://www.instagram.com" + pageContainer
            #print(pageContainerUrl)
            container = pageContainerUrl
            break
    hashId = grab_Query_Hash(pageContainerUrl)
    return hashId,container


def grab_Query_Hash(url):
    blob = request.urlopen(url)
    for i in blob:
        if (str(i).find('queryId:') > 0):
            querystring = i
    return str(querystring).split('queryId:')[1].split(',')[0].replace("\"", '')