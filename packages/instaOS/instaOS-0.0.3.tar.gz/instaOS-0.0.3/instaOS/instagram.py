from time import sleep
from os import system,environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm
from logging import getLogger,basicConfig,INFO

class Instagram():
    def __init__(self,username,password,users) -> None:
        FORMAT = '%(asctime)s %(levelname)s %(message)s'
        basicConfig(filename=environ["LOGNAME"], level=INFO,encoding="utf-8",format=FORMAT)
        self.logger = getLogger(__name__)
        self.username=username
        self.logger.info("__init__ func:started")
        self.header()
        self.login(password)
        self.get_followers(user_input=users)
        self.get_following(user_input=users)
        self.logger.info("__init__ func:finished")
        self.exit()

    def header(self):
        self.logger.info("header func:started")
        self.TIMEOUT = 15
        service = Service(executable_path="./chromedriver")
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument("--log-level=3")
        mobile_emulation = {
        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/124.0.6367.91 Mobile Safari/535.19","clientHints": {"platform": "Android", "mobile": True} }
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument("--device-name=Samsung Galaxy S22 Ultra")
        self.bot = webdriver.Chrome(service=service,options=options)
        self.bot.set_page_load_timeout(15)
        self.bot.set_window_size(width=400,height=800)
        self.logger.info("header func:finished")

    def login(self,password):
        self.logger.info("login func started")
        self.bot.get('https://www.instagram.com/accounts/login/')
        sleep(self.TIMEOUT//5)
        try:
            element = self.bot.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/div[2]/button")
            element.click()
        except NoSuchElementException:
            self.logger.error("Instagram did not require to accept cookies this time.")
        self.logger.error("Logging in...")
        username_input = WebDriverWait(self.bot, self.TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password_input = WebDriverWait(self.bot, self.TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button = WebDriverWait(self.bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        self.logger.info("login button clicked")
        login_button.click()
        sleep(self.TIMEOUT)
        self.logger.info("login func finished")

    def get_followers(self,user_input):
        self.logger.info("get_followers func:started")
        self.bot.get(f'https://www.instagram.com/{self.username}/')
        sleep(self.TIMEOUT//5)
        WebDriverWait(self.bot, self.TIMEOUT).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers')]"))).click()
        sleep(self.TIMEOUT//5)
        self.logger.info(f"[Info] - Scraping followers for {self.username}...")
        users = set()
        while len(users) < user_input:
            followers = self.bot.find_elements(By.XPATH, "//a[contains(@href, '/')]")
            for i in followers:
                if i.get_attribute('href'):
                    model=i.get_attribute('href').split("/")
                    users.add(model[3])
                    system("clear")
                    tqdm(range(0,user_input),desc="followers loading:",initial=len(users))
                else:
                    continue
            ActionChains(self.bot).send_keys(Keys.END).perform()
            sleep(self.TIMEOUT//5)
        users = list(users)[:user_input]
        self.logger.info(f"[Info] - Saving followers for {self.username}...")
        with open(f'{self.username}_followers.txt', 'a') as file:
            file.write('\n'.join(users) + "\n")
            file.close()
        self.logger.info("get_followers func:finished")
        
    def get_following(self,user_input):
        self.logger.info("get_following func:started")
        self.bot.get(f'https://www.instagram.com/{self.username}/')
        sleep(self.TIMEOUT//5)
        WebDriverWait(self.bot, self.TIMEOUT).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/following')]"))).click()
        sleep(self.TIMEOUT//5)
        self.logger.info(f"[Info] - Scraping following for {self.username}...")
        users = set()
        while len(users) < user_input:
            followers = self.bot.find_elements(By.XPATH, "//a[contains(@href, '/')]")
            for i in followers:
                if i.get_attribute('href'):
                    model=i.get_attribute('href').split("/")
                    users.add(model[3])
                    system("clear")
                    tqdm(range(0,user_input),desc="following loading:",initial=len(users))
                else:
                    continue
            ActionChains(self.bot).send_keys(Keys.END).perform()
            sleep(self.TIMEOUT//5)
        users = list(users)[:user_input]
        self.logger.info(f"[Info] - Saving following for {self.username}...")
        with open(f'{self.username}_following.txt', 'a') as file:
            file.write('\n'.join(users) + "\n")
            file.close()
        self.logger.info("get_following func:finished")

    def exit(self):
        self.bot.quit()