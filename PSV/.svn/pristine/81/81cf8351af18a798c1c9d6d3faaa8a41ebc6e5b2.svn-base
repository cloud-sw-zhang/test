''' PSV-2017-2427] Post-Auth RCE via passphrase_an parameter in WLG_bridge_wireless_settings.htm  '''
''' anthor Cloud 2018-01-04'''
'''v1.0 '''
from API._API import *

# #def test_step_0():
    # #log.info( 'step-0-0 dut loaddrfault wait 160s')
    # #aploaddefault()
    # #log.info( "step-0-1 AP Genie over leap done")
    # #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 Post-Auth RCE via passphrase_an parameter in WLG_bridge_wireless_settings.htm')
    if console_type == 'cable':
        print 'This case NA'
        case = 'fail'
    else:
        url = host + 'WLG_bridge_wireless_settings.htm'
        token = getIDToken(url)
        tirgger_page = 'Congratulations2_ap_mode.htm'
        cgi = 'bridge_wireless_main.cgi'
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
        headers = {'Authorization': Authorization}
        payload = 'a' * 0x104
        payload += 'dead' # R4
        payload += 'dead' # R5
        payload += struct.pack("I", 0x94dc0)
        data = {
            'Apply':'123',
            'interface':'Wireless Networks (2.4Ghz b/g/n)',
            'ssid':'NETGEAR88',
            'security_type':'WPA2-PSK',
            'authAlgm':'automatic',
            'wepenc':'1',
            'wep_key_no':'1',
            'KEY1':'',
            'KEY2':'',
            'KEY3':'',
            'KEY4':'',
            'passphrase':'wideskates103',
            'ssid_an':'NETGEAR88-5G',
            'security_type_an':'WPA2-PSK',
            'passphrase_an':payload,
            'tempSetting':'0',
            'wds_enable':'0',
            'wds_enable_an':'0',
            'only_mode':'0',
            'show_wps_alert':'0',
            'security_type_2G':'WPA2-PSK',
            'security_type_5G':'WPA2-PSK',
            'initAuthType':'automatic',
            'initDefaultKey':'0',
            'initAuthType_an':'automatic',
            'initDefaultKey_an':'0',
            'telec_dfs_ch_enable':'1',
            'enable_stamode':'0',
            'wireless_interface':'1',
            'fw_sku':'SKU_WW',
            'fw_sku':'SKU_NA'
        }
        post_url = host + '%s' % cgi + token
        log.info(payload)
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        log.info(r.status_code)
        if r.status_code == 401 or r.status_code == 404:
            case1 = 'pass'
        else:
            case1 = 'fail'
        time.sleep(2)
        r1 = requests.get('http://' + hostip + '/%s' % (tirgger_page), headers=headers)
        log.info(r1.status_code)
        if r1.status_code == 401 or r1.status_code == 404:
            case2 = 'pass'
        else:
            case2 = 'fail'
        if case1 == 'pass' and case2 == 'pass':
            case = 'pass'
        else:
            case = 'fail'
    assert case == 'pass', "The function should work." 
