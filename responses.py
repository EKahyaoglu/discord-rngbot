# responses.py

import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "*hello":
        return "Hey there :)"

    if p_message == "*roll":
        return str(random.randint(1, 6))

    if p_message == "*help":
        return "This is a help message that you can modify."

    if p_message == "*event":
        return "Join us for our Game Night in <#CHANNELID> in 20 minutes!"