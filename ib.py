from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import getpass
import eel

eel.init('web')

@eel.expose
def instaBot(uname, pwd, tag):
    #uname = str(input("Username: "))
    #pwd = getpass.getpass("Password: ")
    #tag = str(input("Which hashtag do you want to try today: "))
    options = Options()
    options.add_argument('user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com")
    time.sleep(5)
    searchbox = driver.find_element_by_name('username')
    searchbox.send_keys(uname)
    searchbox = driver.find_element_by_name('password')
    searchbox.send_keys(pwd)
    searchbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
    searchbutton.click()
    time.sleep(3)
    searchbutton = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    searchbutton.click()
    time.sleep(7)
    driver.get("https://www.instagram.com/explore/tags/" + tag)
    time.sleep(5)

    hrefs = driver.find_elements_by_tag_name('a')
    pichrefs = [elem.get_attribute('href') for elem in hrefs]
    
    z = []
    for pichref in pichrefs:
        if ".com/p/" in pichref:
            z.append(pichref)

    for i in z:
        driver.get(i)
        try:
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            time.sleep(5)
        except Exception as e:
            time.sleep(2)

#eel.start('index.html', size=(1000, 600))
eel.start('index.html')
#if __name__ == '__main__':
#    while True:
#        query = str(input("What do you want to do? "))
#        query = query.lower()
#        
#        if "instagram" in query:
#            instaBot()
#        
#        elif "exit" in query:
#            exit()