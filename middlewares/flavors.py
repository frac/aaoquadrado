from random import choice

def flavor_chooser(request):
    flavors = ["tree", "sea", "red"]
    flavor  = choice(flavors)

    return {
        'flavor': flavor,
    }


