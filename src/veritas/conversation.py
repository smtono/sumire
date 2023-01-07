import os
import openai
from dotenv import load_dotenv

load_dotenv()

sumire = os.path.join(os.getcwd(), 'src', 'data', 'personality_scripts', 'sumire_personality.txt')
gordon = os.path.join(os.getcwd(), 'src', 'data', 'personality_scripts', 'gordon_personality.txt')
jackass = os.path.join(os.getcwd(), 'src', 'data', 'personality_scripts', 'jackass_personality.txt')
nerd = os.path.join(os.getcwd(), 'src', 'data', 'personality_scripts', 'nerd_personality.txt')
friendly = os.path.join(os.getcwd(), 'src', 'data', 'personality_scripts', 'friendly_personality.txt')

openai.api_key = os.getenv('OPENAI_API_KEY')

start_sequence = "\nSumire:"
input_prompt = "\n\nUser:"
session_prompt = ""

with open(sumire, 'r') as file:
    session_prompt = file.read()
chat_log = f'{session_prompt}'

def ask(question: str) -> str:
    """
    Generates a response to a question using the GPT-3 API

    Args:
        question: str
            The question raised by the user
    Returns:
        A string response to the question
    """

    prompt_text = f'{chat_log}{input_prompt}: {question}{start_sequence}:'
    
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      max_tokens=250,
      temperature=0.9,
      n=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )

    story = response['choices'][0]['text']
    chat_log.join("\n"f'{input_prompt} {question}{start_sequence}{story}')
    return str(story)
