from selenium import webdriver
from selenium.webdriver.common.by import By
import time

usuario = "tu_usuario"
pasword = "tu_contraseña"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.netflix.com/login")
time.sleep(1)  
#ruta relativa
username_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div[1]/div/div[1]/input')
username_box.send_keys(usuario)

#css selector
password_box = driver.find_element(By.CSS_SELECTOR, ('input[id=":r3:"]'))
password_box.send_keys(pasword)

#ruta acertiva
login_button = driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div[2]/div/form/button[1]')
login_button.click()

time.sleep(10)

driver.quit()
