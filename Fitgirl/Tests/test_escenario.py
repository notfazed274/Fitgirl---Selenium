
from Fitgirl.Tests.Pages.FG_homepage import FG_homepage

class Test_assertions():


    def test_busqueda(self, browser):

        fg_hp = FG_homepage(browser)
        juego = "fallout 4"

        fg_hp.abrir_pag()
        fg_hp.buscar_juego(juego)

        """
        fg_rp = FG_resultspage(browser)
        # Assert comprueba que el juego buscado esté en el "search for: ...", el primer resultado y también en el título de página.
        assert juego in fg_rp.nombre_primer_resultado() and (browser.title).lower() and fg_rp.titulo_search()
        print(fg_rp.titulo_search())
        print(fg_rp.nombre_primer_resultado())
        fg_rp.seleccionar_primer_resultado()

        fg_gp = FG_gamepage(browser)
        #Assert comprueba que el juego buscado está en el título del artículo y en su descripción.
        assert juego in fg_gp.titulo_publicacion() and fg_gp.descripcion_publicacion()
        print(fg_gp.descripcion_publicacion())
        print(fg_gp.titulo_publicacion())
        """
