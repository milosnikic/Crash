from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button
from util.mouse import click_points
from util.scrape import write_features
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options,
                          executable_path="./chromedriver")

# Creating web driver object
# driver = webdriver.Firefox(executable_path="./geckodriver")
# driver = webdriver.PhantomJS()
url = 'https://www.wtfskins.com/login/'
driver.get(url)

# Method will wait 10secs so we dont need to wait at all here
# this is hardcoded to click on specific points on screen
# Instead of doing this we will use Selenium and navigating
# click_points()
elements = driver.find_elements_by_class_name('form-check-input')

# Click on terms agreed checkboxes
for element in elements:
    element.click()

# Click on enter button
enter_button = driver.find_element_by_class_name('enter-button')
enter_button.click()
# Scrape login page and save it to file
# with open('login.html', 'w') as f:
#     f.write(driver.page_source)

# Main program that scrapes pages
for i in range(339551, 339552):
    url = 'https://www.wtfskins.com/crash/history/round/' + str(i)
    driver.get(url)

    source_html = driver.page_source
    write_features(html=source_html)
    print("One page scraped!")
print("Done")
