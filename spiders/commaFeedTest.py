from selenium import webdriver
import csv
import time

#enter webdriver location
driver = webdriver.Chrome('C:/PythonProjects/chromedriver_win32/chromedriver.exe')
#select web domain to scrape from
driver.get("https://www.commafeed.com/#/welcome")
#find username and password inputs
username = driver.find_element_by_xpath('//input[@name="username"]')
password = driver.find_element_by_xpath('//input[@name="password"]')
#write to username and password inputs
username.send_keys("") #USER INPUT
password.send_keys("") #USER INPUT
#find submit and click
driver.find_element_by_xpath('//input[@type="submit"]').click()
#Get the entry list of CommaFeed
driver.get("https://www.commafeed.com/#/feeds/view/category/all")
#Expand the view by clicking
driver.find_element_by_xpath('//a[@title="Expanded view"]').click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)# to let CommaFeed load while scrolling
#variables setup for scraping
pTitle = driver.find_elements_by_xpath('//*[@class="entry-title"]')
inside = driver.find_elements_by_xpath('//*[@class="entry-body-content"]/div/table/tbody/tr/td[2]/p')
'''
pVendor = driver.find_elements_by_xpath('//*[@class="entry-title"]')
pType = driver.find_elements_by_xpath('//*[@class="entry-title"]')
pPrice = driver.find_elements_by_xpath('//*[@class="entry-title"]')
'''

num_pTitle = len(pTitle)
num_inside = len(inside)

for i in range(num_pTitle): 
    print(str(i) + ": " + pTitle[i].text + ", " + inside[i].text + "\n")    
    
    
driver.close()