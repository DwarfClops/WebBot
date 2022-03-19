import os
from urllib.request import urlretrieve

def SaveImages(folderName, listOfImages):
    photoPath = "D:\Programs\Python_Programs\WebBot\Project\Photos\\"
    folderitems = os.listdir(photoPath)
    if folderName not in folderitems:
        os.mkdir(photoPath + folderName)
    os.chdir(photoPath + folderName)
    num = os.listdir().__len__()
    for x in listOfImages:
        urlretrieve(x, str(num) + ".jpg")
        num += 1

def WriteListofLinks(fName,data):
    print("Writing Data")
    filePath = "D:\Programs\Python_Programs\WebBot\Project\Links\\"
    fileName = fName+".txt"
    os.chdir(filePath)
    with open(fileName,'w') as workingFile:
        for d in data:
            workingFile.write(d)
            workingFile.write("\n")
        workingFile.close()
    print("Done Writing Data")