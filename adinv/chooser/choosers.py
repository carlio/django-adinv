from adinv.chooser.decorator import chooser
import random

@chooser
def pure_random(slot, adverts, *args, **kwargs):
    return random.choice(adverts)


@chooser
def weighted_random(slot, adverts, *args, **kwargs):

    weights = dict([ (advert.id, int(advert.get_config().get('weight', 0))) for advert in adverts])
    total = sum(weights.values())
    
    rand = random.uniform(0, total)

    upto = 0
    for advert in adverts:
        upto += weights[advert.id]
        if upto > rand:
            return advert

    assert False, "Shouldn't get here"
