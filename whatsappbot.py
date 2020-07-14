from selenium import webdriver
import time 
chrome_browser = webdriver.Chrome(executable_path='/Users/fatimazahra.chriha/Desktop/Recurse/pomodoro-whatsapp/chromedriver')
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(15)

print('Scanning is completed...')
username_list = ['Pomodoro Bot', 'Whatsapp Bot', 'Mariam Khti']
for username in username_list:
    user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(username))
    user.click()
    message_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message_box.send_keys('Hey, I am your pomodoro bot')
    send_button = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
    send_button.click()