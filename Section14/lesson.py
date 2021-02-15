# ライブラリのインポート
import os
from time import sleep

import pandas as pd
import requests

IMAGE_DIR = './images/'

# CSVの読み込み
df = pd.read_csv('image_urls_20210215.csv')

if os.path.isdir(IMAGE_DIR):
  print('既存')
else:
  os.makedirs(IMAGE_DIR)

# 画像の保存
for file_name, yahoo_image_url in zip(df.filename[:5], df.yahoo_img_url[:5]):
  image = requests.get(yahoo_image_url)
  with open(IMAGE_DIR + file_name + '.jpg', 'wb') as f:
    f.write(image.content)

  sleep(2)