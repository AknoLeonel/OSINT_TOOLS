import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import requests

# Funções para Nmap e Whois
def executar_nmap():
    alvo = entrada_nmap.get()
    if not alvo:
        messagebox.showerror("Erro", "Por favor, insira um endereço IP ou domínio.")
        return

    try:
        resultado = subprocess.check_output(f"nmap -sV {alvo}", shell=True, text=True)
        texto_resultado.delete("1.0", tk.END)
        texto_resultado.insert(tk.END, resultado)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar o Nmap: {e}")

def executar_whois():
    alvo = entrada_whois.get()
    if not alvo:
        messagebox.showerror("Erro", "Por favor, insira um domínio.")
        return

    try:
        resultado = subprocess.check_output(f"whois {alvo}", shell=True, text=True)
        texto_resultado.delete("1.0", tk.END)
        texto_resultado.insert(tk.END, resultado)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar o Whois: {e}")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("OSINT Tools GUI")
janela.geometry("800x600")
janela.resizable(False, False)

# Estilo Moderno
style = ttk.Style(janela)
style.theme_use("clam")  # Temas: clam, alt, default, classic

# Abas para Ferramentas
abas = ttk.Notebook(janela)
aba_nmap = ttk.Frame(abas)
aba_whois = ttk.Frame(abas)
abas.add(aba_nmap, text="Nmap")
abas.add(aba_whois, text="Whois")
abas.pack(expand=True, fill="both")

# Aba Nmap
tk.Label(aba_nmap, text="Digite o endereço IP ou domínio para escanear:", font=("Arial", 12)).pack(pady=10)
entrada_nmap = tk.Entry(aba_nmap, font=("Arial", 12), width=50)
entrada_nmap.pack(pady=5)

btn_nmap = ttk.Button(aba_nmap, text="Executar Nmap", command=executar_nmap)
btn_nmap.pack(pady=10)

# Aba Whois
tk.Label(aba_whois, text="Digite o domínio para consulta Whois:", font=("Arial", 12)).pack(pady=10)
entrada_whois = tk.Entry(aba_whois, font=("Arial", 12), width=50)
entrada_whois.pack(pady=5)

btn_whois = ttk.Button(aba_whois, text="Executar Whois", command=executar_whois)
btn_whois.pack(pady=10)

# Área de Resultado
texto_resultado = tk.Text(janela, font=("Courier New", 10), height=20, width=80, wrap="word")
texto_resultado.pack(pady=10)

# Rodapé
tk.Label(janela, text="Desenvolvido para estudo de OSINT", font=("Arial", 10), fg="gray").pack(pady=5)

# Loop Principal
janela.mainloop()
