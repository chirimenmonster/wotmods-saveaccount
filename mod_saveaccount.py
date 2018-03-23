"""WoT mod to save account information"""

import BigWorld
from debug_utils import LOG_CURRENT_EXCEPTION
from gui import GUI_SETTINGS
from helpers import dependency
from skeletons.gui.login_manager import ILoginManager

class MOD:
    """mod's information"""
    AUTHOR = '${author}'
    NAME = '${name}'
    VERSION = '${version}'
    DESCRIPTION = '${description}'
    SUPPORT_URL = '${support_url}'

SETTINGS = { 'rememberPassVisible': True, 'clearLoginValue': False }

def init():
    """called on mod's initialization phase"""
    try:
        BigWorld.logInfo(MOD.NAME, '{0} {1} ({2})'.format(MOD.NAME, MOD.VERSION, MOD.SUPPORT_URL), None)

        oldValues = { k:getattr(GUI_SETTINGS, k) for k in SETTINGS.keys() }

        for k, v in SETTINGS.items():
            if oldValues[k] != v:
                GUI_SETTINGS._GuiSettings__settings[k] = v

        newValues = { k:getattr(GUI_SETTINGS, k) for k in SETTINGS.keys() }

        for k in SETTINGS.keys():
            BigWorld.logInfo(MOD.NAME, 'GUI_SETTINGS.{0} = {1} -> {2}'.format(k, oldValues[k], newValues[k]), None)
        
        if newValues != oldValues:
            loginManager = dependency.instance(ILoginManager)
            loginManager.init()
            BigWorld.logInfo(MOD.NAME, 'reload login preference', None)
    except:
        LOG_CURRENT_EXCEPTION()
