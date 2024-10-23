from selenium import webdriver
from selenium.webdriver.common.by import By
import time

usuario = "tu_usuario"
pasword = "tu_contraseña"
correo = "ojalanoexistaestecorreo@gmail.com"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.netflix.com/login")
time.sleep(1)  

#por ID
username_box = driver.find_element(By.ID, ':r0:')
username_box.send_keys(usuario)
'''
password_box = driver.find_element(By.ID, ':r3:')
password_box.send_keys(pasword)

--------------------------------------------------------------

username_box_name = driver.find_element(By.NAME, 'userLoginId')
username_box_name.send_keys(usuario)
'''
#por NAME
password_box_name = driver.find_element(By.NAME, 'password')
password_box_name.send_keys(pasword)

#no lo pude hacer con CLASS NAME porque al ingresar el class del button no funciona, use el metodo del copy xpath
login_button = driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div[2]/div/form/button[1]')
login_button.click()

login_button = driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div[2]/div/form/a')
login_button.click()

#se pudo buscar el correo por CLASS_NAME
username_box_name = driver.find_element(By.CLASS_NAME, 'ui-text-input')
username_box_name.send_keys(correo)

login_button = driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div[3]/div[1]/div/button')
login_button.click()


time.sleep(10)

driver.quit()
