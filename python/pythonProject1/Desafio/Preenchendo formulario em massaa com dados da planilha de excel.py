from openpyxl import load_workbook

nome_arquivo_challeng = "C:\Users\kauan\Downloads\1 rpa\python\pythonProject1.xlsx"
planilhaDadosChalleng = load_workbook(nome_arquivo_challeng)

sheet_selecionada = planilhaDadosChalleng["Dados"]


from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import  pyautogui as tempoEspera
from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallenge.com/")

tempoEspera.sleep(5)

#for = para
for linha in range(2, len(sheet_selecionada['A']) + 1):

    tempoEspera.sleep(5)

    firstName = sheet_selecionada['A%s' % linha].value

    #Localiza o campo FirstName e envia o texto
    #//*[@] - Localizaro campo
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(firstName)

    tempoEspera.sleep(5)

    lastName = sheet_selecionada['B%s' % linha].value

    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(lastName)

    tempoEspera.sleep(5)

    companyName = sheet_selecionada['C%s' % linha].value

    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(companyName)

    tempoEspera.sleep(5)

    role = sheet_selecionada['D%s' % linha].value

    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(role)

    tempoEspera.sleep(5)

    address= sheet_selecionada['E%s' % linha].value

    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(address)

    tempoEspera.sleep(5)

    email = sheet_selecionada['F%s' % linha].value

    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(email)

    tempoEspera.sleep(5)

    phone = sheet_selecionada['G%s' % linha].value

    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(phone)

    tempoEspera.sleep(5)

    navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

    print("Dados enviados com sucesso!")





