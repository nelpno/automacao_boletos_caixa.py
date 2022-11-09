from datetime import datetime, timedelta
import time

import pyautogui
import pyautogui as pa


def verificar_cor_pixel(x, y, r, g, b):
    achou_cor = False

    while not achou_cor:
        if pa.pixelMatchesColor(x, y, (r, g, b)):
            achou_cor = True

    return True


def tempo(segundos):
    pyautogui.countdown(segundos)


def press_junto(x, y):
    pyautogui.hotkey(x, y)


def apertar(letra):
    pyautogui.press(letra)


def escreve(texto):
    pyautogui.write(texto)


def imagem_clicar(arquivo):
    achar_arquivo = achar_img_tela(arquivo)
    pyautogui.click(achar_arquivo)


def data_ontem():
    data_atual = datetime.now() - timedelta(1)
    data_em_texto = data_atual.strftime('%d%m%Y')
    return data_em_texto


def achar_img_tela(arquivo):
    achado = pyautogui.locateOnScreen(arquivo)
    return achado


def clicar(x, y):
    pyautogui.click(x, y)


imagem_clicar('logo_caixa.png')
tempo(1)
clicar(1136, 633)  # clique usuario
escreve("master")
apertar("tab")
escreve("master")
apertar("tab")
press_junto("alt", "a")
clicar(2487, 19)  # reduzir janela
press_junto("alt", "c")
apertar("s")
apertar("enter")
press_junto("alt", "x")
apertar("n")
press_junto("alt", "c")
pyautogui.moveTo(500,500)

while achar_img_tela('menu_boleto.png') is None:
    time.sleep(0.25)

imagem_clicar('botao3pontos.png')
tempo(1)
imagem_clicar('campo_endereco_retorno.PNG')
escreve('C:\CAIXA\Cobranca\Retorno')
apertar('enter')

while achar_img_tela('sem_mais_tratados.png') is None:
    if achar_img_tela('nenhum_boleto.png'):
        imagem_clicar('boleto_cancelar.png')
        print('Não tem boletos.')
        tempo(1)
    else:
        imagem_clicar('tem_boleto.png')
        apertar('enter')
        tempo(1)
        press_junto('alt', 't')
        while achar_img_tela('botao_ok.png') is None or tempo(2):
            time.sleep(0.25)
        imagem_clicar('botao_ok.png')
        while achar_img_tela('botao_ok.png') is None or tempo(2):
            time.sleep(0.25)
        imagem_clicar('botao_ok.png')

        while achar_img_tela('botao3pontos.png') is None:
            time.sleep(0.25)

        imagem_clicar('botao3pontos.png')
        print("E agora?")
        tempo(1)

press_junto('alt', 'f')
press_junto('alt', 'r')
apertar('t')
imagem_clicar('em_aberto.png')
imagem_clicar('vencimento.png')
apertar('tab'), apertar('tab'), apertar('tab'), apertar('tab')
tempo(1)
escreve('01012022')
apertar('tab')
escreve(data_ontem())
press_junto('alt', 'v')
