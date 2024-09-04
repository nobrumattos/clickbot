import pyautogui
import time
import PySimpleGUI as sg

# Configuração da duração padrão de espera
WAIT_TIME = 3

# Função para clicar e aguardar
def click_and_wait(x, y, wait_time=WAIT_TIME):
    pyautogui.click(x, y)
    time.sleep(wait_time)

# Função principal
def main():
    layout = [[sg.Text("Controle de Automação de Cliques")],
              [sg.Button("Iniciar"), sg.Button("Parar")]]
    window = sg.Window("Bot de Cliques", layout)

    automation_running = False
    try:
        while True:
            event, values = window.read(timeout=100)

            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Iniciar":
                automation_running = True
            elif event == "Parar":
                automation_running = False

            if automation_running:
                # Clique na sessão 1
                click_and_wait(1164, 546)

                # Clique na sub-sessão 1
                click_and_wait(1081, 594, wait_time=15)

                # Clique em "Assistir"
                click_and_wait(625, 703, wait_time=15)

                # Pressione a seta para baixo 18 vezes
                for _ in range(18):
                    pyautogui.press('down')

                # Clique no sinal de play
                click_and_wait(698, 315, wait_time=58)

                # Clique para reiniciar o loop
                click_and_wait(701, 629, wait_time=10)
    except KeyboardInterrupt:
        print("Automação interrompida pelo usuário.")
    finally:
        window.close()

if __name__ == "__main__":
    main()
