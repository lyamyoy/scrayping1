from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_path = r'C:\Users\Shunsuke Kawase\Documents\scrayping\ScrapingBeginner-main\chromedriver.exe'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path,options=options)

url = 'https://search.yahoo.co.jp/image'
driver.get(url)

sleep(3)

query = 'プログラミング'
search_box = driver.find_element_by_class_name('SearchBox__searchInput')
search_box.send_keys(query)
search_box.submit()

sleep(3)

height = 1000
while height < 3000:
  driver.execute_script("window.scrollTo(0, {});".format(height))
  height += 100
  print(height)

  sleep(1)

# 画像の要素選択
elements = driver.find_elements_by_class_name('sw-Thumbnail')

d_list = []
# 要素からURLを取得する
for i, element in enumerate(elements, start=1):
  name = f'{query}_{i}'
  raw_url = element.find_element_by_class_name('sw-ThumbnailGrid__details').get_attribute('href')
  yahoo_image_url = element.find_element_by_tag_name('img').get_attribute('src')
  title = element.find_element_by_tag_name('img').get_attribute('alt')

  d = {
    'filename':name,
    'raw_url':raw_url,
    'yahoo_img_url':yahoo_image_url,
    'title':title
  }

  d_list.append(d)

  sleep(1)

df = pd.DataFrame(d_list)
df.to_csv('image_urls_20210215.csv',encoding='utf-8-sig')

driver.quit()