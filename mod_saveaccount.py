# SaveAccount: Mod to save account info for World of Tanks ASIA by Chirimen

import BigWorld
from debug_utils import LOG_CURRENT_EXCEPTION
from gui import GUI_SETTINGS

MOD_NAME = 'SaveAccount'
MOD_VERSION = '1.1'

def init():

    try:
        BigWorld.logInfo(MOD_NAME, '{0} version {1}, mod to save account info'.format(MOD_NAME, MOD_VERSION), None)
        
        oldValue1 = GUI_SETTINGS.rememberPassVisible 
        oldValue2 = GUI_SETTINGS.clearLoginValue

        GUI_SETTINGS._GuiSettings__settings['rememberPassVisible'] = True
        GUI_SETTINGS._GuiSettings__settings['clearLoginValue'] = False
        
        newValue1 = GUI_SETTINGS.rememberPassVisible 
        newValue2 = GUI_SETTINGS.clearLoginValue

        BigWorld.logInfo(MOD_NAME, 'GUI_SETTINGS.rememberPassVisible = {0} -> {1}'.format(oldValue1, newValue1), None)
        BigWorld.logInfo(MOD_NAME, 'GUI_SETTINGS.clearLoginValue= {0} -> {1}'.format(oldValue2, newValue2), None)
        
    except:
        LOG_CURRENT_EXCEPTION()
    
