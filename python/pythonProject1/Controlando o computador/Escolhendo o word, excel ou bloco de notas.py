import pyautogui as escolhaOpcao

opcao = escolhaOpcao.confirm('Clicque no botao desejado',
    buttons=['Excel', 'Word', 'Notepad'])

if opcao == 'excel':

#Estamos apertando as teclas Windows + R
    escolhaOpcao.hotkey('win', 'r')

#Aguarda 4 segundos para o computador processar as informacoes
    escolhaOpcao.sleep(4)

#Digitando a palavra excel
    escolhaOpcao.typewrite('excel')

    escolhaOpcao.sleep(4)

    escolhaOpcao.press('Enter')

    escolhaOpcao.sleep(4)

#Clicando na opcao "pasta de trabalho em branco"
    escolhaOpcao.click(x=322, y=256)

    escolhaOpcao.sleep(5)

    #print(escolhaOpcao.position())

#Digitando no excel
    escolhaOpcao.typewrite('Escolhi abrir o excel')

    print('Voce escolheu abrir o excel')

elif opcao == 'Word':

  escolhaOpcao.hotkey('win', 'r')

  escolhaOpcao.sleep(5)

  escolhaOpcao.typewrite('Winword')

  escolhaOpcao.sleep(5)

  escolhaOpcao.press('Enter')

  escolhaOpcao.sleep(5)

  escolhaOpcao.press('Enter')

  escolhaOpcao.sleep(5)

  # print(escolhaOpcao.position())

  escolhaOpcao.typewrite('escolhi abri o word')

  print('Voce escolheu abri o word')

else:

    escolhaOpcao.hotkey('win', 'r')

    escolhaOpcao.sleep(5)

#Digitando a palavra notepad
    escolhaOpcao.typewrite('Notepad')

    escolhaOpcao.sleep(5)

    escolhaOpcao.press('Enter')

    escolhaOpcao.sleep(5)

    escolhaOpcao.press('Enter')

    escolhaOpcao.sleep(5)

    #print(escolhaOpcao.position())

    escolhaOpcao.typewrite('Escolhi abrir o notepad')

    print('Voce escolheu abrir o notepad')

