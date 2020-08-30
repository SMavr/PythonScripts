import os
from selenium import webdriver


def run():
    """ Run """
    chromedriver_path = r'chromedriver.exe'
    os.environ['webdriver.chrome.driver'] = chromedriver_path
    browser = webdriver.Chrome(chromedriver_path)
    browser.get('https://www.youtube.com/results?search_query=rembetiko')
    ##link_elem = browser.find_element_by_link_text('Οικονομία')
    # link_elem.click()
    # browser.quit()

if __name__ == "__main__":
    run()
