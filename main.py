# Telegram: @SaMi_ye
# Instagram: cyber_77k

from sami_ai import Worm_GPT
import time
import platform
import os

try:
    import pyfiglet
except ImportError:
    os.system('pip install pyfiglet')
    os.system("pip install --upgrade pyfiglet")

# Coded By Mr.SaMI
red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"


def banner():
    sami = pyfiglet.Figlet(font="slant")
    banner_text = sami.renderText("WormGPT")
    print(green + banner_text)


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main(key, model):
    banner()

    while True:
        user_input = input(red + "YOU $_ " + green)

        if user_input.lower() == 'exit':
            print("Exiting WormGPT. Goodbye!")
            break
        elif user_input.lower() == 'clear':
            clear()
        else:
            result = Worm_GPT(user_input, key, model)
            print(f"{red}WormGPT : {green}{result['response']}\n")


if __name__ == "__main__":
    banner()
    key = "YOUR_KEY_OPEN_AI"
    model = "gpt-3.5-turbo-16k-0613"
    clear()
    main(key, model)
