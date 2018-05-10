'''Validation test'''
'''[PSV-2017-2294] Post-auth RCE: Stack overflow in /ia_ap_setting.cgi through "select" parameter'''
from API._API import *

def test_Step_1():
    token = getIDToken('IA_AP_settings.htm')
    log.info( 'Step-1: Set current_flow(Type:STRING, MaxLen:15) as empty')
    post_url = host  + 'ia_ap_setting.cgi' + token
    post_data = 'ssid=NETGEAR&ssid_5g=NETGEAR-5G&use_same_sec=on&security_type=None&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=&ssid_5g_ap_mode=NETGEAR-5G&security_type_5g=None&wepenc_5g=1&wep_key_no_5g=1&KEY_5g1=&KEY_5g2=&KEY_5g3=&KEY_5g4=&passphrase_5g=&enable_ap_mode=&wl_same_sec=1&current_flow=&pc_or_mobile=PC&ap_24g_sec=None&ap_5g_sec=None&mode=&ap_band=&eth_bind_band=&sta_band='
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    time.sleep(120)
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('IA_AP_settings.htm')
    log.info( 'Step-2: Set current_flow(Type:STRING, MaxLen:15) = ABCDEFGHIJKLMNO')
    post_url = host  + 'ia_ap_setting.cgi' + token
    post_data = 'ssid=NETGEAR&ssid_5g=NETGEAR-5G&use_same_sec=on&security_type=None&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=&ssid_5g_ap_mode=NETGEAR-5G&security_type_5g=None&wepenc_5g=1&wep_key_no_5g=1&KEY_5g1=&KEY_5g2=&KEY_5g3=&KEY_5g4=&passphrase_5g=&enable_ap_mode=&wl_same_sec=1&current_flow=ABCDEFGHIJKLMNO&pc_or_mobile=PC&ap_24g_sec=None&ap_5g_sec=None&mode=&ap_band=&eth_bind_band=&sta_band='
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
    time.sleep(120)
    
    assert tmpHTML.status_code == 200, "This action should work."  

def test_Step_3():
    token = getIDToken('IA_AP_settings.htm')
    log.info( 'Step-3: Set current_flow(Type:STRING, MaxLen:15) = ABCDEFGHIJKLMNOP')
    post_url = host  + 'ia_ap_setting.cgi' + token
    post_data = 'ssid=NETGEAR&ssid_5g=NETGEAR-5G&use_same_sec=on&security_type=None&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=&ssid_5g_ap_mode=NETGEAR-5G&security_type_5g=None&wepenc_5g=1&wep_key_no_5g=1&KEY_5g1=&KEY_5g2=&KEY_5g3=&KEY_5g4=&passphrase_5g=&enable_ap_mode=&wl_same_sec=1&current_flow=ABCDEFGHIJKLMNOPQ&pc_or_mobile=PC&ap_24g_sec=None&ap_5g_sec=None&mode=&ap_band=&eth_bind_band=&sta_band='
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
    time.sleep(120)
    
    assert tmpHTML.status_code == 400, "This action should not work."      
