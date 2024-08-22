import tkinter as tk
from tkinter.messagebox import showerror,showerror
from modules.scraping_bot import run_bot
from PIL import Image, ImageTk

# Definir paleta de colores para la interfaz
COLOR_NAVY = '#201E43'
COLOR_BLUE = '#134B70'
COLOR_TEAL = '#508C9B'
COLOR_GRAY = '#EEEEEE'

# Creacion de la ventana principal de la app
root_window = tk.Tk()
root_window.geometry('480x480') # Definir dimenciones de la ventana principal
root_window.resizable(False, False) # Hacer que no se pueda mofificar el tamaño
root_window.configure(
    bg=COLOR_NAVY, # Color de fondo de la ventana
    padx=20, # Padding horizontal 
    pady=20  # Padding vertical
)
root_window.title('Dropi Scraping') # Titulo de la pagina

# Contenedor del formulario
form_container = tk.Frame(master=root_window)
form_container.configure(
    bg=COLOR_BLUE, 
    padx=10,
    pady=10
)
form_container.pack_propagate(False) # Evitar que se ajuste al tamaño de los elementos internos
form_container.pack(fill='both', expand=True) # Insertar en en contenedor

# Cargar logo de dropi
dropi_image = Image.open('img/dropi.png').resize((150, 50)) 
tk_image = ImageTk.PhotoImage(dropi_image)

# Insertar logo de dropi
logo_image = tk.Label(master=form_container, image=tk_image, background='#134b70')
logo_image.pack()

# Crear titulo en la interfaz
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

# Funcion para crear los inputs en el formulario
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

# Crear los inputs y alamcenarlos en variables 
dropi_email = create_entry(form_container, 'Correo elecronico Dropi')
dropi_password = create_entry(form_container, 'Contraseña de Dropi')
product_id = create_entry(form_container, 'ID del producto para buscar en Dropi')

# Funcion del boton para iniciar el web-scraping
def start():
    # Verificar que los campos del formulario esten completos
    if (dropi_email.get() == ''):
        showerror('No hay email de Dropi', 'Es necesrio el email de tu cuenta en dropi para acceder a la información')
        return
    if (dropi_password.get() == ''):
        showerror('No hay contraseña de Dropi', 'Es necesrio la contraseña de tu cuenta en dropi para acceder a la información')
        return
    if (product_id.get() == ''):
        showerror('No hay ID de Producto', 'Es necesrio el ID del producto para buscar en Dropi y acceder a la información')
        return
    # Si estan completos iniciar el proceso de web-scraping
    run_bot(dropi_email.get(), dropi_password.get(), product_id.get())

# Crear y definir la configuracion del boton
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

# Mantener la ventana activa
root_window.mainloop()