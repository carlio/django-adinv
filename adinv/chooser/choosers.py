from adinv.chooser.decorator import chooser
import random

@chooser
def pure_random(slot, *args):
    adverts = list(slot.get_possible_adverts())
    return random.choice(adverts)
