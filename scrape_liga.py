from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# URL de la clasificación
url = "https://www.flashscore.es/futbol/espana/laliga-ea-sports/clasificacion/vcm2MhGk/clasificacion/general/"

# Configurar opciones para Brave en modo headless
options = Options()
options.binary_location = "/usr/bin/brave-browser"  # Path a Brave
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inicializar el driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Cargar la página
    driver.get(url)
    
    # Esperar a que la página cargue completamente (ajustar tiempo si es necesario)
    time.sleep(5)
    
    # Obtener el HTML renderizado
    html = driver.page_source
    
    # Usar pandas para leer las tablas del HTML
    tables = pd.read_html(html)
    
    if tables:
        # Asumir que la primera tabla es la de clasificación
        df = tables[0]
        
        # Limpiar el DataFrame si es necesario (eliminar filas vacías, etc.)
        df = df.dropna(how='all')
        
        # Guardar en Excel
        df.to_excel('clasificacion_liga.xlsx', index=False)
        print("Datos guardados en clasificacion_liga.xlsx")
        print(df.head())
    else:
        print("No se encontraron tablas en la página.")
        
finally:
    # Cerrar el driver
    driver.quit()