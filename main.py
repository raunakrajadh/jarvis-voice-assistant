from jarvis import jarvis
from scripts.speechtotext import speechtotext
from scripts.texttospeech import texttospeech

from gui import start_tkinter, printIt
import threading
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
        
if __name__ == "__main__":
    
    def firstThread():

        printIt(f"{Assistantname}: is online")
        texttospeech(f"{Assistantname} is online")

        while True:
            text = speechtotext()
            if "jarvis" in text.lower():
                printIt(f"{Username}: {text}")
                bot = jarvis(text)
                printIt(f"{Assistantname}: {bot}")
                texttospeech(bot)

    threading.Thread(target=firstThread, daemon=True).start()
    start_tkinter()


        