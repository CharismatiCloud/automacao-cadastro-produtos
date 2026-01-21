import pyautogui
import pandas as pd
import time

link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
tabela = pd.read_csv("produtos.csv")
print(tabela)
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=449, y=371)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha@dificil")
pyautogui.press("tab")
pyautogui.press("enter")

for linha in tabela.index:
    pyautogui.click(x=547, y=252)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)