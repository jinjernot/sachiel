from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import webbrowser

print("Bienvenido a Jinjernot")
user = input("Ingresa el usuario a estalkear  ")

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(2)

#Log in

username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys("a")
password_input.send_keys("a")

login_link = browser.find_element("xpath", "//div[text()='Log In']")
login_link.click()

time.sleep(3)

#----
passlogin_link = browser.find_element("xpath", "//button[text()='Not Now']")
passlogin_link.click()

time.sleep(3)

passlogin_link = browser.find_element("xpath", "//button[text()='Not Now']")
passlogin_link.click()

time.sleep(3)

search_user = browser.find_element("xpath", "//input[@placeholder='Search']")
search_user.send_keys(user)
time.sleep(3)
search_user.send_keys(Keys.ENTER)
search_user.send_keys(Keys.ENTER)

time.sleep(3)

folder_name = user
os.mkdir(folder_name)

images = browser.find_elements(By.TAG_NAME,'img')

i=0
for x in images:
    ext = ".jpg"
    src = x.get_attribute("src")
    time.sleep(1)
    path = (f'{folder_name}/{folder_name}{i}{ext}')
    chida = urllib.request.urlretrieve(src, path)
    print(chida)
    i=i+1
browser.close()

f = open('jinjernot.html', 'w')

html_template =f"""
<html>
    <head>
    <head>
    <title>Jinjernot Gallery</title>
    </head>
    <body>
    <h1>Jinjernot
    <iframe src="https://ghbtns.com/github-btn.html?user=norindes&repo=jinjernot&type=star&count=true" frameborder="0" scrolling="0" width="170px" height="20px"></iframe></h1>
    <img src={path}>
</body>
</html>
"""
f.write(html_template)
  
f.close()
webbrowser.open_new_tab('jinjernot.html')