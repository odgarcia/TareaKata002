__author__ = "oscar"
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FuntionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:\Users\oscar\Downloads\chromedriver_win32\chromedriver.exe')


    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    # def test_registro(self):
    #     self.browser.get('http://localhost:8000')
    #     link = self.browser.find_element_by_id('id_register')
    #     link.click()
    #
    #     self.browser.implicitly_wait(3)
    #     nombre = self.browser.find_element_by_id('id_nombre')
    #     nombre.send_keys('Pedro')
    #
    #     apellidos = self.browser.find_element_by_id('id_apellidos')
    #     apellidos.send_keys('Perez')
    #
    #     experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
    #     experiencia.send_keys('3')
    #
    #     self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
    #     telefono = self.browser.find_element_by_id('id_telefono')
    #     telefono.send_keys('3013648287')
    #
    #     correo = self.browser.find_element_by_id('id_correo')
    #     correo.send_keys('od.garcia@uniandes.edu.co')
    #
    #     imagen = self.browser.find_element_by_id('id_imagen')
    #     imagen.send_keys('C:\Users\oscar\Downloads\yo.jpg')
    #
    #     nombreUsuario = self.browser.find_element_by_id('id_username')
    #     nombreUsuario.send_keys('pedro456')
    #
    #     clave = self.browser.find_element_by_id('id_password')
    #     clave.send_keys('clave123')
    #
    #     botonGrabar = self.browser.find_element_by_id('id_grabar')
    #     botonGrabar.click()
    #
    #     self.browser.implicitly_wait(3)
    #     span=self.browser.find_element_by_xpath( '//span[text()="Pedro Perez"]')
    #
    #     self.assertIn('Pedro Perez', span.text)
    #
    # def test_verDetalle(self):
    #     self.browser.get('http://localhost:8000')
    #     span = self.browser.find_element_by_xpath('//span[text()="Pedro Perez"]')
    #     span.click()
    #
    #     h2 = self.browser.find_element_by_xpath('//h2[text()="Pedro Perez"]')
    #     self.assertIn('Pedro Perez', h2.text)
    #

    # def test_ingreso(self):
    #     self.browser.get('http://localhost:8000')
    #     link = self.browser.find_element_by_id('id_login')
    #     link.click()
    #
    #     self.browser.implicitly_wait(3)
    #
    #     textUserName = self.browser.find_element_by_id("id_username")
    #     textUserName.send_keys('pedro456')
    #
    #     textPassword = self.browser.find_element_by_id("id_password")
    #     textPassword.send_keys('clave123')
    #
    #     botonIngreso = self.browser.find_element_by_id('id_ingreso')
    #     botonIngreso.click()
    #
    #     self.browser.implicitly_wait(1)
    #     mensajeFlotante = self.browser.find_element_by_class_name('float-message')
    #     textMensaje = mensajeFlotante.text
    #     self.assertTrue(textMensaje.index('SUCCESS: Bienvenido al sistema pedro456'))

    #
    # def test_editar(self):
    #     self.browser.get('http://localhost:8000')
    #     link = self.browser.find_element_by_id('id_login')
    #     link.click()
    #
    #     self.browser.implicitly_wait(3)
    #
    #     textUserName = self.browser.find_element_by_id("id_username")
    #     textUserName.send_keys('pedro456')
    #
    #     textPassword = self.browser.find_element_by_id("id_password")
    #     textPassword.send_keys('clave123')
    #
    #     botonIngreso = self.browser.find_element_by_id('id_ingreso')
    #     botonIngreso.click()
    #
    #     self.browser.implicitly_wait(2)
    #     linkEditar = self.browser.find_element_by_id('id_editar')
    #     linkEditar.click()
    #
    #     self.browser.implicitly_wait(1)
    #
    #     nombre = self.browser.find_element_by_id('id_nombre')
    #     nombre.clear()
    #     nombre.send_keys('Carlos')
    #
    #     apellidos = self.browser.find_element_by_id('id_apellidos')
    #     apellidos.clear()
    #     apellidos.send_keys('Santana')
    #
    #     experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
    #     experiencia.clear()
    #     experiencia.send_keys('5')
    #
    #     telefono = self.browser.find_element_by_id('id_telefono')
    #     telefono.clear()
    #     telefono.send_keys('3013648285')
    #
    #
    #     botonGrabar = self.browser.find_element_by_id('id_grabar')
    #     botonGrabar.click()
    #
    #     link = self.browser.find_element_by_id('id_editar')
    #     link.click()
    #
    #     #Verificando nombre
    #     nombre = self.browser.find_element_by_id('id_nombre')
    #     self.assertEqual(nombre.get_attribute("value"),'Carlos')
    #     apellidos = self.browser.find_element_by_id('id_apellidos')
    #     self.assertEqual(apellidos.get_attribute("value"), 'Santana')
    #     telefono = self.browser.find_element_by_id('id_telefono')
    #     self.assertEqual(telefono.get_attribute("value"), '3013648285')
    #     experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
    #     self.assertEqual(experiencia.get_attribute("value"), '5')

    def test_comentar(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element_by_xpath('//span[text()="OSCAR GARCIA"]')
        span.click()

        correo = self.browser.find_element_by_id('correo')
        correo.clear()
        correo.send_keys('od.garcia@uniandes.edu.co')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.clear()
        comentario.send_keys('Hola esto es una prueba')

        self.browser.implicitly_wait(20)
        #button = self.browser.find_element_by_class_name('btn-success')
        button = self.browser.find_element_by_xpath("//button[contains(@class, 'btn btn-default btn-success btn-guardar-comentario')]" )
        button.click()

        self.browser.implicitly_wait(20)

        for option in self.browser.find_element_by_id('comentarios').find_elements_by_tag_name('h4'):
            if option.text.index('od.garcia@uniandes.edu.co'):
                self.assertTrue(option.text.index('od.garcia@uniandes.edu.co'))

        for optionp in self.browser.find_element_by_id('comentarios').find_elements_by_tag_name('p'):
            if optionp.text.index('Hola esto es una prueba'):
                self.assertTrue(optionp.text.index('Hola esto es una prueba'))







