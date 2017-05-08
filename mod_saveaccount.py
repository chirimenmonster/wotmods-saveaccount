# SaveAccount: Mod to save account info for World of Tanks ASIA by Chirimen

import BigWorld
from debug_utils import LOG_CURRENT_EXCEPTION
from gui import GUI_SETTINGS
from helpers import dependency
from skeletons.gui.login_manager import ILoginManager

class MOD:
    AUTHOR = '${author}'
    NAME = '${name}'
    VERSION = '${version}'
    DESCRIPTION = '${description}'
    SUPPORT_URL = '${support_url}'

def init():
    try:
        BigWorld.logInfo(MOD.NAME, '{0} {1} ({2})'.format(MOD.NAME, MOD.VERSION, MOD.SUPPORT_URL), None)
        
        oldValue1 = GUI_SETTINGS.rememberPassVisible 
        oldValue2 = GUI_SETTINGS.clearLoginValue

        GUI_SETTINGS._GuiSettings__settings['rememberPassVisible'] = True
        GUI_SETTINGS._GuiSettings__settings['clearLoginValue'] = False
        
        newValue1 = GUI_SETTINGS.rememberPassVisible 
        newValue2 = GUI_SETTINGS.clearLoginValue

        BigWorld.logInfo(MOD.NAME, 'GUI_SETTINGS.rememberPassVisible = {0} -> {1}'.format(oldValue1, newValue1), None)
        BigWorld.logInfo(MOD.NAME, 'GUI_SETTINGS.clearLoginValue= {0} -> {1}'.format(oldValue2, newValue2), None)

        loginManager = dependency.instance(ILoginManager)
        loginManager.init()
        BigWorld.logInfo(MOD.NAME, 'reload login preference', None)
    except:
        LOG_CURRENT_EXCEPTION()
