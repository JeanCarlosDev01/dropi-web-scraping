import tkinter as tk
from tkinter.messagebox import showerror,showerror
from modules.scraping_bot import run_bot
from PIL import Image, ImageTk

COLOR_NAVY = '#201E43'
COLOR_BLUE = '#134B70'
COLOR_TEAL = '#508C9B'
COLOR_GRAY = '#EEEEEE'

root_window = tk.Tk()
root_window.geometry('480x480')
root_window.resizable(False, False)
root_window.configure(
    bg=COLOR_NAVY,
    padx=20,
    pady=20
)
root_window.title('Dropi Scraping')

form_container = tk.Frame(master=root_window)
form_container.configure(
    bg=COLOR_BLUE,
    padx=10,
    pady=10
)
form_container.pack_propagate(False)
form_container.pack(fill='both', expand=True)

dropi_image = Image.open('img/dropi.png').resize((150, 50))
tk_image = ImageTk.PhotoImage(dropi_image)

logo_image = tk.Label(master=form_container, image=tk_image, background='#134b70')
logo_image.pack()

form_title = tk.Label(master=form_container)
form_title.configure(
    foreground=COLOR_GRAY,
    background=COLOR_BLUE,
    justify='center',
    font=('Roboto', 15, 'bold'),
    text='Scraping',
    pady=10
)
form_title.pack()

def create_entry(container, label_text = 'input'):
    label = tk.Label(container)
    label.configure(
        text= label_text,
        foreground=COLOR_GRAY,
        background=COLOR_BLUE,
        font=('Roboto', 12),
        justify='center',
        pady=5
    )
    label.pack()
    str_variable = tk.StringVar()
    entry = tk.Entry(container, textvariable=str_variable)
    entry.configure(
        background=COLOR_GRAY,
        width=50
    )
    entry.pack(pady=5)
    return str_variable

dropi_email = create_entry(form_container, 'Correo elecronico Dropi')
dropi_password = create_entry(form_container, 'Contraseña de Dropi')
product_id = create_entry(form_container, 'ID del producto para buscar en Dropi')

def start():
    if (dropi_email.get() == ''):
        showerror('No hay email de Dropi', 'Es necesrio el email de tu cuenta en dropi para acceder a la información')
        return
    if (dropi_password.get() == ''):
        showerror('No hay contraseña de Dropi', 'Es necesrio la contraseña de tu cuenta en dropi para acceder a la información')
        return
    if (product_id.get() == ''):
        showerror('No hay ID de Producto', 'Es necesrio el ID del producto para buscar en Dropi y acceder a la información')
        return
    run_bot(dropi_email.get(), dropi_password.get(), product_id.get())

btn_run_bot = tk.Button(master=form_container, command=start, text='Buscar')
btn_run_bot.configure(
    bg=COLOR_TEAL,
    fg=COLOR_GRAY,
    bd=0,
    padx=20,
    pady=2,
    font=('Roboto', 11),
    cursor='hand2'
)
btn_run_bot.pack(pady=10)

root_window.mainloop()