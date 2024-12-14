import random
import string
import tkinter as tk
from tkinter import ttk

def gerar_senha_tkinter():
    # Gera a senha baseada em alguns critérios como: Números, caracteres especiais e letras maiusculas.
    try:
        comprimento = int(comprimento_var.get())
        incluir_maiusculas = maiusculas_var.get()
        incluir_numeros = numeros_var.get()
        incluir_especiais = especiais_var.get()

        # Conjunto básico: letras minúsculas
        caracteres = string.ascii_lowercase
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_especiais:
            caracteres += string.punctuation

        # Verificar se há caracteres disponíveis
        if not caracteres:
            senha_gerada.set("Selecione ao menos uma opção de caracteres!")
            return

        # Gerar senha
        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        senha_gerada.set(senha)
    except ValueError:
        senha_gerada.set("Erro: Comprimento inválido!")

# Janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x300")

# Variáveis
comprimento_var = tk.StringVar(value="8")
maiusculas_var = tk.BooleanVar(value=True)
numeros_var = tk.BooleanVar(value=True)
especiais_var = tk.BooleanVar(value=True)
senha_gerada = tk.StringVar()

# Layout
ttk.Label(janela, text="Comprimento da senha:").pack(pady=5)
ttk.Entry(janela, textvariable=comprimento_var).pack(pady=5)

ttk.Checkbutton(janela, text="Incluir Letras Maiúsculas", variable=maiusculas_var).pack(anchor="w", padx=20)
ttk.Checkbutton(janela, text="Incluir Números", variable=numeros_var).pack(anchor="w", padx=20)
ttk.Checkbutton(janela, text="Incluir Caracteres Especiais", variable=especiais_var).pack(anchor="w", padx=20)

ttk.Button(janela, text="Gerar Senha", command=gerar_senha_tkinter).pack(pady=10)

ttk.Label(janela, text="Senha Gerada:").pack(pady=5)
ttk.Entry(janela, textvariable=senha_gerada, state="readonly", width=50).pack(pady=5)

# Executar a janela
janela.mainloop()
