{"filter":false,"title":"scrapping.py","tooltip":"/scrapping.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":41,"column":13},"action":"remove","lines":["import sys","sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')","","import time","import pandas as pd","from bs4 import BeautifulSoup","from selenium import webdriver","import chromedriver_autoinstaller","","# setup chrome options","chrome_options = webdriver.ChromeOptions()","chrome_options.add_argument('--headless') # ensure GUI is off","chrome_options.add_argument('--no-sandbox')","chrome_options.add_argument('--disable-dev-shm-usage')","","# set path to chromedriver as per your configuration","chromedriver_autoinstaller.install()","","# set the target URL","url = \"https://google.com/\"","","# set up the webdriver","driver = webdriver.Chrome(options=chrome_options)","","","from selenium.webdriver.support.ui import WebDriverWait","from selenium.webdriver.support import expected_conditions as EC","from selenium.webdriver.common.by import By","from selenium import webdriver","","URL = \"https://jumafernandez.github.io/soco-web_scraping/data/encuentro-02/formulario.html\"","","# set up the webdriver","driver.get(URL)","","driver.find_element(By.NAME,(\"email\")).send_keys(\"email@gmail.com\")","driver.find_element(By.NAME,(\"passwd\")).send_keys(\"password1123\")","","","","# quit the driver","driver.quit()"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["t"],"id":3},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["e"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["x"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["t"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["o"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["."]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["a"]}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["s"],"id":4},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["d"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["a"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["s"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["d"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["a"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":14},"end":{"row":0,"column":14},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1733254536856,"hash":"78ae3ced318318581678f680d770a2aeb6457342"}