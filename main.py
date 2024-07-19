import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting up beautiful soup
url = 'https://myanimelist.net/topmanga.php'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Set up Selenium WebDriver
driver = webdriver.Firefox()
driver.get(url)

# Privacy
WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'css-47sehv')]"))
).click()

# hover over the trigger element
hover_trigger = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, 'a.hoverinfo_trigger.fl-l.ml12.mr8'))
)
ActionChains(driver).move_to_element(hover_trigger).perform()

# Wait for the div to be visible after hover
hover_info_div = WebDriverWait(driver, 10).until(
	EC.visibility_of_element_located((By.ID, 'info2'))
)

for item in soup.select('.ranking-list'):
	print(item.h3.text.strip())
	print(item.find('div', class_='information di-ib mt4').text.strip())
	print(item.find('div', class_='js-top-ranking-score-col di-ib al').text.strip())
	print(item.find('div', id='info2', class_='hoverinfo-contaniner'))
	print(hover_info_div.text.strip())
