from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException

from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:\development\chromedriver.exe"

SIMILAR_ACCOUNT = "chefstablenetflix"
USERNAME = INSTAGRAM_USERNAME
PASSWORD = INSTAGRAM_PASSWORD

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        accept_cookies = self.driver.find_element_by_css_selector(".bIiDR")
        accept_cookies.click()

        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)

        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        time.sleep(2)

        enter = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        enter.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)

        open_followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        open_followers.click()
        time.sleep(2)

        for i in range(10):
            time.sleep(1)
            scroll_down = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_down)



    def follow(self):
        time.sleep(2)
        follow = self.driver.find_elements_by_css_selector(".y3zKF")
        for i in follow:
            try:
                time.sleep(2)
                i.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()



insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()