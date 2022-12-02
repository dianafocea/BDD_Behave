from imports import *

class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(10)


    def close(self):
        self.driver.quit()


# Tema 11 - BDD, POM
#
# Exerciții Recomandate - grad de dificultate: Ușor
#
# 1. Revizualizează întâlnirea 10 și ia notițe în caz că ți-a scăpat ceva.
#
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
#
# Avand ca exemplu pagina:
# https://the-internet.herokuapp.com/login
#
# Impementati 3 pagini intr-un nou proiect BDD cu POM
#
# a. Home page https://the-internet.herokuapp.com/
# - Sa aiba cel putin 3 elemente inlcusiv Form Authentication
# - Sa contina metode de click pe ele
#
# b. Login page https://the-internet.herokuapp.com/login
# - Sa contina user, pass, login_btn si metode pt interactiune cu ele
#
# c. Secure page https://the-internet.herokuapp.com/secure
# - Sa contina mesajul de succes si verificare ca e displayed
# - Sa contina logout_btn si click pe el