from tkinter import messagebox
import os

def save_to_database(pr_id='', pr_name='', pr_categories=[], pr_prv_price='', pr_sug_price='', pr_desc = '', imgs_url = []):
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    str_categories = ''
    for category in pr_categories:
        cate = f'{category} '
        str_categories += cate
        
    str_img_links = ''
    
    for url in imgs_url:
        link = f'{url},\n'
        str_img_links += link
    
    text = f"{pr_id}\nNOMBRE: {pr_name}\nCATEGORIAS: {str_categories}\nPRECIO DE PROVEEDOR: {pr_prv_price}\nPRECIO SUGERIDO: {pr_sug_price}\nURL DE IMAGENES: {str_img_links}\nDESCRIPCION: {pr_desc}"
    
    file_data = f'{desktop}/{pr_id.replace('ID:', 'producto-')}.txt'
    with open(file_data, 'x') as file:
        file.write(text)
        messagebox.showinfo('Archivo de dato generado', f'La informacion del producto se guardo en {file_data}')