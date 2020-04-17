from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

filename = 'mos_ru_news.csv'
driver = webdriver.Chrome()
driver.get('https://www.mos.ru/news/')

try:
    for i in range(1):
        element = driver.find_element_by_xpath("//a[@class='mos-button']")
        element.click()
        time.sleep(3)
except Exception as e:
    print(e)


soup = BeautifulSoup(driver.page_source, 'html.parser')
data = pd.DataFrame(columns=['Date', 'News', 'Class', 'Link', 'Text', 'Page'])

all_news = soup.find_all('main-news')[0]


links_to_parse = []

for link in all_news.find_all('a', {'class': 'commonCard__link'}):
    links_to_parse.append('https://www.mos.ru/' + link['href'])
    

text_arr = []
html_arr = []

for url in links_to_parse:
    driver.get(url)
    time.sleep(2)
    
    text = driver.find_element_by_class_name('news-article-content').text
    
    text_arr.append(text)
    html_arr.append(driver.page_source)

ind = 0

for news in all_news.find_all('div', {'class': 'commonCard'}):
    t = news.findChildren('span', {'class': "commonCard__title"} , recursive=True)
    add = list(news.findChildren('span', {'class': "extraList__item"} , recursive=True))
    
    try:
        data.loc[ind] = {'Date': add[0].text.rstrip('\n'), 'News': t[0].text.rstrip('\n'), 'Class': add[1].text.rstrip('\n'), 'Link': links_to_parse[ind], 'Text': text_arr[ind], 'Page': html_arr[ind]}
    except:
        pass
    
    data.to_csv(filename, index=False)
    ind += 1

