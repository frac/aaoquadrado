from random import choice

def flavor_chooser(request):
    flavors = ["tree", "sea", "red"]
    if "flavor" in request.GET.keys():
        flavor =  request.GET["flavor"]
    else:
        flavor  = choice(flavors)


    return {
        'flavor': flavor,
    }


