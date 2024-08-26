import customtkinter
import tkinter as tk

# Funções para a lógica da calculadora
def adicionar_texto(texto):
    atual = EResultado.get()
    EResultado.delete(0, tk.END)
    EResultado.insert(0, atual + texto)

def calcular():
    try:
        expressao = EResultado.get()
        # Substituir 'X' por '*' e '%' por '/100' para avaliação correta
        expressao = expressao.replace('X', '*').replace('%', '/100')
        resultado = eval(expressao)
        EResultado.delete(0, tk.END)
        EResultado.insert(0, str(resultado))
    except Exception as e:
        EResultado.delete(0, tk.END)
        EResultado.insert(0, 'Erro')

def limpar_tudo():
    EResultado.delete(0, tk.END)

def apagar_ultimo():
    atual = EResultado.get()
    EResultado.delete(0, tk.END)
    EResultado.insert(0, atual[:-1])

# Criar as Cores a Usar
Co0 = '#A9A9A9'

# Configurar a Janela Principal
janela = customtkinter.CTk()
janela.geometry('250x250+100+100')
janela.resizable(0, 0)
janela.config(bg=Co0)
janela.title('Calculadora Basica')

# Criar uma Entry para exibir o resultado
EResultado = customtkinter.CTkEntry(janela, width=220, bg_color=Co0, justify='right')
EResultado.place(x=10, y=10)

# Criar os Botões e Operadores
BModulo = customtkinter.CTkButton(janela, text='%', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('%'))
BModulo.place(x=10, y=45)

BClear = customtkinter.CTkButton(janela, text='C', width=50, bg_color=Co0, fg_color=Co0, command=limpar_tudo)
BClear.place(x=65, y=45)

BCE = customtkinter.CTkButton(janela, text='CE', width=50, bg_color=Co0, fg_color=Co0, command=limpar_tudo)
BCE.place(x=120, y=45)

BBack = customtkinter.CTkButton(janela, text='←', width=50, bg_color=Co0, fg_color=Co0, command=apagar_ultimo)
BBack.place(x=175, y=45)

BNove = customtkinter.CTkButton(janela, text='9', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('9'))
BNove.place(x=10, y=80)

BOito = customtkinter.CTkButton(janela, text='8', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('8'))
BOito.place(x=65, y=80)

BSete = customtkinter.CTkButton(janela, text='7', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('7'))
BSete.place(x=120, y=80)

BDiv = customtkinter.CTkButton(janela, text='/', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('/'))
BDiv.place(x=175, y=80)

BQuatro = customtkinter.CTkButton(janela, text='4', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('4'))
BQuatro.place(x=10, y=115)

BCinco = customtkinter.CTkButton(janela, text='5', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('5'))
BCinco.place(x=65, y=115)

BSeis = customtkinter.CTkButton(janela, text='6', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('6'))
BSeis.place(x=120, y=115)

BMultiplicacao = customtkinter.CTkButton(janela, text='X', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('X'))
BMultiplicacao.place(x=175, y=115)

BUM = customtkinter.CTkButton(janela, text='1', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('1'))
BUM.place(x=10, y=150)

BDois = customtkinter.CTkButton(janela, text='2', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('2'))
BDois.place(x=65, y=150)

BTres = customtkinter.CTkButton(janela, text='3', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('3'))
BTres.place(x=120, y=150)

BSub = customtkinter.CTkButton(janela, text='-', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('-'))
BSub.place(x=175, y=150)

BZero = customtkinter.CTkButton(janela, text='0', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('0'))
BZero.place(x=10, y=185)

BVirgula = customtkinter.CTkButton(janela, text=',', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('.'))
BVirgula.place(x=65, y=185)

BIgual = customtkinter.CTkButton(janela, text='=', width=50, bg_color=Co0, fg_color=Co0, command=calcular)
BIgual.place(x=120, y=185)

BSoma = customtkinter.CTkButton(janela, text='+', width=50, bg_color=Co0, fg_color=Co0, command=lambda: adicionar_texto('+'))
BSoma.place(x=175, y=185)

# Criar o label do autor
font = ('Arial', 14, 'bold')
Autor = customtkinter.CTkLabel(janela, text='Autor : Dev Joel 2024 © Portugal', font=font, bg_color=Co0, fg_color=Co0)
Autor.place(x=10, y=220)

# Iniciar o loop da janela
janela.mainloop()
