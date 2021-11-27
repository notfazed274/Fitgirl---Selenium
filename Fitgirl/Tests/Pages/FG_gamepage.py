from selenium.webdriver.common.by import By


class FG_gamepage:

    titulo_juego = (By.CLASS_NAME, "entry-title")
    descripcion_juego = (By.CLASS_NAME, "entry-content")

    def __init__(self, driver):
        self.driver = driver

    def titulo_publicacion(self):

        titulo = self.driver.find_element(*self.titulo_juego)
        return (titulo.text).lower()

    def descripcion_publicacion(self):

        descripcion = self.driver.find_element(*self.descripcion_juego)
        return (descripcion.text).lower()

