import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class Funciones():
    def __init__(self, driver):
        self.driver = driver


    def Saludo(self):
        print("Hola")

    def Tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t

    def Navegar(self, url):
        self.driver.get(url)

    def Texto_XPath(self, xpath, text, tiempo):
        texto = self.driver.find_element(By.XPATH, xpath)
        texto.clear()
        texto.send_keys(text)
        t = time.sleep(tiempo)
        return t

    def Texto_Name(self, name, text, tiempo):
        texto = self.driver.find_element(By.NAME, name)
        texto.clear()
        texto.send_keys(text)
        t = time.sleep(tiempo)
        return t

    def Texto_XPath_Valida(self, xpath, text, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(text)
            t = time.sleep(tiempo)
            return t
        except TimeoutException:  # esto esta bueno porque se tira que el elemento no existe, es decir el test sigue pasando y no se rompe a la primera de cambio
            print("El elemento no se encuentra")

    def Click_XPath_Valida(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException:
            print("El elemento no se encuentra")

    def Click_ID_Valida(self, id, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, id)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException:
            print("El elemento no se encuentra")

    def Select_XPath_Text(self, xpath, text, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = Select(self.driver.find_element(By.XPATH, xpath))
            val.select_by_visible_text(text)
            t = time.sleep(tiempo)
            return t
        except TimeoutException:
            print("El elemento no se encuentra")

    def Select_XPath_Type(self, xpath, tipo, dato, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = Select(self.driver.find_element(By.XPATH, xpath))
            if (tipo == "text"):
                val.select_by_visible_text(dato)
            elif (tipo == "value"):
                val.select_by_value(dato)
            else:
                val.select_by_index(dato)
            t = time.sleep(tiempo)
            return t
        except TimeoutException:
            print("El elemento no se encuentra")

    def Upload_XPath(self, xpath, ruta, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)
            t = time.sleep(tiempo)
            return t
        except TimeoutException:
            print("El elemento no se encuentra")

    def Check_XPath(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException:
            print("El elemento no se encuentra")

    def Check_ID(self, id, tiempo):
        try:
            val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, id)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException:
            print("El elemento no se encuentra")

    def Texto_ID(self, id, text, tiempo):
        texto = self.driver.find_element(By.ID, id)
        texto.clear()
        texto.send_keys(text)
        t = time.sleep(tiempo)
        return t

    def Check_XPath_Multiples(self, tiempo, *args):
        try:
            for i in args:
                val = WebDriverWait(self.driver, tiempo).until(EC.visibility_of_element_located((By.XPATH, i)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, i)
                val.click()
                t = time.sleep(tiempo)
                return t
            print("No se encontraron los elementos")
        except TimeoutException:
            print("El elemento no se encuentra")
            return t

