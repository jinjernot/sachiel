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

#Start the webbrowser
driver = webdriver.Firefox()

#funcion para logearse a instagram
def login():
    
    driver.implicitly_wait(5)
    driver.get('https://www.instagram.com/')

    sleep(3)

    #Busca los campos para meter user y contraseña
    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys("jinjernot")
    password_input.send_keys("sabarobe")

    login_link = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
    login_link.click()

    time.sleep(3)

    #acepta pop ups
    passlogin_link = driver.find_element("xpath", "//button[text()='Not Now']")
    passlogin_link.click()

    time.sleep(3)

    passlogin_link = driver.find_element("xpath", "//button[text()='Not Now']")
    passlogin_link.click()

    time.sleep(3)

#funcion Stalkergram
def stalker():

    #Llama a la funcion para logear
    login()

    #Busca al usuario que se metio en el GUI
    search_user = driver.find_element("xpath", "//input[@placeholder='Search']")
    search_user.send_keys(user.get())
    time.sleep(3)
    search_user.send_keys(Keys.ENTER)
    search_user.send_keys(Keys.ENTER)

    time.sleep(3)

    #Crea un folder para ese user
    folder_name = user.get()
    folder = "im"
    os.mkdir(folder_name)
    os.mkdir(folder)

    #variable para guardar las imagenes
    images = driver.find_elements(By.TAG_NAME,'img')

    #loop para sacar las imagenes y guardarlas en el folder
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
    driver.close()

    #Abre la galeria
    webbrowser.open_new_tab('jinjernot.html')

#funcion like
def like():

    login()

    likes = driver.find_element("xpath", "//input[@placeholder='Search']")
    likes.send_keys(user.get())
    time.sleep(3)
    likes.send_keys(Keys.ENTER)
    likes.send_keys(Keys.ENTER)

    time.sleep(8)

    likes = driver.find_element("xpath", "//a[@href='/p/']")
    likes.click()




#funcion para mandar inbox
def inbox():

    #Llama a la funcion para logear

    login()

    time.sleep(3)
    mensaje = driver.find_element("xpath", "//a[@href='/direct/inbox/']/./..")
    mensaje.click()

    time.sleep(2)
    mensaje = driver.find_element("xpath", "//button[text()='Send Message']")
    mensaje.click()

    time.sleep(2)
    mensaje = driver.find_element("xpath", "//input[@placeholder='Search...']")
    mensaje.send_keys(user.get())

    time.sleep(3)
    mensaje = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/span/img")
    mensaje.click()
    
    time.sleep(3)
    mensaje = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div")
    mensaje.click()

    time.sleep(3)
    mensaje = driver.find_element("xpath", "//textarea[@placeholder='Message...']")
    mensaje.send_keys("oli desde el bot")
    time.sleep(3)
    mensaje.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.close()


    
#Crea el GUI
ws = Tk()
ws.title('Jinjernot')
ws.geometry('1920x1080')
user = tk.StringVar()


# Carga imagen de fondo png
bg = PhotoImage(file = 'img/intro.png')

#crea Ventana HD
canvas = Canvas(
	ws, 
	width = 1920,
	height = 1080
	)

#Asigna la img a todo el fondo
canvas.pack(fill='both', expand = True)

canvas.create_image(
	0, 
	0, 
	image=bg,
	anchor = "nw"
	)

#Titulo
canvas.create_text(
	1000, 
	110, 
	text = 'Jinjernot v1',
	font=("Terminal", 36, "bold"),
    fill=("white")
	)

#Agarra el usuario y lo asigna a variable
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

#boton stalker
btnS = Button(
	ws, 
	text = 'Stalk',
	command=stalker,
	width=8,
	height=2,
	relief=SOLID,
	font=("Terminal", 36, "bold")
	)
btns_canvas = canvas.create_window(
	800, 
	300,
	anchor = "nw",
	window = btnS,
	)

#Boton Inbox
btnI = Button(
	ws, 
	text = 'Inbox',
	command=inbox,
	width=8,
	height=2,
	relief=SOLID,
	font=("Terminal", 36, "bold")
	)

btnI_canvas = canvas.create_window(
	400, 
	300,
	anchor = "nw",
	window = 
    btnI,
	)

btnL = Button(
	ws, 
	text = 'Likes',
	command=like,
	width=8,
	height=2,
	relief=SOLID,
	font=("Terminal", 36, "bold")
	)
btnL_canvas = canvas.create_window(
	1200, 
	300,
	anchor = "nw",
	window = btnL,
	)
ws.mainloop()

