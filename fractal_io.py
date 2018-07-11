from os import listdir
from os.path import isfile, join
import random

VAR_DIR = './variation_styles'

def get_variation_style():
    with open(VAR_DIR) as vd:
        var_list = list(filter(lambda x: x, vd.read().split('\n')))
    return random.choice(var_list)
