import tkinter as tk
from tkinter import ttk, messagebox


def converter():
    try:
        valor = float(entrada_valor.get())
        tipo = escolha_tipo.get()
        unidade = escolha_unidade.get()

        resultado.delete("1.0", tk.END) # apaga o conteúdo antes de mostrar uma nova conversão

        if tipo == "Comprimento":
            # estamos utilizando o metro como base
            fatores = {
                "Metro": 1,
                "Quilômetro": 1000,
                "Centímetro": 0.01,
                "Milímetro": 0.001
            }

            valor_metros = valor * fatores[unidade]

            for nome, fator in fatores.items():
                resultado.insert (tk.END, f"{nome}: {valor_metros / fator:.4f}\n")


        elif tipo == "Temperatura":
            if unidade == "Celsius":
                c = valor
            elif unidade == "Fahrenheit":
                c = (valor-32) * 5/9
            elif unidade == "Kelvin":
                c = valor - 273.15
            
            conversoes = {
                "Celsius": c,
                "Fahrenheit": (c * 9/5) + 32,
                "Kelvin": c + 273.15
            }

            for nome, valor_convertido in conversoes.items():
                resultado.insert(tk.END, f"{nome}: {valor_convertido:.2f}\n")


        elif tipo == "Massa":
            # estamos utilizando grama como base
            fatores = {
                "Grama": 1,
                "Quilograma": 1000,
                "Miligrama": 0.001,
                "Tonelada": 1000000
            }

            valor_gramas = valor * fatores[unidade]

            for nome, fator in fatores.items():
                resultado.insert (tk.END, f"{nome}: {valor_gramas / fator:.4f}\n")

        
        elif tipo == "Tempo":
            # estamos utilizando o segundo como base
            fatores = {
                "Segundo": 1,
                "Minuto": 60,
                "Hora": 3600,
                "Dia": 86400
            }

            valor_segundos = valor * fatores[unidade]

            for nome, fator in fatores.items():
                resultado.insert (tk.END, f"{nome}: {valor_segundos / fator:.4f}\n")
    
    
    except ValueError:
        messagebox.showerror("Erro", "DIgite um número válido.")


def atualizar_unidades(event=None):
    tipo = escolha_tipo.get()

    unidades = {
        "Comprimento": ["Metro", "Quilômetro", "Centímetro", "Milímetro"],
        "Temperatura": ["Celsius", "Fahrenheit", "Kelvin"],
        "Massa": ["Grama", "Quilograma", "Miligrama", "Tonelada"],
        "Tempo": ["Segundo", "Minuto", "Hora", "Dia"]
    }

    escolha_unidade["values"] = unidades[tipo]
    escolha_unidade.current(0)

# Inteface

janela = tk.Tk()
janela.title("Conversor de Medidas")
janela.geometry("400x400")

tk.Label(janela, text="Digite o valor:").pack(pady=5)
entrada_valor = tk.Entry(janela)
entrada_valor .pack(pady=5)

tk.Label(janela, text="Escolha o tipo de medida: ").pack(pady=5)
escolha_tipo = ttk.Combobox(
    janela,
    values = ["Comprimento", "Temperatura", "Massa", "Tempo"],
    state = "readyonly"
)
escolha_tipo.pack(pady=5)
escolha_tipo.current(0)
escolha_tipo.bind("<<ComboboxSelected>>", atualizar_unidades)
                  
tk.Label(janela, text="Escolha a unidade original:").pack(pady=5)
escolha_unidade = ttk.Combobox(janela, state="readyonly")
escolha_unidade.pack(pady=5)

botao = tk.Button(janela, text="Converter", command=converter)
botao.pack(pady=10)

resultado = tk.Text(janela, height=8, width=35)
resultado.pack(pady=10)

atualizar_unidades()

janela.mainloop()