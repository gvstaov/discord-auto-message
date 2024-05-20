import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import webbrowser

# Função para enviar mensagem
def enviar_mensagem(user, mensagem):
    # Abra a busca do Discord (Ctrl + K)
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(1)  # Esperar a janela de busca abrir
    
    # Digite o usuário e pressione Enter
    pyautogui.write(user)
    time.sleep(1)  # Esperar a busca processar
    pyautogui.press('enter')
    time.sleep(2)  # Esperar entrar na conversa

    # Digite a mensagem e pressione Enter
    pyautogui.write(mensagem)
    pyautogui.press('enter')
    time.sleep(1)  # Esperar a mensagem ser enviada

# Função para executar o script
def executar_script():
    usuarios = entry_usuarios.get().split(",")
    mensagem = entry_mensagem.get()
    
    if not usuarios or not mensagem:
        messagebox.showwarning("Input Error", "Por favor, insira os usuários e a mensagem.")
        return
    
    # Abrir o Discord no navegador
    webbrowser.open("https://discord.com/app")
    time.sleep(10)  # Esperar o navegador carregar o Discord e fazer login manualmente

    for user in usuarios:
        enviar_mensagem(user.strip(), mensagem)
        time.sleep(2)  # Esperar um pouco entre enviar mensagens

    messagebox.showinfo("Sucesso", "Mensagens enviadas com sucesso!")

# Configuração da janela principal
root = tk.Tk()
root.title("Enviar Mensagens no Discord")
root.geometry("400x300")

# Label e Entry para usuários
label_usuarios = tk.Label(root, text="Usuários (separados por vírgula):")
label_usuarios.pack(pady=10)
entry_usuarios = tk.Entry(root, width=50)
entry_usuarios.pack(pady=5)

# Label e Entry para mensagem
label_mensagem = tk.Label(root, text="Mensagem:")
label_mensagem.pack(pady=10)
entry_mensagem = tk.Entry(root, width=50)
entry_mensagem.pack(pady=5)

# Botão para executar o script
button_executar = tk.Button(root, text="Enviar Mensagens", command=executar_script)
button_executar.pack(pady=20)

# Iniciar o loop principal da interface gráfica
root.mainloop()
