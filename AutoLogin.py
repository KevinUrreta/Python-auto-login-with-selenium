# Para importar cualquier tipo de libreria usamos 'pip install <libreria>'.
# Por ejemplo: 'pip install selenium', en este caso.
import selenium # Importamos una libreria para poder extraer elementos de una página 'index.html'.
from selenium import webdriver # Permite ejecutar el navegador.
from selenium.webdriver.common.by import By # Permite extraer campos.
from selenium.webdriver.common.keys import Keys # Nos permite enviar el texto deseado de los campos extraidos.
import time # Importamos un 'temporizador' para hacer que el programa espere entre funciones.

# Creamos las variables, aunque podemos introducirlas directamentes, según tus preferencias.
email = "usuario@gmail.com" # Ponemos nuestro correo electrónico.
passwd = "contraseña123" # Ponemos nuestra contraseña.
url = "https://PAGINA.DESEADA.com" # La dirección de la página donde queremos ingresar.
path = "/usr/lib/firefox-esr/firefox-esr %u" # La ruta del driver de nuestro navegador (quizá debamos actualizarlo).

driver = webdriver.Firefox() # Abre el navegador.
driver.get(url) # Abre la página que hemos declarado antes como una variable.
#driver.maximize_window() # Lo activamos si queremos mantener la ventana maximizada.

# Buscamos los elementos dentro de la página y enviamos los valores que queremos introducir.
# Para encontrar el XPATH, debemos de copiar el elemento y veremos un menú desplegable
# nos dejará escojer qué queremos copiar.
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(passwd)
driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/div[1]/form/div[3]/button').click()
time.sleep(5)
