import pyautogui as posicaoMouse

import pyautogui as tempoEspera

tempoEspera.sleep(4)

posicaoMouse.moveTo(36, 1056)

tempoEspera.sleep(4)

posicaoMouse.click(36, 1056)

tempoEspera.sleep(5)

#Digita na barra de tarefas
posicaoMouse.typewrite('Edger')

tempoEspera.sleep(5)

#Precionando a tecla enter para abrir o google chrome
posicaoMouse.press('enter')

tempoEspera.sleep(6)

#Digitando a palavra "dolar" para pesquisar
posicaoMouse.typewrite('Dolar hoje')

tempoEspera.sleep(5)

#Preciona enter no edger
posicaoMouse.press("enter")