
#####   Here you can edit the config:    #####

#Here you can change the count of threads. If you have more threads than the program will finish faster!
number_threads = 10

#Here you can change if you want to use proxies. Make sure the boolean is set to True if the poll uses ip check.
use_proxies = False

#Change this number if you not using proxies.
number_of_votes = 100

#Change this to your strawpoll url. For example: strawpoll_url = "https://www.strawpoll.me/12345678"
strawpoll_url = ""

#Just replace the xxx after the hyphen with the options name
options_id = "field-options-xxx"

#Change this boolean to True if you want to load the pictures. Make shure this boolean is set to False if you using proxies to make the site load faster.
load_pictures = False

#####   Do not change the code below otherwise it may not work probably!    #####



import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

import time
from selenium import webdriver
import selenium
import urllib.request
import socket
import urllib.error
from threading import Thread

usedproxys = list()

votes = 0
def bot(i):
    f = open("proxies.txt", "r")
    for x in f:
        if x in usedproxys:
            return
        else:
            usedproxys.append(x)
        try:
            chrome_options = webdriver.ChromeOptions()
            if not load_pictures:
                prefs = {"profile.managed_default_content_settings.images": 2}
                chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(chrome_options=chrome_options) # Optional argument, if not specified will search path.
            webdriver.DesiredCapabilities.CHROME['proxy'] = {
                "httpProxy":x,
                "ftpProxy":x,
                "sslProxy":x,
                "noProxy":[],
                "proxyType":"MANUAL"
            }
            driver.set_page_load_timeout(30)
            driver.get(strawpoll_url);
            time.sleep(0.5)

            driver.find_element_by_id(options_id).click()


            driver.find_element_by_xpath("//button[@type='submit']").click()

            time.sleep(1) # Let the user actually see something!
                    
            votes = votes + 1
            print("Successfully voted! (" + str(votes) + ")")
            time.sleep(0.1)
            driver.close()
        except Exception as e:
            print(e)
            driver.close()

def bot_no_proxies(i):
    global votes
    for x in range(number_of_votes):
        try:
            chrome_options = webdriver.ChromeOptions()
            if not load_pictures:
                prefs = {"profile.managed_default_content_settings.images": 2}
                chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(chrome_options=chrome_options) # Optional argument, if not specified will search path.
            driver.set_page_load_timeout(30)
            driver.get(strawpoll_url);
            time.sleep(0.5)

            driver.find_element_by_id(options_id).click()


            driver.find_element_by_xpath("//button[@type='submit']").click()

            time.sleep(1) # Let the user actually see something!
                    
            votes += 1
            print("Successfully voted! (" + str(votes) + ")")
            time.sleep(0.1)
            driver.close()
        except Exception as e:
            print(e)
            driver.close()

if not strawpoll_url:
    print("No url was set!")
    strawpoll_url = input("Enter the url: ")
    if not strawpoll_url:
        print("Wrong url!")
        exit()

if use_proxies:
    for i in range(number_threads):
        t = Thread(target=bot, args=(i,))
        t.start()
        time.sleep(1)
else:
    for i in range(number_threads):
        t = Thread(target=bot_no_proxies, args=(i,))
        t.start()
        time.sleep(1)