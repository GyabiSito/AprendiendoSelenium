import time
import unittest
import sys
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

CURRENT_DIR = Path(__file__).resolve().parent
FUNCIONES_DIR = CURRENT_DIR / "Funciones"
if str(FUNCIONES_DIR) not in sys.path:
    sys.path.insert(0, str(FUNCIONES_DIR))

from Funciones_Globales.Funciones import Funciones

service = Service(r"C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
t = .3


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(t)
        driver = self.driver

    def test1(self):
        driver = self.driver
        driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/08-Mouse%20Actions/01-Sublists.html")

        # Encontrar los elementos por ID
        admin = driver.find_element(By.ID, "menu_admin_viewAdminModule")
        user_mgmt = driver.find_element(By.ID, "menu_admin_viewUserManagment")
        system_users = driver.find_element(By.ID, "menu_admin_viewSystemUsers")

        # Hacer hover y click encadenado
        actions = ActionChains(driver)

        # Hover encadenado
        actions.move_to_element(admin).perform()
        WebDriverWait(driver, 5).until(EC.visibility_of(user_mgmt))

        actions.move_to_element(user_mgmt).perform()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "menu_admin_viewSystemUsers")))

        system_users = driver.find_element(By.ID, "menu_admin_viewSystemUsers")
        actions.move_to_element(system_users).click().perform()

    def test2(self):
        driver = self.driver
        driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/08-Mouse%20Actions/02-DobleClick.html")

        box = driver.find_element(By.ID, "box")
        actions = ActionChains(driver)
        actions.double_click(box).perform()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "box"), "¡Doble click detectado!")
        )

        self.assertIn("Doble click", box.text)
        time.sleep(2)

    def test3(self):
        driver = self.driver
        driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/08-Mouse%20Actions/03-ClickDerecho.html")

        target = driver.find_element(By.ID, "target")
        actions = ActionChains(driver)

        # Click derecho (context menu)
        actions.context_click(target).perform()

        # Esperar al cambio de texto
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "target"), "¡Click derecho detectado!")
        )

        self.assertIn("Click derecho", target.text)
        time.sleep(2)  # Visual pause

    def test4(self):
        driver = self.driver
        driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/08-Mouse%20Actions/04-DragAndDrop.html")

        source = driver.find_element(By.ID, "drag")
        target = driver.find_element(By.ID, "dropzone")

        actions = ActionChains(driver)
        # Método directo
        actions.drag_and_drop(source, target).perform()

        # Esperar que el texto cambie
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "dropzone"), "¡Elemento soltado!")
        )

        self.assertIn("soltado", target.text)
        time.sleep(2)  # Visual pause


    def test5(self):
        driver = self.driver
        driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/08-Mouse%20Actions/05-ClickXYTest.html")

        canvas = driver.find_element(By.ID, "canvas")
        actions = ActionChains(driver)

        actions.move_to_element_with_offset(canvas, 50, 80).click().perform()
        time.sleep(1)

        actions.move_to_element_with_offset(canvas, 60, 70).click().perform()
        time.sleep(2)

        # Validar que se agregaron los "dots" al canvas
        dots = canvas.find_elements(By.CLASS_NAME, "dot")
        self.assertGreaterEqual(len(dots), 2)


    def test6(self):
        driver = self.driver
        driver.get("file:///C:/Users/Josec/OneDrive/Escritorio/Selenium/08-Mouse%20Actions/06-CopiarPegar.html")

        source = driver.find_element(By.ID, "source")
        target = driver.find_element(By.ID, "target")

        # Seleccionar todo el texto en source y copiar
        source.send_keys(Keys.CONTROL, "a")
        source.send_keys(Keys.CONTROL, "c")

        # Pegar en el target
        target.click()
        target.send_keys(Keys.CONTROL, "v")

        time.sleep(1)  # para ver la acción

        # Validar que el contenido se pegó bien
        self.assertEqual(source.get_attribute("value"), target.get_attribute("value"))

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

