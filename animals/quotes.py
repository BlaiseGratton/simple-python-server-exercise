import random


QUOTES = [
    'Everybody has a plan until they get punched in the face.',
    'People don\'t think it be that way, but it do.',
    'Be dangerous - it\'s careful out there!',
    'It is what it is.',
    'Carpe diem',
    'Who did he tell you that to?'
]


def get_all_quotes():
    return QUOTES


def get_random_quote():
    return random.choice(QUOTES)