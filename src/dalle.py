import openai

def ask(question: str):
    response = openai.Image.create(
        prompt=' '.join(question),
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url
