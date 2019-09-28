import config
from selenium import webdriver
import pyotp


totp = pyotp.TOTP(config.otpkey)
browser = webdriver.Chrome()
browser.get(config.site)


def login_sele():
    username_box = browser.find_element_by_id("login_field")
    username_box.send_keys(config.user)
    password_box = browser.find_element_by_id("password")
    password_box.send_keys(config.password)
    password_box.submit()
    time.sleep(1)
    twofactor = browser.find_element_by_name("otp")
    twofactor.send_keys(totp.now())
    twofactor.submit()


if __name__ == "__main__":
    try:
        login_sele()
    except:
        print("An error occurred")
        webdriver.Chrome.quit()
