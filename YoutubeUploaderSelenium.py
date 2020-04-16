from selenium import webdriver
import pyautogui
from getpass import getpass
import time

'''
URL = ['https://studio.youtube.com/channel/UC-Vpcs3DXBBB2fJn80Jq-8A']
EMAIL = ['trendingclock@gmail.com']
PASSWORD = ['BncLR10!']
'''

driver = webdriver.Chrome("/Users/teoscomputer/src/chromedriver")
     
def logIn(url, email, password):
    driver.get(url)
    time.sleep(1)
    emailIn = driver.find_element_by_xpath('//*[@id="identifierId"]')
    emailIn.send_keys(email)
    nextBtn = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
    nextBtn.click()
    time.sleep(1)
    passwordIn = driver.find_element_by_xpath('//input[@class="whsOnd zHQkBf"]')
    passwordIn.send_keys(password)
    nextBtn2 = driver.find_element_by_xpath('//span[@class="RveJvd snByac"]')
    nextBtn2.click()
    time.sleep(1)
    try:
        confirm = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/span/span')
        confirm.click()
    except:
        pass

promo = False
public = False

def upload(file, title, description, promotion, public):
    #driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    upload = driver.find_element_by_xpath('//*[@id="upload-icon"]')
    upload.click()
    time.sleep(1)
    select = driver.find_element_by_xpath('//*[@id="select-files-button"]/div')
    select.click()
    time.sleep(1)
    #pyautogui.click()
    #time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.typewrite(file)
    time.sleep(1)
    for x in range(2):
        pyautogui.press('tab')
    pyautogui.press('1')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(title)
    time.sleep(1)
    for x in range(2):
        pyautogui.press('tab')
    pyautogui.typewrite(description)
    time.sleep(1)
    ageBtn = driver.find_element_by_xpath('//*[@id="made-for-kids-group"]/paper-radio-button[2]')
    ageBtn.click()
    if(promotion == True):
        #may need clause before to activate 
        promoBtn = driver.find_element_by_xpath('//*[@id="paper-checkbox"]')
        promobtn.click
    nextBtn = driver.find_element_by_xpath('//*[@id="next-button"]/div')
    nextBtn.click()
    time.sleep(1)
    nextBtn.click()
    time.sleep(2)
    if (public == True):
        publicBtn = driver.find_element_by_xpath('//*[@id="privacy-radios"]/paper-radio-button[1]')
        publicBtn.click()
    else:
        publicBtn = driver.find_element_by_xpath('//*[@id="privacy-radios"]/paper-radio-button[3]')
        publicBtn.click()
    time.sleep(1)
    finishedProcessing()
    publish = driver.find_element_by_xpath('//*[@id="done-button"]')
    publish.click()
    
def finishedProcessing():
    processing = driver.find_element_by_xpath('//*[@id="dialog"]/div/ytcp-animatable[2]/div/div[1]/ytcp-video-upload-progress/span')
    if(processing.text == 'Finished processing'):
        print('Processing completed!')
    else:
        time.sleep(2)
        print('Processing...')
        finishedProcessing()