from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)

chrome_browser = webdriver.Chrome(options=options)
chrome_browser.maximize_window()
chrome_browser.get("https://qaplayground.com/practice/forms")

# assert "Form Automation Practice" in chrome_browser.title
login_button = chrome_browser.find_element(
    By.CLASS_NAME, "forms-module__ZLwUJq__submitBtn"
)
print(login_button.get_attribute("innerHTML"))

assert "Login" in chrome_browser.page_source

email_message = chrome_browser.find_element(By.ID, "login-email")
email_message.clear()
email_message.send_keys("abc@gmail.com")

password_input = chrome_browser.find_element(By.ID, "login-password")
password_input.clear()
password_input.send_keys("12345678")

login_button.click()

output_message = chrome_browser.find_element(By.ID, "loginResult")
assert "abc@gmail.com" in output_message.text

time.sleep(5)
chrome_browser.quit()
