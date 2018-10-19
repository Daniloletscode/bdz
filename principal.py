###
# Meu código

import tkinter as tk

pedidos = [0]*12
mesa_selecionada = 0


def click_mesa_01():
    janela_de_pedido(1)


def click_mesa_02():
    janela_de_pedido(2)


def click_mesa_03():
    janela_de_pedido(3)


def click_mesa_04():
    janela_de_pedido(4)


def click_mesa_05():
    janela_de_pedido(5)


def click_mesa_06():
    janela_de_pedido(6)


def click_mesa_07():
    janela_de_pedido(7)


def click_mesa_08():
    janela_de_pedido(8)


def click_mesa_09():
    janela_de_pedido(9)


def click_mesa_10():
    janela_de_pedido(10)


def click_mesa_11():
    janela_de_pedido(11)


def click_mesa_12():
    janela_de_pedido(12)


def click_salvar():
    global n_mesa
    pedidos[n_mesa-1] += 10

def janela_de_pedido():
	global mesa_selecionada
	janela_pedido = tk.Toplevel()
	tk.Label(janela_pedido, text= "Mesa {}")







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
