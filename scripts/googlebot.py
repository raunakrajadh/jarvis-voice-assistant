from googleapiclient.discovery import build
from groq import Groq
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")
GoogleCSEID = env_vars.get("GoogleCSEID")
GoogleAPIKey = env_vars.get("GoogleAPIKey")

client = Groq(api_key=GroqAPIKey)

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which has real-time up-to-date information from the internet.
*** Provide Answers In a Professional Way, make sure to add full stops, commas, question marks, and use proper grammar.***
*** Just answer the question from the provided data in a professional way. ***"""

def google(query):
    # Build the service
    service = build("customsearch", "v1", developerKey=GoogleAPIKey)
    
    # Perform the search
    res = service.cse().list(q=query, cx=GoogleCSEID).execute()
    
    # Get the search results
    if 'items' in res:
        results = res['items']
        answer = f"The search results for '{query}' are:\n[start]\n"
        for item in results:
            title = item.get('title')
            snippet = item.get('snippet')
            answer += f"Title: {title}\nDescription: {snippet}\n\n"
        answer += "[end]"
        return answer
    else:
        return "There are no search results on Google."

def AnswerModifier(Answer):
    lines = Answer.split("\n")
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = "\n".join(non_empty_lines)
    return modified_answer

def googlesearch(prompt: str = "test"):  

    googleInfo = google(prompt)
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": System},
            {"role": "user", "content": "Hi"},
            {"role": "assistant", "content": "Hello, how can I help you?"}  ,
            {"role": "system", "content": googleInfo},
            {"role": "user", "content": prompt}
        ],   
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        stream=True,
        stop=None,
    )

    Answer = ""

    for chuck in completion:
        if chuck.choices[0].delta.content:
            Answer += chuck.choices[0].delta.content

    Answer = Answer.strip().replace("</s>", "")
    return AnswerModifier(Answer=Answer)

if __name__ == "__main__":
    while True:
        prompt = input("Enter your query: ")
        print(googlesearch(prompt))