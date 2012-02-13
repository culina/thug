# Xunlei Thunder PPLAYER.DLL_1.WORK ActiveX Control

import logging
log = logging.getLogger("Thug")

def DownURL2(self, arg0, arg1, arg2, arg3):
    if len(arg0) > 1024:
        log.ThugLogging.add_behavior_warn('[Xunlei Thunder PPlayer ActiveX] DownURL2 Overflow')

def SetFlvPlayerUrl(self, val):
    self.__dict__['FlvPlayerUrl'] = val

    if len(val) > 1060:
        log.ThugLogging.add_behavior_warn('[Xunlei Thunder PPlayer ActiveX] FlvPlayerUrl Property Handling Buffer Overflow')

def SetLogo(self, val):
    self.__dict__['Logo'] = val

    if len(val) > 128:
        log.ThugLogging.add_behavior_warn('[Xunlei Thunder PPlayer ActiveX] Remote Overflow Exploit in Logo property')

