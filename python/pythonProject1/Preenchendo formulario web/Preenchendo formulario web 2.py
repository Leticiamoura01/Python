from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

from selenium.webdriver.support.select import Select

navegador = opcoesSelenium.Chrome()

navegador.get("https://form.jotform.com/221436066464051")


#Tempo para o computador abrir o formulário
tempoEspera.sleep(5)

#Prenche o campo Nome
navegador.find_element(By.NAME, "q3_nome[first]").send_keys("Ana Paula")

#Tempo para o computador abrir o formulário
tempoEspera.sleep(1)

#Prenche o campo Sobrenome
navegador.find_element(By.NAME, "q3_nome[last]").send_keys("Souza")

#Tempo para o computador abrir o formulário
tempoEspera.sleep(1)

#Prenche o campo Email
navegador.find_element(By.NAME, "q4_email").send_keys("ana.paula@hotmail.com")

#Tempo para o computador abrir o formulário
tempoEspera.sleep(3)

pegaDropDown = navegador.find_element(By.ID, "input_5")
itemSelecionado = Select(pegaDropDown)
itemSelecionado.select_by_index(2)

#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

filho = "Não"

#if = se
if filho == "Sim":

    #Marca a opção tem filho / SIM
    navegador.find_element(By.ID, "label_input_6_0").click()

else:

    # Marca a opção tem filho / NÃO
    navegador.find_element(By.ID, "label_input_6_1").click()


#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

#Marca a opção cor AZUL
navegador.find_element(By.ID, "label_input_7_0").click()

#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

#Marca a opção cor VERDE
navegador.find_element(By.ID, "label_input_7_5").click()

#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

#Marquei 5 estrelas
navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[5]').click()

#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

#Marca como muito satisfeito a Qualidade do Serviço
navegador.find_element(By.ID, "input_9_0_3").click()

#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

#Marca como satisfeito o Grau de Dificuldade
navegador.find_element(By.ID, "input_9_1_2").click()

#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

#Enviar informações
navegador.find_element(By.ID, "input_2").click()
