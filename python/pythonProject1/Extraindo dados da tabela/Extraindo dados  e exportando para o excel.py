from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pandas as pd

navegador = opcoesSelenium.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")

elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

dataFrameLista = []

linha = 1
for linhaAtual in linhas:

  print(linhaAtual.text)
  dataFrameLista.append(linhaAtual.text)

  linha = linha + 1

arquivoExcel = pd.ExcelWriter('dadosSites.xlsx', engine='xlsxwriter')
arquivoExcel._save()

dataFrame = pd.DataFrame(dataFrameLista, columns=['colunaDados'])

#Prepara o arquivo do excel usando xlsxwriter como mecanismo
arquivoExcel = pd.ExcelWriter('dadosSites.xlsx', engine='xlsxwriter')

dataFrame.to_excel('arquivo excel', sheet_name='Sheet1', index=True)

#Salva as informacoes no arquivo de excel
arquivoExcel._save()


