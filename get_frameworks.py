from bs4 import BeautifulSoup
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from selenium import webdriver
import os

parent_dir = "C:/Users/mavbe/Desktop/Coding Folder/Frameworks/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bairesdev.com/blog/top-100-development-frameworks/")
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
for o in soup.find_all("ol"):
	for l in o.find_all('li'):
		for s in l.find_all('span'):
			file_name = s.text.replace(chr(0xa0),'').strip().replace(' ', '_').replace('/','_')
			path = os.path.join(parent_dir,file_name)
			os.mkdir(path)