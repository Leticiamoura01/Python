from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

from selenium.webdriver.support.select import Select
navegador = opcoesSelenium.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

#Tempo para o computador abrir o formulario
tempoEspera.sleep(10)

#Preenche o campo nome
navegador.find_element(By.NAME, "q3_nome[first]").send_keys("Ana Leticia")

tempoEspera.sleep(5)

#Preenche o campo sobrenome
navegador.find_element(By.NAME, 'q3_nome[last]').send_keys("Felipe")

tempoEspera.sleep(5)

#Preenche o campo email
navegador.find_element(By.NAME, 'q4_email').send_keys("leticia@gmail.com")

tempoEspera.sleep(5)

pegaDropDown = navegador.find_element(By.ID, 'input_5')
itemSelecionado = Select(pegaDropDown)
itemSelecionado.select_by_index(2)

tempoEspera.sleep(5)

filho = "Não"

#if = se
if filho == "Sim":

    #Marca a opcao tem filho/ sim
    navegador.find_element(By.ID, "label_input_6_0").click()

else:

    #Marca a opcao tem filho /não
    navegador.find_element(By.ID, "label_input_6_1").click()

tempoEspera.sleep(5)

#Marca a opção cor vermelha
navegador.find_element(By.ID, "label_input_7_2").click()

tempoEspera.sleep(5)

navegador.find_element(By.ID, "label_input_7_4").click()

tempoEspera.sleep(5)

#Marquei 3 estrelas
navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[3]').click()







