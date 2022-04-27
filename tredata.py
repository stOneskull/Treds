from random import choice


def male_name():
    with open('male', 'r') as names:
        namelist = names.readlines()[7:]
    return choice(namelist).strip()


def female_name():
    with open('female', 'r') as names:
        namelist = names.readlines()[7:]
    return choice(namelist).strip()


def horse_name():
    with open('horse', 'r') as names:
        namelist = names.readlines()
    return choice(namelist).rstrip()


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
