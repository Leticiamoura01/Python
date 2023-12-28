import pyautogui as posicaoMouse

import pyautogui as tempoEspera

#Tempo de espera para que o computador possa pensar/processar informações
tempoEspera.sleep(5)

#Movendo o mouse ate o botao iniciar
posicaoMouse.moveTo(36, 1056)

#Tempo de espera para que o computador possa pensar/processar informações
tempoEspera.sleep(5)
#Clicando na posicao
posicaoMouse.click(36, 1056)

#Tempo de espera para que o computador possa pensar/processar informações
tempoEspera.sleep(5)

#Permite escrever no campo
posicaoMouse.typewrite('calculadora')

#Tempo de espera para que o computador possa pensar/processar informações
tempoEspera.sleep(8)

#Movendo o mouse ate o aplicativo da calculadora
posicaoMouse.moveTo(x=220, y=320)

tempoEspera.sleep(3)

#Clico na calculadora
posicaoMouse.click(x=220, y=320)

tempoEspera.sleep(5)

#print(posicaoMouse.position())