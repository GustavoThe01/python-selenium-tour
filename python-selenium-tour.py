import random
import time
import sys
import os
import pyautogui  # Biblioteca para controlar o teclado do Windows
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class RoboPortfolio:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def digitar_como_humano(self, elemento, texto):
        for letra in texto:
            elemento.send_keys(letra)
            time.sleep(random.uniform(0.05, 0.12))

    def rolar_pagina_devagar(self):
        altura_atual = 0
        altura_total = self.driver.execute_script("return document.body.scrollHeight")
        while altura_atual < altura_total:
            deslocamento = random.randint(150, 250)
            self.driver.execute_script(f"window.scrollBy(0, {deslocamento});")
            altura_atual += deslocamento
            time.sleep(random.uniform(0.4, 0.8))
            altura_total = self.driver.execute_script("return document.body.scrollHeight")

    def escrever_no_bloco_de_notas(self):
        print("\nAbrindo Bloco de Notas...")
        # Abre o Bloco de Notas (Windows + R -> notepad)
        pyautogui.hotkey('win', 'r')
        time.sleep(1)
        pyautogui.write('notepad')
        pyautogui.press('enter')
        time.sleep(2)  # Espera o programa abrir

        # Escreve a mensagem de forma humana
        mensagem = "Vamos conhecer um pouco mais de Gustavo."
        pyautogui.write(mensagem, interval=0.1)

        print("Mensagem escrita. Aguardando 3 segundos...")
        time.sleep(3)

        # Fecha sem salvar (Alt + F4 e depois 'n' para Não salvar)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(1)
        pyautogui.press('n')
        print("Bloco de Notas fechado.")

    def executar(self):
        # --- PASSO 1: GOOGLE ---
        self.driver.get("https://www.google.com")
        campo_google = self.driver.find_element(By.NAME, "q")
        self.digitar_como_humano(campo_google, "Gustavo Osterno Linkedin")
        campo_google.send_keys(Keys.RETURN)
        time.sleep(3)

        # --- PASSO 2: LINKEDIN ---
        resultados = self.driver.find_elements(By.TAG_NAME, "h3")
        resultados[2].click() if len(resultados) >= 3 else resultados[0].click()
        time.sleep(5)

        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "Ver perfil").click()
            time.sleep(4)
        except:
            pass

        try:
            self.driver.find_element(By.XPATH, "//button[@aria-label='Fechar']").click()
        except:
            pass

        self.rolar_pagina_devagar()
        time.sleep(2)

        # --- PASSO NOVO: BLOCO DE NOTAS ---
        self.escrever_no_bloco_de_notas()

        # --- PASSO 3: GITHUB ---
        print("\nVoltando para o tour: Abrindo GitHub...")
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://github.com/GustavoThe01")
        time.sleep(3)

        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "Repositories").click()
            time.sleep(3)
            self.rolar_pagina_devagar()
            self.driver.back()
            time.sleep(5)
        except:
            pass

    def finalizar(self):
        self.driver.quit()
        print("\n" + "=" * 30)
        feedback = input("Como foi a Tour? ")
        print(f"\nObrigado pelo feedback: '{feedback}'")
        print("=" * 30)


def menu_inicial():
    print("-" * 50)
    print("Podemos Iniciar um tuor para conhecer o Gustavo?")
    print("1 - Sim\n2 - Não")
    print("-" * 50)
    if input("Opção: ") == "1":
        bot = RoboPortfolio()
        bot.executar()
        bot.finalizar()
    else:
        print("\nAté logo!")
        sys.exit()


if __name__ == "__main__":
    menu_inicial()