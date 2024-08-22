from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tkinter.messagebox import showerror
import re
import time
from modules.save_product_data import save_to_file

# Definir una funcion que me permita esperar unos segundos antes de seguir ejecutando codigo
def time_sleep(seconds = 10):
    time.sleep(seconds)

def run_bot(email, password, product_id):
    # Define la expresión regular para verificar una dirección de correo electrónico
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Funcion para verificar que el correo electronico sea valido
    def email_is_valid(mail):
        if re.match(email_regex, mail):
            return True
        return False

    # Si el email es invalido, mostrara un mensaje al usuario y detendra la ejecucion
    if not email_is_valid(email):
        showerror('El email no es valido', 'Por favor verifica el correo electronico')
        return
    
    # Funcion para verificar que el id del producto sea valido
    def id_is_valid(pr_id):
        try:
            int(pr_id)
            return True
        except:
            showerror('Id del producto invalido', 'El ID del producto debe ser numerico')
            return False
        
    if not id_is_valid(product_id):
        return
    
    # Definir la ruta del chrome driver y crear el web driver
    service = Service('./webdriver/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # ------------ INICIO DE SESSION --------

    # Abrir el enlace de login de dropi
    driver.get('https://app.dropi.co/auth/login')
    
    time_sleep(5)

    # seleccionar los inputs del login de Dropi
    input_email = driver.find_element(By.ID, 'email')
    input_password = driver.find_element(By.ID, 'password')

    # Insertar los valores en los inputs del login
    input_email.send_keys(email)
    input_password.send_keys(password)

    # Seleccionar el boton para iniciar session
    btn_login = driver.find_element(By.XPATH, '//button[@type="button"]')
    btn_login.click() # Hacer click en el boton

    # Esperar 10s antes para que cargue la pagina
    time_sleep(5)
    
    def credentials_is_vallid():
        try:
            msg_error = driver.find_element(By.ID, 'swal2-title')
            if msg_error.text == 'Oops...':
                showerror('No se pudo iniciar session', 'Las credenciales de acceso a Dropi son incorrectas')
                driver.quit()
                return False
        except:
            return True

    if not credentials_is_vallid():
        return
    
    # Buscar el producto por su id en Dropi
    driver.get(f'https://app.dropi.co/dashboard/search?search={product_id}')

    # Esperar 5s para que cargue la pagina y evitar errores
    time_sleep(5)

    # Seleccionar la carta del producto correspondiente 
    card_product = driver.find_element(By.TAG_NAME, 'app-card-product')
    card_product.click() # Hacer click sobre la carta para ver la informacion

    time_sleep(5)

    # --------- extraer informacion del producto -----------
    # La informacion del producto se carga en una nueva pestaña del navegador
    #seleccionar la nueva pestaña
    tabs = driver.window_handles
    driver.switch_to.window(tabs[-1])

    # Seleccionar el elemento html y estraer los datos correpondientes
    product_id = driver.find_element(By.XPATH, '//div[@class="id_product"]').text # Extraer ID del producto
    product_name = driver.find_element(By.TAG_NAME, 'h2').text # Extraer nombre del producto
    product_categories = driver.find_elements(By.XPATH, '//div[@class="chip ng-star-inserted"]') # Extraer elementos html que contienen la categoria(s) del producto
    category_names = list() # lista que almacenara cada categoria

    # Iterar la lista de elementos html de las categorias
    for category in product_categories:
        # Guardar el nombre de cada categoria y guararla en la lista
        category_names.append(category.text)

    try:
        # Seleccionar el contenedor del precio de producto del proveedor
        container_provider_price = driver.find_element(By.CLASS_NAME, 'price-providers')
        # Extraer el texto del precio
        product_provider_price = container_provider_price.find_element(By.TAG_NAME, 'currency').text
        
        # Seleccionar el contenedor del precio sugerido del producto
        container_suggested_price = driver.find_element(By.CLASS_NAME, 'price-providers')
        # Extraer el texto del precio
        product_suggested_price = container_suggested_price.find_element(By.TAG_NAME, 'currency').text
    except:
        list_container_price = driver.find_elements(By.CLASS_NAME, 'ng-star-inserted')
        container_provider_price = list_container_price[0]
        # Extraer el texto del precio
        list_prices = container_provider_price.find_elements(By.TAG_NAME, 'currency')
        product_provider_price = list_prices[0].text
        product_suggested_price = list_prices[1].text

    time_sleep(5) #  Esperar a que carguen las imagenes

    # Seleccionar el contenedor de la imagenes
    container_product_images = driver.find_element(By.ID, 'pn_id_5')
    # Seleccionar todos los elementos que contienen imagenes del producto
    list_elements_image = container_product_images.find_elements(By.TAG_NAME, 'img')
    list_url_images = list() # lsita para almacenar las urls

    # Iterar la lista de elementos para extraer las urls
    for image in list_elements_image:
        # Extrar urls de cada elemento imagen y alamacenarlo en una lista
        list_url_images.append(image.get_attribute('src'))

    # Eliminar la primera imagen que carga por defecto en la pagina que por lo general es repetida
    list_url_images.pop(0)

    # Seleccionar elemento que contiene la descripcion del producto y extraer el texto
    product_description = driver.find_element(By.ID, 'descriptionContainer').text
    driver.quit() # cerrar el webdriver
    
    # Guardar la informacion en un archivo
    save_to_file(product_id, product_name, category_names, product_provider_price, product_suggested_price, product_description, list_url_images)