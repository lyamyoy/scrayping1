from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

driver.quit()