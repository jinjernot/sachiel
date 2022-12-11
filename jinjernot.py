from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import webbrowser
from tkinter import *
import tkinter as tk

#GUI
ws = Tk()
ws.title('Jinjernot')
ws.geometry('1920x1080')
user = tk.StringVar()

#Global variables|
browser = webdriver.Firefox()


def login():
    
    browser.implicitly_wait(5)

    browser.get('https://www.instagram.com/')

    sleep(2)

    #   Log in

    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys("jinjernot")
    password_input.send_keys("sabarobe")

    login_link = browser.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
    login_link.click()

    time.sleep(3)

    #----
    passlogin_link = browser.find_element("xpath", "//button[text()='Not Now']")
    passlogin_link.click()

    time.sleep(3)

    passlogin_link = browser.find_element("xpath", "//button[text()='Not Now']")
    passlogin_link.click()

    time.sleep(3)

# Funcion Stalkergram
def stalker():

    login()

    search_user = browser.find_element("xpath", "//input[@placeholder='Search']")
    search_user.send_keys(user.get())
    time.sleep(3)
    search_user.send_keys(Keys.ENTER)
    search_user.send_keys(Keys.ENTER)

    time.sleep(3)

    folder_name = user.get()
    folder = "im"
    os.mkdir(folder_name)
    os.mkdir(folder)

    images = browser.find_elements(By.TAG_NAME,'img')

    i=0
    for x in images:
        ext = ".jpg"
        src = x.get_attribute("src")
        time.sleep(1)
        path = (f'{folder_name}/{folder_name}{i}{ext}')
        path2 = ((f'{folder}/{i}{ext}'))
        chida = urllib.request.urlretrieve(src, path)
        palreact = urllib.request.urlretrieve(src, path2)
        print(chida)
        print(palreact)
        i=i+1
    browser.close()

    webbrowser.open_new_tab('jinjernot.html')

def inbox():

    login()

    mensaje = browser.find_element("xpath", "//a[@href='/direct/inbox/']")
    mensaje.click()




# Imagen de fondo
bg = PhotoImage(file = 'img/intro.png')

canvas = Canvas(
	ws, 
	width = 1920,
	height = 1080
	)

canvas.pack(fill='both', expand = True)

canvas.create_image(
	0, 
	0, 
	image=bg,
	anchor = "nw"
	)

canvas.create_text(
	1000, 
	110, 
	text = 'Jinjernot v1',
	font=("Terminal", 36, "bold"),
    fill=("white")
	)

entry = Entry (
    ws,
    width=50,
    textvariable=user,
)

entry_canvas = canvas.create_window(
    950,
    200,
    window=entry
    )


btn = Button(
	ws, 
	text = 'Stalk',
	command=stalker,
	width=8,
	height=2,
	relief=SOLID,
	font=("Terminal", 36, "bold")
	)

btn_canvas = canvas.create_window(
	800, 
	300,
	anchor = "nw",
	window = btn,
	)

btnL = Button(
	ws, 
	text = 'Post',
	command=inbox,
	width=8,
	height=2,
	relief=SOLID,
	font=("Terminal", 36, "bold")
	)

btnL_canvas = canvas.create_window(
	400, 
	300,
	anchor = "nw",
	window = btnL,
	)

ws.mainloop()
