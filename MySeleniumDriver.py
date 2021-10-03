from msedge.selenium_tools import Edge, EdgeOptions
import os


def LoadEdgeWithUserData():
    UserName = os.getlogin()
    path = "edgedriver_win32\\msedgedriver.exe"
    UserProfilePath = "C:\\Users\\{}\\AppData\\Local\\Microsoft\\Edge\\User Data".format(UserName)
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument(UserProfilePath)
    edge_options.add_argument("profile-directory=Profile 1")
    driver = Edge(options=edge_options, executable_path=path)
    driver.get("https://www.bing.com")
    return driver