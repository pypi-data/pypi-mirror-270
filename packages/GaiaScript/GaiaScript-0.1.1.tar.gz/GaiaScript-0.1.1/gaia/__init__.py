import os
from gaia._template import TemplateManager
from ._exceptions import *

SCRIPTS_FOLDER = './scripts/'
TEMPLATE_SCRIPTS_FOLDER = SCRIPTS_FOLDER + 'template/'
DEBUG_SCRIPTS_FOLDER = SCRIPTS_FOLDER + 'debug/'
WORK_SCRIPTS_FOLDER = SCRIPTS_FOLDER + 'work/'

os.makedirs(SCRIPTS_FOLDER, exist_ok=True)
os.makedirs(DEBUG_SCRIPTS_FOLDER, exist_ok=True)
os.makedirs(TEMPLATE_SCRIPTS_FOLDER, exist_ok=True)
os.makedirs(WORK_SCRIPTS_FOLDER, exist_ok=True)


def get_template_script_manager():
    return TemplateManager(TEMPLATE_SCRIPTS_FOLDER)
