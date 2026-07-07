import tkinter as tk
from tkinter import ttk, messagebox


def converter():
    # realiza o cálculo de conversões entre os tipos de medidas
    try:
        valor = float(entrada_valor.get())
        tipo = escolha_tipo.get()
        unidade = escolha_unidade.get()

        resultado.delete("1.0", tk.END) # apaga o conteúdo antes de mostrar uma nova conversão

        if tipo == "Comprimento":
            # estamos utilizando o metro como base
            if unidade == "Metros":
                c = valor 
            elif unidade == "Polegadas":
                c = valor * 0.0254
            elif unidade == "Jardas":
                c = valor * 0.9144
            elif unidade == "Pés":
                c = valor * 0.3048
            elif unidade == "Milhas":
                c = valor * 1609.34

            conversoes = {
                "Metros": c,
                "Polegadas": c / 0.0254,
                "Jardas": c / 0.9144,
                "Pés": c / 0.3048,
                "Milhas": c / 1609.34
            }

            for nome, valor_convertido in conversoes.items():
                resultado.insert (tk.END, f"{nome}: {valor_convertido:.4f}\n")
            # percorre todas as conversões e escreve cada uma na caixa de resultados

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
            # estamos utilizando quilograma como base
            if unidade == "Quilograma":
                c = valor
            elif unidade == "Libra":
                c = valor * 0.4536
            elif unidade == "Onça":
                c = valor * 0.02835
            elif unidade == "Pedra":
                c = valor * 6.35
            
            conversoes = {
                "Quilograma": c,
                "Libra": c / 0.4536,
                "Onça": c / 0.02835,
                "Pedra": c / 6.35
            }

            for nome, valor_convertido in conversoes.items():
                resultado.insert(tk.END, f"{nome}: {valor_convertido:.4f}\n")

        
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
        messagebox.showerror("Erro", "Digite um número válido.")


def atualizar_unidades(event=None):
    # Atualiza as unidades disponíveis quando o usuário altera o tipo de medida
    tipo = escolha_tipo.get()

    unidades = {
        "Comprimento": ["Metros", "Polegadas", "Jardas", "Pés", "Milhas"],
        "Temperatura": ["Celsius", "Fahrenheit", "Kelvin"],
        "Massa": ["Quilograma", "Libra", "Onça", "Pedra"],
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
    state = "readonly"
)
# Com o state = "readonly" o usuário só pode escolher uma das opções da lista, não pode digitar.
escolha_tipo.pack(pady=5)
escolha_tipo.current(0)
escolha_tipo.bind("<<ComboboxSelected>>", atualizar_unidades)
# Quando o usuário mudar a opção na caixinha, chama a função atualizar_unidades()
                  
tk.Label(janela, text="Escolha a unidade original:").pack(pady=5)
escolha_unidade = ttk.Combobox(janela, state="readonly")
escolha_unidade.pack(pady=5)

botao = tk.Button(janela, text="Converter", command=converter)
botao.pack(pady=10)

resultado = tk.Text(janela, height=8, width=35)
resultado.pack(pady=10)

atualizar_unidades()

janela.mainloop()