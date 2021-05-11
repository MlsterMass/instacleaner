import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

re = "\033[1;31m"
gr = "\033[1;32m"
login = input(gr + "[+] enter your login : " + re)
password = input(gr + "[+] enter your password : " + re)

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
chrome_options = Options()
notifications = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", notifications)
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=" + user_agent)
chrome_options.add_argument('--lang=en')
chrome_options.add_argument("--start-maximized")
browser = Chrome(executable_path="assets/chromedriver", options=chrome_options)
browser.get("https://instagram.com/")

time.sleep(5)
browser.find_element_by_css_selector('input[name="username"]').send_keys(login)
time.sleep(2)
browser.find_element_by_css_selector('input[name="password"]').send_keys(password)
time.sleep(2)
browser.find_element_by_css_selector('button[type="submit"]').click()
time.sleep(2)
# open tab
browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
time.sleep(2)
browser.get('https://www.instagram.com/adventurer.me')
time.sleep(2)

browser.find_element_by_partial_link_text(' following').click()


def cleaner():
    pop_up_window = WebDriverWait(
        browser, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='isgrP']")))
    browser.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
        pop_up_window)
    time.sleep(1)
    a = 10
    while True:
        browser.find_element_by_xpath(
            f"/html/body/div[5]/div/div/div[2]/ul/div/li[{a}]/div/div[2]/button").click()
        time.sleep(1)
        pop_up_window2 = WebDriverWait(
            browser, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='piCib']/div[3]/button[1]"))).click()
        time.sleep(3)
        a += 1


cleaner()
