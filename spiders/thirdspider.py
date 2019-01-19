from selenium import webdriver
import csv

driver = webdriver.Chrome('C:/PythonProjects/chromedriver_win32/chromedriver.exe')

max_page_num = 5
max_page_dig = 3

with open('C:/PythonProjects/commaFeedScraper/results.csv' , 'w') as file:
    file.write("Buyers, Price \n")


for i in range(1, max_page_num + 1):
    page_num = (max_page_dig - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"
    
    driver.get(url)
    
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
    
    num_page_items = len(buyers)
    with open('C:/PythonProjects/commaFeedScraper/results.csv' , 'a') as file:
        for i in range(num_page_items):
            file.write(buyers[i].text + "," + prices[i].text + "\n")
            
driver.close()
    
'''
driver = webdriver.Chrome('C:/PythonProjects/chromedriver_win32/chromedriver.exe')
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

num_page_items = len(buyers)

for i in range(num_page_items):
    print(buyers[i].text + " : " + prices[i].text)
    
driver.close()
'''


