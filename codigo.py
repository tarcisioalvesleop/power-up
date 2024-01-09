# Passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# bibliotecas
# instalando !pip install pyautogui
import pyautogui # RPA - automação 
import time

# a cada segundo ele vai ter um delay de 1 seg
pyautogui.PAUSE = 1
# Aperta a tecla windows (comand + barra de espaço)
pyautogui.press("win")
# digita o nome do programa
pyautogui.write("chrome")
# aperta enter
pyautogui.press("enter")
#digitar o link
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
#apertar enter
pyautogui.press("enter")

# aguardando a página abrir esperando 5 seg nesse momento
time.sleep(5)

# Passo 2 - Fazer login
# clicar no campo de email Point(x=398, y=373)
pyautogui.click(x=398, y=373)
#digitar o email
pyautogui.write("teste.gmail.com")
#passa para o campo da senha
pyautogui.press("tab")
# escreve a senha
pyautogui.write("123456")
#passa para logar
pyautogui.press("tab")
#pressiona enter
pyautogui.press("enter")

time.sleep(5)

# Passo 3 - Importar a base de dados
# pip install pandas numpy openpyxl
import pandas

# le e carrega a base de dados
tabela = pandas.read_csv("produtos.csv")

# Passo 4 - Cadastrar um produto

# escrever o codigo do produto
#laço de repetição
for linha in tabela.index:   
    #clicar onde começa a preencher os dados
    pyautogui.click(x=397, y=256)

    #preencher os campos
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #tratando a observação sem valor
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): #se obs não for vazio entrar
        pyautogui.write(str(obs))

    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)

# Passo 5 - Repetir isso até acabar a base