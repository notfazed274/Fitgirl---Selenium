from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FG_homepage:

    base_url = "https://fitgirl-repacks.site/"
    boton_search = (By.CLASS_NAME, "search-toggle")
    input_search =(By.CLASS_NAME, "search-field")

    def __init__(self, browser):
        self.browser = browser

    def abrir_pag(self):
        self.browser.get(self.base_url)

    def buscar_juego(self, juego):
        abrir_input = self.browser.find_element(*self.boton_search)
        abrir_input.click()

        input_busqueda = self.browser.find_element(*self.input_search)
        input_busqueda.send_keys(juego)
        input_busqueda.send_keys(Keys.RETURN)