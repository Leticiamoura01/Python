from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as tempoEspera
import pyautogui as funcoesTeclado

import pandas as pd

navegador = opcoesSelenium.Chrome()

#Preparando o site
navegador.get("https://www.magazineluiza.com.br/")

#Procura pelo campo Id e digita o nome do produto
navegador.find_element(By.ID, 'input-search').send_keys("Geladeira")

tempoEspera.sleep(5)

funcoesTeclado.press('enter')

tempoEspera.sleep(10)

#Criando data frame que vai receber os dados
listaDataFrame = []

listaProdutos = navegador.find_elements(By.CLASS_NAME, "eJDyHN")

for item in listaProdutos:

    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

    if nomeProduto ==  "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "sc-eWzREE").text
        except Exception:
            pass
    elif nomeProduto ==  "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "uaEbk").text
        except Exception:
            pass

    print(nomeProduto)
    #---------------------------------------------------------------

    if precoProduto ==  "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "kXWuGr").text
        except Exception:
            pass

    elif precoProduto ==  "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-hoLEA").text
        except Exception:
            pass

    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "eCPtRw").text
        except Exception:
            pass

    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-kpDqfm").text
        except Exception:
            pass

    else:

        precoProduto = "0"
    #-------------------------------------------------

    if urlProduto ==  "":

        try:
            urlProduto = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            pass

    else:

        urlProduto = "-"

    print(nomeProduto, "-", precoProduto)
    print(urlProduto)

    dadosLinha = nomeProduto + ";" + precoProduto + ";" + urlProduto

    #Populando data frame com as linhas/informacoes
    listaDataFrame.append(dadosLinha)

    arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
    arquivoExcel._save()

    dataFrame = pd.DataFrame(listaDataFrame, columns=['Descrição;Preco;Url'])

    arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')

    dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

    arquivoExcel._save()

