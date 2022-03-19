import pyautogui
from Project.WebSites.Bing.Methods import ListFunctions
import time

class BingCellSearch():
    def __init__(self):
        listfnc = ListFunctions()
        self.searchList = listfnc.ReadSearchList()
        while True:
            a = input("place pointer in terminal place mouse cursor at local and hit enter")
            points = pyautogui.position()
            print(points)
            if points:
                self.points = points
                break
            else:
                print("nope")

    def EnterSearches(self):
        pyautogui.moveTo(self.points)
        for word in self.searchList:
            pyautogui.click()
            pyautogui.hotkey('ctrl','a')
            pyautogui.write(word)
            pyautogui.press("enter")
            time.sleep(2.5)

a = BingCellSearch()
a.EnterSearches()