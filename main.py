import os
import time
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from threading import Thread
import requests
import csv

options = Options()
options.set_preference("media.volume_scale", "0.0");

# using webdriver's install_addon API to install the downloaded Firefox extension
service = Service("C:/Users/x79/PycharmProjects/ScrapeJAVHDPORN/geckodriver-v0.30.0-win64/geckodriver.exe")

driver = webdriver.Firefox(service=service, options=options)

class DownloadThread():
    def __init__(self, Thread, parent, url, vid_code, fsize):
        """Constructor"""
        Thread.__init__(self)
        self.fsize = fsize
        self.url = url
        self.parent = parent
        self.vid_code = vid_code
        self.run()
        self.reporthook()

    def run(self):
        local_fname = self.vid_code + ".mp4"
        try:
            urlretrieve(self.url, local_fname, self.reporthook)
        except:
            urlretrieve(self.url, "default.mp4", self.reporthook)

    def reporthook(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = int((readsofar / totalsize) * 100)
        else:  # total size is unknown
            percent = 0
        # Initial call to print 0% progress
        print(percent)


class MainPanel():
    def __init__(self, url, vid_code):
        self.url = url
        self.vid_code = vid_code
        self.download_number = 1
        self.onDownload()

    def onDownload(self):
        """
        Update display with downloading gauges
        """
        try:
            header = requests.head(self.url, allow_redirects=True)
            fsize = int(header.headers["content-length"]) / 1024
            # start thread
            DownloadThread(Thread, self.download_number, self.url, self.vid_code, fsize)
        except Exception as e:
            print()
    def readUrlFromFile(self):
        lines = loadtxt("filename.dat", comments="#", delimiter=",", unpack=False)
        with open('filename.csv', 'r') as fd:
            reader = csv.reader(fd)
            for row in reader:
        # do something
        result =
        return result[]

def main():
    if (len(driver.window_handles) == 1):
        driver.get("https://vlxx.sex/video/duoc-moi-ve-nha-thanh-nien-du-co-dong-nghiep-nguyen-dem-khong-nghi/2149/")
        timeout = 20
        # switch to first tab
        driver.switch_to.window(driver.window_handles[0])
        video_tag = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
        current_resolution = driver.execute_script("return jwplayer().getCurrentQuality()")
        list_resolution = driver.execute_script("return jwplayer().getQualityLevels()")

        if (current_resolution < len(list_resolution) - 1):
            try:
                driver.execute_script("jwplayer().setCurrentQuality(" + int(len(list_resolution) - 1) + ")")
            except Exception as e:
                print()
        driver.execute_script("jwplayer().play()")
        time.sleep(5)
        url_video = video_tag.get_attribute("src")
        video_code = driver.find_element(By.CLASS_NAME, "video-code").get_attribute('innerHTML')
        print(video_code)
        driver.quit()
        MainPanel(url_video, video_code)

if __name__ == "__main__":
    main()
