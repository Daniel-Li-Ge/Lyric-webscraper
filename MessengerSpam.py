import pyautogui, time
import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def gooiie():
    N_a_Ar = []
    s_name_in = input("Input song name: ")
    s_name = '\"'+ s_name_in + '\"'
    N_a_Ar.append(s_name)
    N_a_Ar.append(input("Artist Name: "))
    return N_a_Ar

def lyric_finder(anlist):
    browser = webdriver.Chrome("C:\\Users\\danie\\Desktop\\repo\\chromedriver83.exe")
    browser.get("https://www.azlyrics.com/")
    searchBar = browser.find_element_by_id("q")
    searchBar.send_keys(anlist[0], ' ', anlist[1])
    searchBar.send_keys(Keys.ENTER)
    try:
        main = WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.LINK_TEXT, anlist[0]))
        )
        link_elem = main.get_attribute('href')
        main.click()
    except:
        browser.quit()
        fail = "failed to find song"
        return fail

    re_obj = requests.get(link_elem)
    soup = BeautifulSoup(re_obj.text, 'html.parser')
    lyrics = soup.body.findAll('div')[20].text.split('\n')
    return lyrics


    
#     # block = browser.find_element_by_xpath("//div[@class='container main-page']")
#     # block = browser.find_element_by_xpath("//div[@class='row']")
#     # block = browser.find_element_by_xpath("//div[@class='col-xs-12 col-lg-8 text-center']")
#     # block = browser.find_element_by_xpath("//div[5]") 
def spammer(lyrics):
    for line in lyrics:
        pyautogui.typewrite(line)
        pyautogui.press("enter")

spammer(lyric_finder(gooiie()))
time.sleep(2)


# url = 'https://www.azlyrics.com/lyrics/jid/never.html'

# obj = requests.get(url)

# soup = BeautifulSoup(obj.text, 'html.parser')
# liter = soup.body.findAll('div')[20].text.split('\n')

# for line in liter:

#     print(line)










