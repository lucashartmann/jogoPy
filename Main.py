from view.App import Jogo
from config import Terminal

if __name__ == "__main__":
    try:
        Jogo(ansi_color=True).run()
    except Exception as e:
        print(e)
        Terminal.remove_background_image()
