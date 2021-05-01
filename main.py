import os
import time
import os.path
import random
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# lấy path đến thư mục bot
_currentDir = os.getcwd()
_profileDir = _currentDir + "/profile"
_chromePath = _currentDir + "/chromedriver.exe"
_wordList = ["tình", "yêu", "màu", "hồng", "vĩnh", "cửu", "kiếp", "duyên", "không", "thành", "hướng",
                "dương", "kẹo", "bông", "gòn", "sài", "em", "băng", "qua", "đường", "quyền", "nhớ", "người",
                "hay", "ta", "nửa", "đời", "âu", "sầu", "hoa", "vàng", "tàn", "nay", "họ", "ai", "mất", "rồi",
                "ngày", "phận", "lỡ", "làng", "ngàn", "thương", "về", "đâu", "dù", "anh", "có", "khóc", "lần",
                "nước", "chảy", "trôi", "bạn", "diệu", "kỳ", "mộng", "mơ", "bình", "yên", "nơi", "cùng", "kết",
                "rồi", "đấy", "từ", "mà", "ra", "quay", "lại", "thanh", "niên", "thê", "lương", "hôm", "tôi",
                "buồn", "chỉ", "là", "nhau", "khó", "vẽ", "nụ", "cười", ""]


def docFile(filePath, mode):
    if(path.exists(filePath) == False):
        f = open(filePath, "w+")
        print("tệp " + filePath + " rỗng")
        return -1
    tempList = []
    if mode == 1:
        tempList = [line.rstrip("\n").split("|")
                    for line in open(filePath, "r", encoding='utf-8')]
    elif mode == 2:
        tempList = [line.rstrip("\n")
                    for line in open(filePath, "r", encoding='utf-8')]
    return tempList


def login(username, password):
    driver.get("https://www.presearch.org/login")
    time.sleep(5)

    emailElement = driver.find_element_by_name("email")
    guiTungTu(emailElement, username)
    time.sleep(2)
    
    passwordElement = driver.find_element_by_name("password")
    guiTungTu(passwordElement, password)
    return


def guiTungTu(str, element):
    for i in range(0, len(str)):
        element.send_keys(str[i])
        time.sleep(0.2)
    return


def randomWord(dataList, size):
    return ' '.join(random.choice(dataList) for i in range(size))


def demNguoc(i, message = "!"):
    t = time.time()
    for x in range(i, 0, -1):
        sys.stdout.write(
            "[%s] Waiting %s seconds %s\r "
            % (time.strftime("%H:%M:%S", time.localtime(t)), x, message)
        )
        time.sleep(1)


def runAuto(account, dataList):
    username = account[0]
    password = account[1]
    option = webdriver.ChromeOptions()
    if path.exists(_profileDir) == False:
        os.rmdir(_profileDir)
    if path.exists(_profileDir) == True:
        option.add_argument("user-data-dir=" + _profileDir + "/" + username)

    driver = webdriver.Chrome(options=option)
    driver.set_window_size(375, 667)

    print("run account: ", username)
    # login(username, password)
    # input("enter: ")
    lastIndex = 30
    lenDataList = len(dataList)
    for index in range(0, lastIndex):
        text = ""
        if index >= lenDataList or not dataList[index]:
            print("tạo từ ngẫu nhiên")
            text = randomWord(_wordList, 4)
        else:
            text = randomWord(dataList, 1)
        
        print("chạy lần ", (index + 1), ":", text)
        driver.get(url="https://www.presearch.org")
        demNguoc(3)

        searchElement = driver.find_element_by_id('search')
        time.sleep(1)

        guiTungTu(text, searchElement)
        time.sleep(1)

        searchElement.send_keys(Keys.ENTER)
        demNguoc(5, "and continue")
    demNguoc(5, "to close chrome")
    driver.close()
    return


def main():
    accPath = "data/acc.txt"
    dataPath = "data/text.txt"
    accList = docFile(accPath, 1)
    dataList = docFile(dataPath, 2)

    if(accList == -1 or dataList == -1):
        exit
    elif not accList:
        print("nhập tk, mk vào trong " + accPath)
        print("dạng: tk|ml")
    else:
        lastIndex = len(accList)
        for index in range(0, lastIndex):
            runAuto(accList[index], dataList)
    return


if __name__ == '__main__':
    main()
