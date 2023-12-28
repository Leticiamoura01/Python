from selenium import webdriver as opcoesselenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
from selenium.webdriver.support.select import Select

navegador = opcoesselenium.Chrome()

navegador.get("https://pt.surveymonkey.com/r/7GX9XRZ")

tempoEspera.sleep(8)

#Preenche o nome
navegador.find_element(By.NAME, "72542598").send_keys("Amalia Cardoso")

tempoEspera.sleep(5)

#Preenche o email
navegador.find_element(By.NAME, "72542821").send_keys("amalia@gmail.com")

tempoEspera.sleep(5)

sexo = "Feminino"

#Se = if
if sexo == "Masculino":


    navegador.find_element(By.ID, "72542994_583517054_label").click()

else:

    navegador.find_element(By.ID, "72542994_583517055_label").click()

tempoEspera.sleep(5)

pegaDropdown = navegador.find_element(By.ID, "72543178")
itemSelecionado = Select(pegaDropdown)
itemSelecionado.select_by_index(2)

#Clicar no botao para enviar as informacoes
navegador.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()




