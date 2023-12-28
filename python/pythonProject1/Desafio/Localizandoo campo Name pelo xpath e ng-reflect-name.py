from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import  pyautogui as tempoEspera
from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallenge.com/")

tempoEspera.sleep(5)

#Localiza o campo FirstName e envia o texto
#//*[@] - Localizaro campo
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys("Ednardo")

tempoEspera.sleep(5)

navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys("Abreu")

tempoEspera.sleep(5)

navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys("Aprendendo Python")

tempoEspera.sleep(5)

navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys("Diretor")

tempoEspera.sleep(5)

navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys("Rua Alvares Centro, 3535")

tempoEspera.sleep(5)

navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys("ednardo@gmail.com")

tempoEspera.sleep(5)

navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys("99999-9999")

tempoEspera.sleep(5)

navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

print("Dados enviados com sucesso!")

