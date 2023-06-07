import random
from memes import get_random_meme_url

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This bot is in development the current features are: \n !meme for a christian meme \n !roll for a dice roll`"

    if p_message == '!meme':
        image_url = get_random_meme_url()
        return image_url

    return 'Yeah, I don\'t know. Try typing "!help".'
