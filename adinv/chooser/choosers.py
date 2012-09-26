from adinv.chooser.decorator import chooser
import random

@chooser
def pure_random(slot, adverts, *args, **kwargs):
    if len(adverts) == 0:
        return None
    
    return random.choice(adverts)
