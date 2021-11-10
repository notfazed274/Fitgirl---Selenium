from selenium.webdriver.common.by import By

class FG_resultspage:

    titulo_resultados = (By.CSS_SELECTOR, '#content > header > h1')
    primer_resultado = (By.CLASS_NAME, "entry-title")

    def __init__(self, driver):
        self.driver = driver

    def titulo_search(self):
        titulo_encabezado = self.driver.find_element(*self.titulo_resultados)
        return (titulo_encabezado.text).lower()

    def seleccionar_primer_resultado(self):

        resultado = self.driver.find_element(*self.primer_resultado)
        resultado.click()

    def nombre_primer_resultado(self):

        titulo_juego = self.driver.find_element(*self.primer_resultado)
        return (titulo_juego.text).lower()