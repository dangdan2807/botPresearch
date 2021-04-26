import os
import time
import os.path
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# lấy path đến thư mục bot
current_dir = os.getcwd()
profile_dir = current_dir + "/profile"
url_chrome = current_dir + "/chromedriver.exe"


def docFile(filePath, mode):
    if(path.exists(filePath) == False):
        f = open(filePath, "w+")
        print(filePath + " rỗng")
        return -1
    tempList = []
    if mode == 1:
        tempList = [line.rstrip("\n").split("|")
                    for line in open(filePath, "r", encoding='utf-8')]
    elif mode == 2:
        tempList = [line.rstrip("\n")
                    for line in open(filePath, "r", encoding='utf-8')]
    return tempList


def login():
    driver.get("https://www.presearch.org/login")
    time.sleep(5)
    driver.find_element_by_name("email").send_keys(accList[0][0])
    time.sleep(2)
    driver.find_element_by_name("password").send_keys(accList[0][1])
    return


def guiTungTu(str, element):
    for i in range(0, len(str)):
        element.send_keys(str[i])
        sleep(0.1)
    return


def runAuto(account, dataList):
    option = webdriver.ChromeOptions()
    if path.exists(profile_dir) == False:
        os.rmdir(profile_dir)
    if path.exists(profile_dir) == True:
        option.add_argument("user-data-dir=" + profile_dir + "/" + account[0])

    driver = webdriver.Chrome(options=option)
    driver.set_window_size(375, 667)

    print("run account: ", account[0])
    lastIndex = 30
    for index in range(0, lastIndex):
        lenDataList = len(dataList)
        text = ""
        if index >= lenDataList:
            text = index + "nội dung này không tồn tại"
        else:
            text = dataList[index]

        print("chạy lần ", (index + 1), ":", text)
        driver.get(url="https://www.presearch.org")
        time.sleep(3)

        searchElement = driver.find_element_by_id('search')
        time.sleep(1)

        guiTungTu(text, searchElement)
        time.sleep(1)

        searchElement.send_keys(Keys.ENTER)
        time.sleep(5)
    print("waiting close chrome to 5 second")
    time.sleep(5)
    driver.close()
    return


def main():
    accPath = "data/acc.txt"
    dataPath = "data/text.txt"
    accList = docFile(accPath, 1)
    dataList = docFile(dataPath, 2)

    if(accList == -1 or dataList == -1):
        exit
    elif (not accList or not dataList):
        if not accList:
            print("nhập tk, mk vào trong " + accPath)
            print("dạng: tk|ml")
        else:
            print("danh sách từ khóa trong " + dataPath)
    else:
        lastIndex = len(accList)
        for index in range(0, lastIndex):
            runAuto(accList[index], dataList)
    return

if __name__ == '__main__':
    main()