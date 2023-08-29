from random import randint

def get_encouraging_message():
    """Returns a one-line encouraging message as a string"""
    
    encouraging_msgs = [
        "Don't worry, you're not dead yet. That means you still have something within you yet.",
        "You got this!",
        "Sending major good vibes your way.",
        "This won't be easy, but you've got what it takes to get through it.",
        "Good luck today! You’ll do great.",
        "Hey, you've got a thing to work on, so get on it!",
        "Remember why you chose to suffer through this.",
        "Keep on going!",
        "A little everyday can go a long way."
    ]
    last_index = len(encouraging_msgs)-1
    rand_index = randint(0, last_index)
    
    return encouraging_msgs[rand_index]