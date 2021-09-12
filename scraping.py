import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time




driver = webdriver.Chrome(executable_path='C:/Users/adisu/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://www.tokopedia.com/samsung/product')

#scroll til bottom of page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#analize the html page to find element that will be used as data selector
content = driver.page_source
soup = BeautifulSoup(content, features='html.parser')

#wait til all content loaded
time.sleep(3)
#close selenium webdriver
driver.close()

#create empty list
name_res = []
price_res = []
sold_res = []

for ph_name in soup.find_all(attrs='css-33bcxk'): #parent class
    name = ph_name.find(attrs='css-1f4mp12') #child class,
    if name not in name_res:
        name_res.append(name.text) #append the result in text format

for ph_name in soup.find_all(attrs='css-33bcxk'):
    price = ph_name.find(attrs='css-rhd610') #this attrs contain product price
    if price not in price_res:
        price_res.append(price.text)

for ph_name in soup.find_all(attrs='css-33bcxk'):
    sold = ph_name.find(attrs='css-vogbyu') # this attrs contain sold number
    if sold not in sold_res:
        sold_res.append(sold.text)

df = pd.DataFrame({'name': name_res, 'price': price_res, 'sold': sold_res})
df.to_csv('samsung_phone.csv', index=False, encoding='utf-8') #save to .csv
print(df.head(), '\n')
print(df.info())