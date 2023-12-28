from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

#serve para controlar as teclas do computador e tempo/pausa
import pyautogui as tempoEspera

#Serve para trabalharmos com excel
import pandas as pd

navegador = opcoesSelenium.Chrome()

# Abrindo o site do rpa
navegador.get("https://rpachallengeocr.azurewebsites.net/")

listaDataFrame = []

linha = 1
i = 1

# Enquanto
while i < 4:
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

    for linhaAtual in linhas:
        print(linhaAtual.text)
        listaDataFrame.append(linhaAtual.text)
        linha = linha + 1


    i += 1

    # Para dar tempo do computador processar as informações
    tempoEspera.sleep(5)

    # Procura o xpath do botão "proximo" e clica
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    tempoEspera.sleep(5)

else:
    print("Pronto! Dados extraídos com sucesso!")

arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')
arquivoExcel._save()

dataFrame = pd.DataFrame(listaDataFrame, columns=['#;Id;Due Date'])

arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

arquivoExcel._save()



