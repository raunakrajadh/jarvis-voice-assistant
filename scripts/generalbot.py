from groq import Groq
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey)

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in English if the question is in English, Reply in Hindi if the question is in Hindi. But reply in english if its any other language than hindi. ***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
*** Respond = "Sir [information]" or [information] sir. include sir but dont use a (,) and say a complete sentence.***
"""
# *** Reply in only English, even if the question is in Hindi, reply in English.***

def TimeInformation():
    current_data_time = datetime.datetime.now()
    day = current_data_time.strftime("%A")
    date = current_data_time.strftime("%d")
    month = current_data_time.strftime("%B")
    year = current_data_time.strftime("%Y")
    hour = current_data_time.strftime("%H")
    minute = current_data_time.strftime("%M")
    second = current_data_time.strftime("%S")

    data = f"Please use this real-time information if needed but general response as 'the time is hr:min am/pm'\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}"
    data += f"\nTime: {hour} hours :{minute} minutes :{second} seconds.\n"
    return data

def AnswerModifier(Answer):
    lines = Answer.split("\n")
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = "\n".join(non_empty_lines)
    return modified_answer

def generalbot(Query):

    try:

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages= [
                {"role": "system", "content": System},
                {"role": "user", "content": TimeInformation()},
                {"role": "user", "content": Query}],
            max_tokens=1024,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None,
        )

        Answer = ""

        for chuck in completion:
            if chuck.choices[0].delta.content:
                Answer += chuck.choices[0].delta.content

        Answer = Answer.replace("</s>", "")
        return AnswerModifier(Answer=Answer)
    
    except Exception as e:

        print(f"Error: {e}")
        return generalbot(Query)
    
if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Questions: ")
        print(generalbot(user_input))