from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

website_url = "https://simari.ulm.ac.id/login/module.php/core/loginuserpass.php?AuthState=_9b580da462f35d11c20239dd5f249caa76adddefe9%3Ahttps%3A%2F%2Fsimari.ulm.ac.id%2Flogin%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fsimari.ulm.ac.id%252Fsaml%252Fmetadata%26cookieTime%3D1718339434%26RelayState%3Dhttps%253A%252F%252Fsimari.ulm.ac.id%252Fsaml"

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(website_url)
time.sleep(5)

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys("2110817220678")  # Replace with your username
password_input.send_keys("laluli09")

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
login_button.click()

print("Login Failed")

wait = WebDriverWait(driver, 10)
input("Press Enter to close the browser...")

driver.quit()
