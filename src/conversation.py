import os
import openai
from dotenv import load_dotenv

load_dotenv()

gordon = 'gordon_personality.txt'
jackass = 'jackass_personality.txt'
nerd = 'nerd_personality.txt'

openai.api_key = os.getenv('OPENAI_API_KEY')

start_sequence = "\nSumire:"
input_prompt = "\n\nUser:"
session_prompt = ""
with open(gordon,'r') as file:
    session_prompt = file.read()
chat_log = f'{session_prompt}'

def ask(question): #question, chat_log=None
    prompt_text = f'{chat_log}{input_prompt}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.5,
      max_tokens=250,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    chat_log.join("\n"f'{input_prompt} {question}{start_sequence}{story}')
    return str(story)
