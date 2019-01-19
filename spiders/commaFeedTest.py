from selenium import webdriver
import csv
import time

with open('C:/PythonProjects/commaFeedScraper/CompetitorStores.csv' , 'w') as file:
    file.write("Pnum,Title,Source,Link,Vendor,Type,Price,Date\n")

driver = webdriver.Chrome('C:/PythonProjects/chromedriver_win32/chromedriver.exe') #enter webdriver location

driver.get("https://www.commafeed.com/#/welcome") #select web domain to scrape from
           
username = driver.find_element_by_xpath('//input[@name="username"]') #find username and password inputs
password = driver.find_element_by_xpath('//input[@name="password"]')

username.send_keys("salemstrider") #USERNAME INPUT
password.send_keys("yeetusfiend1") #PASSWORD INPUT

driver.find_element_by_xpath('//input[@type="submit"]').click() #find submit and click

driver.get("https://www.commafeed.com/#/feeds/view/category/all") #Get the entry list of CommaFeed
           
driver.find_element_by_xpath('//a[@title="Expanded view"]').click() #Expand the view by clicking

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #infinite scroll down

time.sleep(5)# to let CommaFeed load while scrolling

pTitle = driver.find_elements_by_xpath('//*[@class="entry-title"]/a') #variables setup for scraping
source = driver.find_elements_by_xpath('//*[@class="entry-source ng-scope"]/a')
inside = driver.find_elements_by_xpath('//*[@class="entry-body-content"]/div/table/tbody/tr/td[2]/p')
uploadDate = driver.find_elements_by_xpath('//*[@class="entry-date ng-binding"]')

def splitAtr(pList):
    list1 = pList.split("\n")
    list2 = []
    for x in list1: 
        y = x.replace('Vendor: ', '').replace('Type: ', '').replace('Price: ', '').replace(',','')
        list2.append(y)
    return list2

#print(source.text)

num_pTitle = len(pTitle)
num_inside = len(inside)

with open('C:/PythonProjects/commaFeedScraper/CompetitorStores.csv' , 'a') as file:
    for i in range(num_pTitle): 
        #print(str(i) + "\n" + pTitle[i].text + "\n" + source[i].text + "\n" + pTitle[i].get_attribute('href') + "\n" + splitAtr(inside[i].text)[0] + "\n"
        #      + splitAtr(inside[i].text)[1] + "\n" + splitAtr(inside[i].text)[2] + "\n" + uploadDate[i].text + "\n") 
        file.write(str(i) + "," + pTitle[i].text.replace(",","") + "," + source[i].text +"," + pTitle[i].get_attribute('href') + "," + splitAtr(inside[i].text)[0] + ","
                   + splitAtr(inside[i].text)[1] + "," + splitAtr(inside[i].text)[2] + "," + uploadDate[i].text + "\n")
    print("Done.")    
    

driver.close()
