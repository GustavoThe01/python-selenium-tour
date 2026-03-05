# 🤖 Portfolio Automation Tour (Python + Selenium)

Este projeto é uma automação interativa desenvolvida em **Python** que realiza um tour guiado pelos meus perfis profissionais (LinkedIn e GitHub). O objetivo é demonstrar competências em **RPA** (Robotic Process Automation), manipulação de **DOM** e integração com o sistema operativo.

## 🚀 Funcionalidades

* **Menu Interativo:** O tour só começa após a autorização do utilizador via terminal.
* **Disfarce Humano:** Digitação letra a letra e scroll de página com intervalos aleatórios para evitar deteção de bots.
* **Navegação Inteligente:** Pesquisa no Google, seleciona o terceiro link e navega por perfis sociais.
* **Integração Desktop:** Interage com o Bloco de Notas (Notepad) do Windows para deixar uma mensagem personalizada antes de seguir para o GitHub.
* **Navegação em Abas:** Gestão de múltiplas janelas e abas do navegador em tempo real.

## 🛠️ Tecnologias e Bibliotecas

* **[Python 3.14](https://www.python.org/):** Linguagem base.
* **[Selenium WebDriver](https://www.selenium.dev/):** Automação de navegação Web.
* **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Automação de interface de desktop.
* **[Pyperclip](https://github.com/asweigart/pyperclip):** Gestão segura da área de transferência (copy/paste) para evitar erros de caracteres especiais.

## 📋 Pré-requisitos

Antes de correr o script, precisas de instalar as dependências:

```bash
pip install selenium pyautogui pyperclip
