import tkinter as tk
import requests

def call_api(endpoint, param):
    url = f"http://127.0.0.1:8000/{endpoint}?{param}"
    response = requests.get(url)
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, response.json())

app = tk.Tk()
app.title("Security Tools GUI")

tk.Label(app, text="Escolha a ferramenta:").pack()
tool_var = tk.StringVar(value="whois")
tk.Radiobutton(app, text="WHOIS", variable=tool_var, value="whois").pack()
tk.Radiobutton(app, text="Nmap", variable=tool_var, value="nmap").pack()

tk.Label(app, text="Parâmetro:").pack()
param_entry = tk.Entry(app)
param_entry.pack()

tk.Button(app, text="Executar", command=lambda: call_api(tool_var.get(), param_entry.get())).pack()

result_box = tk.Text(app, height=10, width=50)
result_box.pack()

app.mainloop()
