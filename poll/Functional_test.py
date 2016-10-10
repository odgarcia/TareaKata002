__author__ = "oscar"
from unittest import TestCase
from selenium import webdriver

class FuntionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Pedro')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Perez')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('3')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3013648287')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('od.garcia@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\Users\oscar\Downloads\yo.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('pedro456')

        clave = self.browser.find_element_by_id('id_clave')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(3)
        span=self.browser.find_element_by_xpath( '//span[text()="Pedro Perez"]')

        self.assertIn('Pedro Perez', span.text)

