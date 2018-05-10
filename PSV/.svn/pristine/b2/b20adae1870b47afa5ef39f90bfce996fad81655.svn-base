'''[PSV-2017-0331] Wireless settings update CSRF at /wireless.cgi  '''
''' anthor Cloud 2017-12-08'''
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
    log.info("step-1 Wireless setting update CSRF at /wireless.cgi--wireless ssid should not change")
    url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
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
    if console_type == 'cable':
        post_url = host + 'goform/WirelessSettings' + token
        data ='uthAlgm=automatic&wepenc=1&passphraseStr=&KEY1=0000000000&KEY1Hidden=0000000000&KEY2=0000000000&KEY2Hidden=0000000000&KEY3=0000000000&KEY3Hidden=0000000000&KEY4=0000000000&KEY4Hidden=0000000000&passphrase=WUXCNJGL&passphraseHidden=WUXCNJGL&enterprise_encryptmode_2G=1&group_key_update_interval_2G=0&radius_server_2G_1=0&radius_server_2G_2=0&radius_server_2G_3=0&radius_server_2G_4=0&radius_port_2G=1812&radius_key_2G=&ssid_bc_an=ssid_5G_bc&ssid_an=NETGEAR-6501-5G&w_channel_an=Auto&w_channel_an_drv=153&opmode_an=600Mbps&security_type_an=WPA2-PSK&authAlgm_an=automatic&wepenc_an=1&passphraseStr_an=&KEY1_an=0000000000&KEY1Hidden_an=0000000000&KEY2_an=0000000000&KEY2Hidden_an=0000000000&KEY3_an=0000000000&KEY3Hidden_an=0000000000&KEY4_an=0000000000&KEY4Hidden_an=0000000000&passphrase_an=WUXCNJGL&passphraseHidden_an=WUXCNJGL&enterprise_encryptmode_5G=1&group_key_update_interval_5G=0&radius_server_5G_1=0&radius_server_5G_2=0&radius_server_5G_3=0&radius_server_5G_4=0&radius_port_5G=1812&radius_key_5G=&tempSetting=&tempRegion=11&setRegion=11&wds_enable=0&wds_enable_an=0&only_mode=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&initChannel=0&initAuthType=automatic&initDefaultKey=0&initChannel_an=153&initAuthType_an=automatic&initDefaultKey_an=0&dfs_ch_enable=1&dfs_ch_enable_default=&auto_channel_5G=1&display_5G=1&fw_sku=SKU_NA'
    else:
        post_url = host + 'wireless.cgi' + token
        data ='Apply=Apply&ssid_bc=ssid_24G_bc&ssid=xxxxxxxxxxxxxxx&w_channel=0&opmode=300Mbps&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=unusualcanoe339&encryptmode=1&wpa_en_gk_int=3600&RADIUSAddr1_wla=&RADIUSAddr2_wla=&RADIUSAddr3_wla=&RADIUSAddr4_wla=&wpa_en_radius_port=1812&wpa_en_radius_ss=&ssid_bc_an=ssid_5G_bc&ssid_an=NETGEAR01-5G&w_channel_an=44&opmode_an=HT80&security_type_an=WPA2-PSK&authAlgm_an=automatic&wepenc_an=1&wep_key_no_an=1&KEY1_an=&KEY2_an=&KEY3_an=&KEY4_an=&passphrase_an=unusualcanoe339&encryptmode_an=1&wpa_en_gk_int_wlg=3600&RADIUSAddr1_wlg=&RADIUSAddr2_wlg=&RADIUSAddr3_wlg=&RADIUSAddr4_wlg=&wpa_en_radius_port_wlg=1812&wpa_en_radius_ss_wlg=&ssid_bc_an_2=ssid_5G_bc&ssid_an_2=NETGEAR01-5G-2&w_channel_an_2=153&opmode_an_2=HT80&security_type_an_2=WPA2-PSK&authAlgm_an_2=automatic&wepenc_an_2=1&wep_key_no_an_2=1&KEY1_an_2=&KEY2_an_2=&KEY3_an_2=&KEY4_an_2=&passphrase_an_2=unusualcanoe339&encryptmode_an_2=1&wpa_en_gk_int_wlh=3600&RADIUSAddr1_wlh=&RADIUSAddr2_wlh=&RADIUSAddr3_wlh=&RADIUSAddr4_wlh=&wpa_en_radius_port_wlh=1812&wpa_en_radius_ss_wlh=&sku_name=NA&tempSetting=0&tempRegion=5&setRegion=11&wds_enable=0&wds_enable_an=0&only_mode=0&band_steering_5g=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&security_type_5G_2=WPA2-PSK&init_security_type_2G=WPA2-PSK&init_security_type_5G=WPA2-PSK&init_security_type_5G_2=WPA2-PSK&init_passhprase_5G_2=unusualcanoe339&init_ssid_5G_2=NETGEAR01-5G-2&initChannel=0&initAuthType=automatic&initDefaultKey=0&initChannel_an=44&initAuthType_an=automatic&initDefaultKey_an=0&initChannel_an_2=153&initAuthType_an_2=automatic&initDefaultKey_an_2=0&telec_dfs_ch_enable=1&ce_dfs_ch_enable=&fcc_dfs_ch_enable=&auto_channel_5G=1&support_ac_mode=1&board_id=U12H334T00_NETGEAR&enable_band_steering=0&fw_sku=SKU_WW&fw_sku=SKU_NA&wla_radius_ipaddr=0.0.0.0&wlg_radius_ipaddr=0.0.0.0&wla_ent_secu_type=WPA-AUTO&wlg_ent_secu_type=WPA-AUTO&wan_ipaddr=10.7.5.219&wan_netmask=255.0.0.0&wlh_radius_ipaddr=0.0.0.0&wlh_ent_secu_type=WPA-AUTO&wlh_ent_secu_port=1812&wlh_ent_secu_interval=3600&wlh_radius_secret=&wifi_dual_5g_band=1&init_ssid_bc_an_2=checked&init_opmode_an_2=20000'
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '': 
        log.info(r.status_code)
        log.info('Send it again using same TokenID')
    if console_type == 'cable':
        data1 ='Apply=Apply&ssid_bc=ssid_24G_bc&ssid=MickSSID_FinalChanges&w_channel=Auto&w_channel_drv=0&opmode=300Mbps&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&passphraseStr=&KEY1=0000000000&KEY1Hidden=0000000000&KEY2=0000000000&KEY2Hidden=0000000000&KEY3=0000000000&KEY3Hidden=0000000000&KEY4=0000000000&KEY4Hidden=0000000000&passphrase=WUXCNJGL&passphraseHidden=WUXCNJGL&enterprise_encryptmode_2G=1&group_key_update_interval_2G=0&radius_server_2G_1=0&radius_server_2G_2=0&radius_server_2G_3=0&radius_server_2G_4=0&radius_port_2G=1812&radius_key_2G=&ssid_bc_an=ssid_5G_bc&ssid_an=NETGEAR-6501-5G&w_channel_an=Auto&w_channel_an_drv=153&opmode_an=600Mbps&security_type_an=WPA2-PSK&authAlgm_an=automatic&wepenc_an=1&passphraseStr_an=&KEY1_an=0000000000&KEY1Hidden_an=0000000000&KEY2_an=0000000000&KEY2Hidden_an=0000000000&KEY3_an=0000000000&KEY3Hidden_an=0000000000&KEY4_an=0000000000&KEY4Hidden_an=0000000000&passphrase_an=WUXCNJGL&passphraseHidden_an=WUXCNJGL&enterprise_encryptmode_5G=1&group_key_update_interval_5G=0&radius_server_5G_1=0&radius_server_5G_2=0&radius_server_5G_3=0&radius_server_5G_4=0&radius_port_5G=1812&radius_key_5G=&tempSetting=&tempRegion=11&setRegion=11&wds_enable=0&wds_enable_an=0&only_mode=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&initChannel=0&initAuthType=automatic&initDefaultKey=0&initChannel_an=153&initAuthType_an=automatic&initDefaultKey_an=0&dfs_ch_enable=1&dfs_ch_enable_default=&auto_channel_5G=1&display_5G=1&fw_sku=SKU_NA'
    else:
        data1 ='Apply=Apply&ssid_bc=ssid_24G_bc&ssid=Mick_FinalChanges&w_channel=0&opmode=300Mbps&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=unusualcanoe339&encryptmode=1&wpa_en_gk_int=3600&RADIUSAddr1_wla=&RADIUSAddr2_wla=&RADIUSAddr3_wla=&RADIUSAddr4_wla=&wpa_en_radius_port=1812&wpa_en_radius_ss=&ssid_bc_an=ssid_5G_bc&ssid_an=NETGEAR01-5G&w_channel_an=44&opmode_an=HT80&security_type_an=WPA2-PSK&authAlgm_an=automatic&wepenc_an=1&wep_key_no_an=1&KEY1_an=&KEY2_an=&KEY3_an=&KEY4_an=&passphrase_an=unusualcanoe339&encryptmode_an=1&wpa_en_gk_int_wlg=3600&RADIUSAddr1_wlg=&RADIUSAddr2_wlg=&RADIUSAddr3_wlg=&RADIUSAddr4_wlg=&wpa_en_radius_port_wlg=1812&wpa_en_radius_ss_wlg=&ssid_bc_an_2=ssid_5G_bc&ssid_an_2=NETGEAR01-5G-2&w_channel_an_2=153&opmode_an_2=HT80&security_type_an_2=WPA2-PSK&authAlgm_an_2=automatic&wepenc_an_2=1&wep_key_no_an_2=1&KEY1_an_2=&KEY2_an_2=&KEY3_an_2=&KEY4_an_2=&passphrase_an_2=unusualcanoe339&encryptmode_an_2=1&wpa_en_gk_int_wlh=3600&RADIUSAddr1_wlh=&RADIUSAddr2_wlh=&RADIUSAddr3_wlh=&RADIUSAddr4_wlh=&wpa_en_radius_port_wlh=1812&wpa_en_radius_ss_wlh=&sku_name=NA&tempSetting=0&tempRegion=5&setRegion=11&wds_enable=0&wds_enable_an=0&only_mode=0&band_steering_5g=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&security_type_5G_2=WPA2-PSK&init_security_type_2G=WPA2-PSK&init_security_type_5G=WPA2-PSK&init_security_type_5G_2=WPA2-PSK&init_passhprase_5G_2=unusualcanoe339&init_ssid_5G_2=NETGEAR01-5G-2&initChannel=0&initAuthType=automatic&initDefaultKey=0&initChannel_an=44&initAuthType_an=automatic&initDefaultKey_an=0&initChannel_an_2=153&initAuthType_an_2=automatic&initDefaultKey_an_2=0&telec_dfs_ch_enable=1&ce_dfs_ch_enable=&fcc_dfs_ch_enable=&auto_channel_5G=1&support_ac_mode=1&board_id=U12H334T00_NETGEAR&enable_band_steering=0&fw_sku=SKU_WW&fw_sku=SKU_NA&wla_radius_ipaddr=0.0.0.0&wlg_radius_ipaddr=0.0.0.0&wla_ent_secu_type=WPA-AUTO&wlg_ent_secu_type=WPA-AUTO&wan_ipaddr=10.7.5.219&wan_netmask=255.0.0.0&wlh_radius_ipaddr=0.0.0.0&wlh_ent_secu_type=WPA-AUTO&wlh_ent_secu_port=1812&wlh_ent_secu_interval=3600&wlh_radius_secret=&wifi_dual_5g_band=1&init_ssid_bc_an_2=checked&init_opmode_an_2=20000'
    r1 = ''
    try:
        r1 = requests.post(post_url, headers=headers, data=data1,timeout=5)
    except:
        time.sleep(1)
    if r1 != '':
        log.info(r1.status_code)

def test_Step_2():
    log.info( 'step-2 check wireless ssid ')
    driver = webdriver.Firefox()
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlWirelessSetup
    driver.get(url)
    time.sleep(15)
    ssidname = driver.find_element_by_name("ssid").get_attribute('value')
    time.sleep(5)
    driver.quit()
    if ssidname == 'xxxxxxxxxxxxxxx' or ssidname == 'MickSSID_FinalChanges':
        case = 'fail'
    else:
        case = 'pass'
    assert case == 'pass', "This action should not work." 