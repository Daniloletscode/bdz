
###
# Meu código

import tkinter as tk

pedidos = [0]*12
mesa_selecionada = 0
entrada_de_pedido = None


def click_mesa_01():
    janela_de_pedido()
    print("Mesa 1")
    global mesa_selecionada 
    mesa_selecionada = 1

def click_mesa_02():
    janela_de_pedido()
    print("Mesa 2")
    global mesa_selecionada 
    mesa_selecionada = 2
    


def click_mesa_03():
    janela_de_pedido()
    print("Mesa 3")
    global mesa_selecionada 
    mesa_selecionada = 3


def click_mesa_04():
    janela_de_pedido()
    print("Mesa 4")
    global mesa_selecionada 
    mesa_selecionada = 4


def click_mesa_05():
    janela_de_pedido()
    print("Mesa 5")
    global mesa_selecionada 
    mesa_selecionada = 5


def click_mesa_06():
    janela_de_pedido()
    print("Mesa 6")
    global mesa_selecionada 
    mesa_selecionada = 6


def click_mesa_07():
    janela_de_pedido()
    print("Mesa 7")
    global mesa_selecionada 
    mesa_selecionada = 7

def click_mesa_08():
    janela_de_pedido()
    print("Mesa 8")
    global mesa_selecionada 
    mesa_selecionada = 8


def click_mesa_09():
    janela_de_pedido()
    print("Mesa 9")
    global mesa_selecionada 
    mesa_selecionada = 9


def click_mesa_10():
    janela_de_pedido()
    print("Mesa 10")
    global mesa_selecionada 
    mesa_selecionada = 10


def click_mesa_11():
    janela_de_pedido()
    print("Mesa 11")
    global mesa_selecionada 
    mesa_selecionada = 11


def click_mesa_12():
    janela_de_pedido()
    print("Mesa 12")
    global mesa_selecionada 
    mesa_selecionada = 12


def click_salvar():
    global mesa_selecionada
    global entrada_de_pedido
    valor = float(entrada_de_pedido.get())
    indice = mesa_selecionada - 1
    pedidod[indice] += valor

def janela_de_pedido():
	global mesa_selecionada
	global entrada_de_pedido
	janela_pedido = tk.Toplevel()
	tk.Label(janela_pedido, text="Mesa {}".format(mesa_selecionada)).pack()
	tk.Label(janela_pedido, text="Valor do pedido:").pack()
	entrada_de_pedido = tk.Entry(janela_pedido)
	entrada_de_pedido.pack()
	tk.Button(janela_pedido, text="Salvar", height=3, command=click_salvar).pack(fill=tk.X, pady=5)
	tk.Button(janela_pedido, text="Encerrar mesa").pack(fill=tk.X)

    





root = tk.Tk()
root.geometry("185x345+30+30")

tk.Label(root, text="Bar Do Zé Atomatik").grid(row=0, column=0, columnspan=3)


tk.Button(root, command=click_mesa_01, text="1", width=6, height=4
          ).grid(row=1, column=0, padx=5, pady=5)

tk.Button(root, command=click_mesa_02, text="2", width=6, height=4
          ).grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, command=click_mesa_03, text="3", width=6, height=4
          ).grid(row=1, column=2, padx=5, pady=5)

tk.Button(root, command=click_mesa_04, text="4", width=6, height=4
          ).grid(row=2, column=0, padx=5, pady=5)

tk.Button(root, command=click_mesa_05, text="5", width=6, height=4
          ).grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, command=click_mesa_06, text="6", width=6, height=4
          ).grid(row=2, column=2, padx=5, pady=5)

tk.Button(root, command=click_mesa_07, text="7", width=6, height=4
          ).grid(row=3, column=0, padx=5, pady=5)

tk.Button(root, command=click_mesa_08, text="8", width=6, height=4
          ).grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, command=click_mesa_09, text="9", width=6, height=4
          ).grid(row=3, column=2, padx=5, pady=5)

tk.Button(root, command=click_mesa_10, text="10", width=6, height=4
          ).grid(row=4, column=0, padx=5, pady=5)

tk.Button(root, command=click_mesa_11, text="11", width=6, height=4
          ).grid(row=4, column=1, padx=5, pady=5)

tk.Button(root, command=click_mesa_12, text="12", width=6, height=4
          ).grid(row=4, column=2, padx=5, pady=5)

root.mainloop()
