import requests as rq
import json

def call_ollama_model(prompt: str, model: str, stream: bool=False) -> str | dict:
    url = 'http://localhost:11434/api/generate'

    params = {
        'prompt' : prompt,
        'model' : model,
        'stream' : stream
    }

    payload = json.dumps(params)

    response = rq.post(url, data=payload,
                       headers={'Content-Type' : 'application/json'})

    if response.status_code != 200:
        return 'Error'
    else:
        response: dict = response.json()['response']
        return response
###########################################################################
if __name__ == '__main__':
    print('Hello there, I am a chatbot! Tell me anything you want...!')
    print('Enter /END to end the proccess')
    model = 'gemma3:1b'

    while True:
        prompt = input('Enter your prompt: ')
        if prompt.upper().strip() == '/END':
            print('Goodbye! See you soon.')
            break

        response = call_ollama_model(prompt, model)
        print(response)
