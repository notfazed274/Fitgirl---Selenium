from selenium import webdriver
import pytest
from Fitgirl.Pages.FG_homepage import FG_homepage
from Fitgirl.Pages.FG_resultspage import FG_resultspage
from Fitgirl.Pages.FG_gamepage import FG_gamepage

class Test_assertions():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=r'C:/Users/Federico/Documents/APIbooks/Webdrivers/chromedriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield
        driver.close()
        driver.quit()
        print("""

        Test completado

        """)

    def test_busqueda(self, test_setup):

        fg_hp = FG_homepage(driver)
        juego = "fallout 4"

        driver.get(fg_hp.base_url)
        fg_hp.buscar_juego(juego)

        fg_rp = FG_resultspage(driver)
        # Assert comprueba que el juego buscado esté en el "search for: ...", el primer resultado y también en el título de página.
        assert juego in fg_rp.nombre_primer_resultado() and (driver.title).lower() and fg_rp.titulo_search()
        print(fg_rp.titulo_search())
        print(fg_rp.nombre_primer_resultado())
        fg_rp.seleccionar_primer_resultado()

        fg_gp = FG_gamepage(driver)
        #Assert comprueba que el juego buscado está en el título del artículo y en su descripción.
        assert juego in fg_gp.titulo_publicacion() and fg_gp.descripcion_publicacion()
        print(fg_gp.descripcion_publicacion())
        print(fg_gp.titulo_publicacion())

