from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# auth.txt contains the username and password separated by a newline
username, password = open("auth.txt").readlines()

# Open the hover.com sign-in page in Chromium and log in
# The control panel redirects to the sign in page and forwards the user to the control panel once they login.
driver = webdriver.Firefox()
driver.get("https://www.hover.com/control_panel/domain/icanhazsite.com")

# Find the username box and type username
username_box = driver.find_element_by_name("username")
username_box.send_keys(username)
time.sleep(1)

# Find the password box and type password
password_box = driver.find_element_by_name("password")
password_box.send_keys(password)

# Hit the 'Sign In' button
time.sleep(2)
sign_in_button = driver.find_element_by_link_text("SIGN IN")
sign_in_button.send_keys(Keys.RETURN)
# Grrr this ^^ clicks the button but doesn't redirect the page, so were just
# stuck on the login page again :|
