'''Validation test'''
'''[PSV-2017-2294] Post-auth RCE: Stack overflow in /usbDetation.cgi through "select" parameter'''

from API._API import *

def test_Step_1():
    token = getIDToken('WLG_bridge_wireless_settings.htm')
    log.info('Step-1: Set passphrase_an(Type:PASSWORD, MaxLen:64) = 0')
    post_url = host  + 'bridge_wireless_main.cgi' + token
    post_data = 'Cancel=Cancel&interface=Wireless+Networks+%282.4Ghz+b%2Fg%2Fn%29&ssid=ttxs2018&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=12345678&ssid_an=ttxs2018-5g&security_type_an=WPA2-PSK&passphrase_an=&tempSetting=0&wds_enable=0&wds_enable_an=0&only_mode=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&initAuthType=automatic&initDefaultKey=0&initAuthType_an=automatic&initDefaultKey_an=0&telec_dfs_ch_enable=1&enable_stamode=0&wireless_interface=1&fw_sku=SKU_WW'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should not work."  

def test_Step_2():
    token = getIDToken('WLG_bridge_wireless_settings.htm')
    log.info('Step-2: Set passphrase_an(Type:PASSWORD, MaxLen:64) as 64 characters')
    post_url = host  + 'bridge_wireless_main.cgi' + token
    a = 'a' * 64
    post_data = 'Cancel=Cancel&interface=Wireless+Networks+%282.4Ghz+b%2Fg%2Fn%29&ssid=ttxs2018&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=12345678&ssid_an=ttxs2018-5g&security_type_an=WPA2-PSK&passphrase_an=' + a + '&tempSetting=0&wds_enable=0&wds_enable_an=0&only_mode=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&initAuthType=automatic&initDefaultKey=0&initAuthType_an=automatic&initDefaultKey_an=0&telec_dfs_ch_enable=1&enable_stamode=0&wireless_interface=1&fw_sku=SKU_WW'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('WLG_bridge_wireless_settings.htm')
    log.info('Step-3: Set passphrase_an(Type:PASSWORD, MaxLen:64) as 65 characters')
    post_url = host  + 'bridge_wireless_main.cgi' + token
    a = 'a' * 65
    post_data = 'Cancel=Cancel&interface=Wireless+Networks+%282.4Ghz+b%2Fg%2Fn%29&ssid=ttxs2018&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=12345678&ssid_an=ttxs2018-5g&security_type_an=WPA2-PSK&passphrase_an=' + a + '&tempSetting=0&wds_enable=0&wds_enable_an=0&only_mode=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&initAuthType=automatic&initDefaultKey=0&initAuthType_an=automatic&initDefaultKey_an=0&telec_dfs_ch_enable=1&enable_stamode=0&wireless_interface=1&fw_sku=SKU_WW'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  

def test_Step_4():
    log.info('Step-4:DUT loaddefault')
    aploaddefault()
    Genie_overleap()
    Disable_changedToken()
    token = getIDToken('WLG_bridge_wireless_settings.htm')
    log.info(token)