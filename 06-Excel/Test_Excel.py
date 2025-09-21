import time
import unittest
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from funciones.Funciones_Excel import Funexcel
from funciones.Funciones import Funciones

# Tiempo global de espera
tg = 1


class BaseTest(unittest.TestCase):
    def setUp(self):
        """Configuración inicial del navegador"""
        self.driver = webdriver.Chrome(
            service=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
        )
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test1(self):
        """Prueba de llenado de formulario con datos de Excel"""
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)

        # Abrir la página de prueba
        f.Navegar("https://demoqa.com/text-box")

        # Ruta al Excel
        ruta = str(CURRENT_DIR / "datos.xlsx")

        # Contar filas en la hoja
        filas = fe.getRowCount(ruta, "Hoja 1")

        # Recorrer filas desde la segunda (saltando encabezado)
        for r in range(2, filas + 1):
            nombre = fe.readData(ruta, "Hoja 1", r, 1)
            email = fe.readData(ruta, "Hoja 1", r, 2)
            dir1 = fe.readData(ruta, "Hoja 1", r, 3)
            dir2 = fe.readData(ruta, "Hoja 1", r, 4)

            # Llenar formulario
            f.Texto_ID("userName", nombre, 1)
            f.Texto_ID("userEmail", email, 1)
            f.Texto_ID("currentAddress", dir1, 1)
            f.Texto_ID("permanentAddress", dir2, 1)
            f.Click_ID_Valida("submit", 1)

            time.sleep(1)

            # Botón de cerrar modal si aparece
            f.Click_XPath_Valida("//button[@type='button']", 1)
            time.sleep(1)

            # Verificar creación
            e = f.Existe("id", "name", tg)
            if e == "Existe":
                print(f" El usuario {nombre} se creó correctamente")
                fe.writeData(ruta, "Hoja 1", r, 5, "OK")
            else:
                print(f" El usuario {nombre} no se creó correctamente")
                fe.writeData(ruta, "Hoja 1", r, 5, "NO")


if __name__ == "__main__":
    unittest.main()
