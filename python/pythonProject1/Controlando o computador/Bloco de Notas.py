import pyautogui as posicaoAbreArquivos

#import pygetWindow as fecharBlocoDeNotas

#Mesma coisa que pressionar as teclas do teclado
#windows + R
posicaoAbreArquivos.hotkey('win', 'r')

#Aguarda um tempo para o computador processar as informacoes
posicaoAbreArquivos.sleep(4)

#Digitando na caixa de pesquisa para abrir o bloco de notas
posicaoAbreArquivos.typewrite('Notepad')

#Aguarda um tempo para o computador processar as informacoes
posicaoAbreArquivos.sleep(4)

#Apertar a tecla enter para abrir o bloco de notas
posicaoAbreArquivos.press('enter')

posicaoAbreArquivos.sleep(5)

#Estamos escrevendo dentro do bloco de notas
posicaoAbreArquivos.typewrite('Minha primeira automação com Python, He He He')

#Aguarda um tempo para o computador processar as informações
posicaoAbreArquivos.sleep(4)

#Permite pegar a janela que esta ativa
fecharBlocoDeNotas = posicaoAbreArquivos.getActiveWindow()

posicaoAbreArquivos.sleep(4)

#Aciona a opçao para fechjar a janela ativa
fecharBlocoDeNotas.close()

posicaoAbreArquivos.sleep(4)

#Estou pressionado para o botao nao salvar
posicaoAbreArquivos.press('tab')

posicaoAbreArquivos.sleep(4)

#Apertamos a tecla enter para fechar sem salvar
posicaoAbreArquivos.press('enter')

print('Automacao executada com sucesso!')