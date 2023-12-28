from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pandas as pd

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

tempoEspera.sleep(8)

# Dicionario
dicionarioCEPS = {
    "CEP 1:": "60320740",
    "CEP 2:": "01153000",
    "CEP 3:": "60320740"
}

# DataFrame
listaDataFrame = []

# Digitando um cep no caixa de Cep do busc Cep
navegador.find_element(By.NAME, "endereco").send_keys("60320740")

tempoEspera.sleep(5)

# Clica no botão de pesquisar
navegador.find_element(By.NAME, "btn_pesquisar").click()

tempoEspera.sleep(8)

for contador in dicionarioCEPS.values():
    tempoEspera.sleep(5)

    # Voltando para a página inicial, para pesquisar um novo cep
    navegador.find_element(By.NAME, 'btn_nbusca').click()

    tempoEspera.sleep(5)

    # Digitando um cep no caixa de Cep do busc Cep
    navegador.find_element(By.NAME, "endereco").send_keys(contador)

    tempoEspera.sleep(5)

    # Clica no botão de pesquisar
    navegador.find_element(By.NAME, "btn_pesquisar").click()

    tempoEspera.sleep(6)

    # Estamos pegando o xpath das tabelas onde tem as informações
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

    endereco = ""
    for linhaTabela in elementoTabela.find_elements(By.TAG_NAME, 'tr'):
        for colunaTabela in linhaTabela.find_elements(By.TAG_NAME, "td"):
            endereco = endereco + ";" + colunaTabela.text

    # Adiciona itens
    listaDataFrame.append(endereco)

arquivoExcel = pd.ExcelWriter('enderecosBuscaCEP.xlsx', engine='xlsxwriter')
arquivoExcel.save()

dataFrame = pd.DataFrame(listaDataFrame, columns=[';Rua;Bairro;Cidade;Cep'])

# Preparando o arquivo usando o mecanismo do xlsxwriter
arquivoExcel = pd.ExcelWriter('enderecosBuscaCEP.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='dados', index=False)

# Salvando o arquivo com as alterações
arquivoExcel.save()
