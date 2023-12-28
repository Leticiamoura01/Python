from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

tempoEspera.sleep(8)

#Digitando um cep no caixa de Cep do busc Cep
navegador.find_element(By.NAME, "endereco").send_keys("60320740")

tempoEspera.sleep(5)

#Clica no botão de pesquisar
navegador.find_element(By.NAME, "btn_pesquisar").click()

tempoEspera.sleep(8)

#estamos pegando o xpath das tabelas onde tem as informacoes
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

for linhaTabela in elementoTabela.find_elements(By.TAG_NAME, "tr"):
    endereco = ""
    for colunaTabela in linhaTabela.find_elements(By.TAG_NAME, "td"):

        endereco = endereco + ";" + colunaTabela.text

print(endereco)



