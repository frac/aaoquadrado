from random import choice

QUOTES = (["And, for an instant, she stared directly into those soft blue eyes and knew, with an instinctive mammalian certainty, that the exceedingly rich were no longer even remotely human. ", "William Gibson"],
        ["The 'Net is a waste of time, and that's exactly what's right about it.","William Gibson"],
        ["Why shouldn't we give our teachers a license to obtain software, all software, any software, for nothing? Does anyone demand a licensing fee, each time a child is taught the alphabet?","William Gibson"],
        ["Anyone who considers protocol unimportant has never dealt with a cat.","Robert A. Heinlein"],
        ["Being right too soon is socially unacceptable.","Robert A. Heinlein"],
        ["Never insult anyone by accident.","Robert A. Heinlein"],
        ["Computer science is no more about computers than astronomy is about telescopes.","Edsger Dijkstra"],
        ["Elegance is not a dispensable luxury but a factor that decides between success and failure.","Edsger Dijkstra"],
        ["If 10 years from now, when you are doing something quick and dirty, you suddenly visualize that I am looking over your shoulders and say to yourself: 'Dijkstra would not have liked this', well that would be enough immortality for me. ","Edsger Dijkstra"],
        ["She held out  her hands, palms up, the  white fingers  slightly spread, and with a  barely  audible click, ten double-edged, four-centimeter scalpel blades slid from their housings beneath the burgundy nails.","William Gibson"],
        ["Everything happens to everybody sooner or later if there is time enough.","George Bernard Shaw "],
        ["True greatness is measured by how much freedom you give to others, not by how much you can coerce others to do what you want.","Larry Wall"],
        ["A human being should be able to change a diaper, plan an invasion, butcher a hog, conn a ship, design a building, write a sonnet, balance accounts, build a wall, set a bone, comfort the dying, take orders, give orders, cooperate, act alone, solve equations, analyze a new problem, pitch manure, program a computer, cook a tasty meal, fight efficiently, die gallantly. Specialization is for insects.","Robert A. Heinlein"],
        ["Be less curious about people and more curious about ideas.","Marie Curie"],
        ["Intelligence is the ability to avoid doing work, yet getting the work done. ","Linus Torvalds"],
        ["Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program.","Linus Torvalds"],
        ["You won't get sued for anticompetitive behavior.","Linus Torvalds"],
        )
"""
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],
        ["",""],

"""
def flavor_chooser(request):
    flavors = ["tree", "sea", "red"]
    if "flavor" in request.GET.keys():
        flavor =  request.GET["flavor"]
    else:
        flavor  = choice(flavors)
    quote = choice(QUOTES)

    return {
        'flavor': flavor,
        'quote': quote,
    }

