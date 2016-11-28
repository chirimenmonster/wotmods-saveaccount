# SaveAccount: Mod to save account info for World of Tanks ASIA by Chirimen

import BigWorld
from debug_utils import LOG_CURRENT_EXCEPTION
from gui import GUI_SETTINGS

MODNAME = 'SaveAccount'

def init():

    try:
        BigWorld.logInfo(MODNAME, 'change settings to save account info', None)
        
        oldValue1 = GUI_SETTINGS.rememberPassVisible 
        oldValue2 = GUI_SETTINGS.clearLoginValue

        settings = GUI_SETTINGS._GuiSettings__settings
        settings['rememberPassVisible'] = True
        settings['clearLoginValue'] = False
        GUI_SETTINGS._GuiSettings__settings = settings
        
        newValue1 = GUI_SETTINGS.rememberPassVisible 
        newValue2 = GUI_SETTINGS.clearLoginValue

        BigWorld.logInfo(MODNAME, 'GUI_SETTINGS.rememberPassVisible={0}->{1}'.format(oldValue1, newValue1), None)
        BigWorld.logInfo(MODNAME, 'GUI_SETTINGS.clearLoginValue={0}->{1}'.format(oldValue1, newValue2), None)
        
    except:
        LOG_CURRENT_EXCEPTION()
    
