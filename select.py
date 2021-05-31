from lab7 import main as lab7_main
from lab8 import main as lab8_main
from lab9 import main as lab9_main
from lab10 import main as lab10_main


def selectLab(labNom):
    if labNom == '7':
        lab7_main.window()
    if labNom == '8':
        lab8_main.window()
    if labNom == '9':
        lab9_main.window()
    if labNom == '10':
        lab10_main.window()
