from msedge.selenium_tools import Edge, EdgeOptions
import os


def LoadEdgeWithUserData():
    UserName = os.getlogin()
    path = "../../edgedriver_win32/msedgedriver.exe"
    UserProfilePath = "--user-data-dir=C:\\Users\\{}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default".format(UserName)
    print(UserProfilePath)
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument(UserProfilePath)
    edge_options.add_argument("profile-directory=Profile 1")
    driver = Edge(options=edge_options, executable_path=path)
    return driver