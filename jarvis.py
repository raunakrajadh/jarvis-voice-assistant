from scripts.taskdecider import decideTask
from scripts.generalbot import generalbot
from scripts.googlebot import googlesearch
from scripts.automation import Automation

from asyncio import run
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")

automationTasks = ["open", "close", "play", "content", "google search", "youtube search"]

def jarvis(text):  

    commands = decideTask(text)

    for command in commands:

        command: str = command.lower()

        if any(command.startswith(automationTask) for automationTask in automationTasks):
            run(Automation(list(commands)))
            return "on it"
        elif command.startswith("general"):
            return generalbot(command.removeprefix("general "))
        elif command.startswith("realtime"):
            return googlesearch(command.removeprefix("realtime "))
        elif command.startswith("undecided"):
            return "I am not sure about that sir."
        else:
            return "No function found for this command"