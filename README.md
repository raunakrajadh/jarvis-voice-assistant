# Jarvis

## Features
1. general chatbot
2. realtime information from google chatbot can respond with
3. ask time
4. ask weather
5. automations such as:
- open apps
- close apps
- play directly on youtube with song name
- write contents: essay, emails, letters, etc
- google search
- youtube search

## Setup
Setup virtual environment
```bash
python -m venv venv
```

Activate environment
```bash
.\venv\Scripts\activate
```

## Installation
To install packages:
```bash
python install -r requirements.txt
```

## Config
Setup config: Go to `.env` and put values for CohereAPIKEY, GroqAPIKEY, GoogleAPIKey, GoogleCSEID

```bash
CohereAPIKey = 
GroqAPIKey = 
GoogleAPIKey = 
GoogleCSEID = 

Username = Raunak Raj Adhikari
Assistantname = Jarvis
InputLanguage = en
AssistanceVoice = en-CA-LiamNeural
```

Use the following websites:
- [Cohere API Key](https://dashboard.cohere.com/api-keys)
- [Groq API Key](https://console.groq.com/keys)
- [Google Cloud Console - GoogleAPIKey](https://cloud.google.com/) - Make sure to enable Custom Search API 
- [Google CSE Id](https://programmablesearchengine.google.com/) - Get your Custom Search Engine ID

## Usage
To start using Jarvis, run the following command:
```bash
python main.py
```
