from tkinter import messagebox
import os

# Funcion para guardar la informacion en un archivo
def save_to_file(pr_id='', pr_name='', pr_categories=[], pr_prv_price='', pr_sug_price='', pr_desc = '', imgs_url = []):
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop') # Obtener la ruta del escritorio
    
    # Variable para almacenar las categorias
    str_categories = ''
    # Iterar la lista de categorias y agregarlas a la variable
    for category in pr_categories:
        cate = f'{category} '
        str_categories += cate
    
    # Variable para almacenar los links de las imagenes    
    str_img_links = ''
    # Iterar la lista de urls y agregarlas a la variable
    for url in imgs_url:
        link = f'{url},\n'
        str_img_links += link
    
    # Completar el formato de texto que se guardara en el archivo
    text = f"{pr_id}\nNOMBRE: {pr_name}\nCATEGORIAS: {str_categories}\nPRECIO DE PROVEEDOR: {pr_prv_price}\nPRECIO SUGERIDO: {pr_sug_price}\nURL DE IMAGENES: {str_img_links}\nDESCRIPCION: {pr_desc}"
    
    # Crear la ruta del archivo para guardar la informacion
    file_data = f'{desktop}/{pr_id.replace('ID:', 'producto-')}.txt'
    # Abrir el archivo y escribir la informacion
    with open(file_data, 'x') as file:
        file.write(text)
        # Mostrar mensaje cuando el archivo este creado
        messagebox.showinfo('Archivo de dato generado', f'La informacion del producto se guardo en {file_data}')