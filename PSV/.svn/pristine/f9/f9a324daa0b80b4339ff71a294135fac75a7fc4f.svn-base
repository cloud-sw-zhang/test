#encoding=utf8
'''
Created on 2015.10.20
format check lib 
@author: Jim Chen
'''
def check01Format(strText):
    if strText == '0' or strText == '1':
        return True
    else:
        return False

def checkStatusFormat(strText):
    if strText == 'Up' or strText == 'Disable':
        return True
    else:
        return False

def checkSsidFormat(strText):
    if strText == 'None' or (len(strText) > 0 and len(strText) <= 32):
        return True
    else:
        return False
    
def checkRegionFormat(strText):
    listRegion = ['Africa', 'Asia', 'Australia', 'Canada', 'Europe', 'Germany', 'Israel', 'Japan', 'Korea', 'Mexico', 'South America', 'United States', 'Others']
    if strText in listRegion:
        return True
    else:
        return False

def check5gChannelFormat(strText):
    #listChannel = ['36', '40', '44', '48', '149', '153', '157', '161']
    listChannel = ['36', '40', '44', '48', '52', '58', '64', '100', '104', '108', '112', '116', '120', '124', '128', '132', '136', '140', '149', '153', '157', '161']  
    if strText in listChannel:
        return True
    else:
        return False
    
def checkWirelessModeFormat(strText):
    if 'Mbps' in strText and (len(strText) > 0 and len(strText) <= 64):
        return True
    else:
        return False
    
def checkNewBasicEncryptionModesFormat(strText):
    listModes = ['None', 'WEP', 'WPA-PSK', 'WPA2-PSK', 'WPA-PSK/WPA2-PSK']
    if strText in listModes:
        return True
    else:
        return False
    
def checkWEPAuthTypeFormat(strText):
    listWEPAuthType = ['Open', 'Shared', 'Automatic']
    if strText in listWEPAuthType:
        return True
    else:
        return False
    
def checkWPAEncryptionModesFormat(strText):
    listModes = ['None', 'WPA-PSK', 'WPA2-PSK', 'WPA-PSK/WPA2-PSK']
    if strText in listModes:
        return True
    else:
        return False
    
def checkWLANMACAddressFormat(strText):
    if len(strText) != 12:
        return False
    else:
        return True

def checkWPAPassphraseFormat(strText):
    if len(strText) >= 8 and len (strText) <= 64:
        return True
    else:
        return False
    
def checkIpv4AddressFormat(strIP):
    if strIP == '':
        return False
    
    ipList = strIP.split('.')
    if len(ipList) == 4:
        for item in ipList:
            try:
                itemInt = int(item)
            except:
                return False
            if itemInt >= 0 and itemInt <= 255:
                pass
            else:
                return False
        return True
    else:
        return False
