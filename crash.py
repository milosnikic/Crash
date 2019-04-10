from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button
from util.mouse import click_points
from util.scrape import write_features
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome(chrome_options=options)

# Creating web driver object
driver = webdriver.Firefox(executable_path="./geckodriver")
url = 'https://www.wtfskins.com/login/'
driver.get(url)

# Method will wait 10secs so we dont need to wait at all here
click_points()

for i in range(339471, 339551):
    url = 'https://www.wtfskins.com/crash/history/round/' + str(i)
    driver.get(url)

    source_html = driver.page_source
    write_features(html=source_html)
    print("One page scraped!")
print("Done")
