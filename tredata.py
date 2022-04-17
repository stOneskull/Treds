from random import choice


def male_name():
    with open('male', 'r') as names:
        namelist = names.readlines()[7:]
    return choice(namelist).rstrip()


def female_name():
    with open('female', 'r') as names:
        namelist = names.readlines()[7:]
    return choice(namelist).rstrip()


def horse_name():
    from horsenames import namelist
    return choice(namelist()).rstrip()


def choose_name(namelist='both'):
    if namelist == 'all':
        return choice([male_name(), female_name(), horse_name()])
    if namelist == 'both':
        return choice([male_name(), female_name()])
    if namelist == 'male':
        return male_name()
    if namelist == 'female':
        return female_name()
    if namelist == 'horse':
        return horse_name()
    return '23'
