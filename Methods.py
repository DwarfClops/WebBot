class ListFunctions():
    def __init__(self):
        return None

    def ReadSearchList(self,):
        listSting = "SearchList.txt"
        listFile = open(listSting,'r')
        data = listFile.readlines()
        data = list(map(lambda d: d.strip(), data))
        return data

    def MakeLinkList(self):
        fileName = 'ListofLinks.txt'
        listFile = open(fileName,'w')
        return listFile

    def InputLinks(self,data,exceptions,linkFile):
        for d in data:
            if d in exceptions:
                continue
            try:
                linkFile.writelines(d+"\n")
            except:
                continue