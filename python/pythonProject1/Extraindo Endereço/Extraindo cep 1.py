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

#Pega os dados da rua no site pelo XPATH
rua = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[1]/td[1]').text
print("Rua:", rua)

bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[1]/td[2]').text
print("Bairro:", bairro)

cidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[1]/td[3]').text
print("Cidade:", cidade)

cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[1]/td[4]').text
print("Cep:", cep)


