import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
t=.8


@pytest.mark.run
def test_uno():
    print("Test uno")

@pytest.mark.run
def test_dos():
    print("Test dos")

@pytest.mark.run
def test_tres():
    print("Test tres")

@pytest.mark.notrun
def test_cuatro():
    print("Test cuatro")

@pytest.mark.run
def test_cinco():
    print("Test cinco")

@pytest.mark.run
def test_seis():
    print("Test seis")

@pytest.mark.skip
def test_siete():
    print("Test siete")

#Puedo hacer : pytest .\Pytest_Mark.py -s -v -k "not cuatro" y me corre todo menos el 4
#Puedo hacer : pytest .\Pytest_Mark.py -s -v -k "run" y me corre todos los que tienen la marca run
#Puedo hacer : pytest .\Pytest_Mark.py -s -v -k "not run" y me corre todos los que no tienen la marca run
#Puedo hacer : pytest .\Pytest_Mark.py -s -v -k "not run and not siete" y me corre todos los que no tienen la marca run y no es el 7
