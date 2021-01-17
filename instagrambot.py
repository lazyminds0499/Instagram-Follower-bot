from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

USER_NAME = "nky7988@gmail.com"
PASSWORD = "7988nky@#0"
similar_account = "chefsteps"


class InstaFollower:
    def __init__(self):
        self.chrome_drive_path = "C:/Users/Nitin/Development/chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path=self.chrome_drive_path, options=self.options)
        self.driver.get("https://www.instagram.com/")
        self.login()
        self.find_followers()
        self.follow()

    def login(self):
        time.sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USER_NAME)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        not_now_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()
        time.sleep(2)
        notification_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification_button.click()

    def find_followers(self):
        time.sleep(2)
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(similar_account)
        search.send_keys(Keys.ENTER)

        time.sleep(2)
        required_account = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')
        required_account.click()

        time.sleep(3)
        followers_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        time.sleep(5)

    def follow(self):
        follow_button = self.driver.find_elements_by_css_selector("._1XyCr .soMvl button")[:20]
        for button in follow_button:
            button.click()