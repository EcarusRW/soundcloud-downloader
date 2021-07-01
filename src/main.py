from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://soundcloud.com/%USER%/likes')
try:
    ## Wait for cookies to be clickable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
    )
    driver.find_element_by_id('onetrust-accept-btn-handler').click()

    ## Scroll to bottom
    try:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        loadingElement = driver.find_element_by_class_name('loading')
        while (loadingElement):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            loadingElement = driver.find_element_by_class_name('loading')
            #WebDriverWait(driver,3).until_not(EC.presence_of_element_located((By.CLASS_NAME, 'loading')))
    except:
        print('No more likes')
except TimeoutException:
    print('Closed due time exceeded')