# Scraper de Clasificación Liga EA SPORTS

Este proyecto extrae la tabla de clasificación de la Liga EA SPORTS desde Flashscore.es y la guarda en un archivo Excel.

## Investigación

La página https://www.flashscore.es/futbol/espana/laliga-ea-sports/clasificacion/vcm2MhGk/clasificacion/general/ carga los datos de la tabla dinámicamente mediante JavaScript. El HTML inicial no contiene la tabla; se carga después de que el JavaScript se ejecute.

No se encontró una API pública documentada para acceder directamente a los datos JSON. Los datos se obtienen mediante requests AJAX internos del sitio, pero estos requieren autenticación o headers específicos que no están disponibles públicamente.

## Instalación y Ejecución

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Asegúrate de tener Google Chrome instalado.

3. Ejecuta el script:
   ```bash
   python3 scrape_liga.py
   ```

   O usa el script automatizado:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

Esto generará `clasificacion_liga.xlsx` con la clasificación.

## Dependencias

- selenium
- webdriver-manager
- pandas
- openpyxl

Por lo tanto, se utiliza Selenium para renderizar la página completamente antes de extraer la tabla.

## Instalación de Dependencias

Ejecuta el siguiente comando para instalar las dependencias:

```bash
pip install -r requirements.txt
```

Las dependencias incluyen:
- selenium: Para controlar un navegador web.
- webdriver-manager: Para gestionar automáticamente el ChromeDriver.
- pandas: Para procesar y guardar los datos en Excel.
- openpyxl: Para escribir archivos Excel.

## Ejecución

Ejecuta el script Python:

```bash
python scrape_liga.py
```

El script:
1. Abre la página en un navegador headless (sin interfaz gráfica).
2. Espera a que la página cargue completamente.
3. Extrae la tabla de clasificación.
4. Guarda los datos en `clasificacion_liga.xlsx`.

## Notas

- Asegúrate de tener Google Chrome instalado en tu sistema, ya que Selenium usa ChromeDriver.
- Si no tienes Chrome, puedes modificar el script para usar Firefox (geckodriver).
- El tiempo de espera (time.sleep(5)) puede ajustarse si la página tarda más en cargar.