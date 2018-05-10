'''Validation test'''
'''[PSV-2017-2226] Post-Auth RCE via BO in 0x543cc on WLG_wireless_tri_band.htm'''

from API._API import *

def test_Step_1():
    token = getIDToken('WLG_wireless_dual_band_r10.htm')
    log.info( 'Step-1: Set wpa_en_gk_int_wlg(Type:NUM, MaxLen:5) = 3600')
    post_url = host  + 'wireless.cgi' + token
    post_data = 'Apply=Apply&ssid_bc=ssid_24G_bc&enable_coexistence=enable_coexistence&ssid=ttxs2018&w_channel=0&opmode=300Mbps&enable_tpc=1&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=12345678&encryptmode=1&wpa_en_gk_int=3600&RADIUSAddr1_wla=&RADIUSAddr2_wla=&RADIUSAddr3_wla=&RADIUSAddr4_wla=&wpa_en_radius_port=1812&wpa_en_radius_ss=&ssid_bc_an=ssid_5G_bc&ssid_an=ttxs2018-5g&w_channel_an=153&opmode_an=HT80&enable_tpc_an=1&security_type_an=WPA2-PSK&authAlgm_an=automatic&wepenc_an=1&wep_key_no_an=1&KEY1_an=&KEY2_an=&KEY3_an=&KEY4_an=&passphrase_an=12345678&encryptmode_an=1&wpa_en_gk_int_wlg=3600&RADIUSAddr1_wlg=&RADIUSAddr2_wlg=&RADIUSAddr3_wlg=&RADIUSAddr4_wlg=&wpa_en_radius_port_wlg=1812&wpa_en_radius_ss_wlg=&tempSetting=0&tempRegion=5&setRegion=11&wds_enable=0&wds_enable_an=0&only_mode=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&gui_security_type_5G=&init_security_type_2G=WPA2-PSK&init_security_type_5G=WPA2-PSK&initChannel=0&initAuthType=automatic&initDefaultKey=0&initChannel_an=153&initAuthType_an=automatic&initDefaultKey_an=0&telec_dfs_ch_enable=1&ce_dfs_ch_enable=&fcc_dfs_ch_enable=&auto_channel_5G=1&support_ac_mode=1&board_id=U12H270T20_NETGEAR&fw_sku=SKU_WW&fw_sku=SKU_NA&wla_radius_ipaddr=0.0.0.0&wlg_radius_ipaddr=0.0.0.0&wla_ent_secu_type=WPA-AUTO&wlg_ent_secu_type=WPA-AUTO&wan_ipaddr=10.0.0.245&wan_netmask=255.255.255.0&select_2g_tpc=1&select_5g_tpc=1&wifi_2g_enable=Enable&wifi_5g_enable=Enable'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('WLG_wireless_dual_band_r10.htm')
    log.info( 'Step-2: Set wpa_en_gk_int_wlg(Type:NUM, MaxLen:5) = 65535')
    post_url = host  + 'wireless.cgi' + token
    post_data = 'Apply=Apply&ssid_bc=ssid_24G_bc&enable_coexistence=enable_coexistence&ssid=ttxs2018&w_channel=0&opmode=300Mbps&enable_tpc=1&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=12345678&encryptmode=1&wpa_en_gk_int=3600&RADIUSAddr1_wla=&RADIUSAddr2_wla=&RADIUSAddr3_wla=&RADIUSAddr4_wla=&wpa_en_radius_port=1812&wpa_en_radius_ss=&ssid_bc_an=ssid_5G_bc&ssid_an=ttxs2018-5g&w_channel_an=153&opmode_an=HT80&enable_tpc_an=1&security_type_an=WPA2-PSK&authAlgm_an=automatic&wepenc_an=1&wep_key_no_an=1&KEY1_an=&KEY2_an=&KEY3_an=&KEY4_an=&passphrase_an=12345678&encryptmode_an=1&wpa_en_gk_int_wlg=65535&RADIUSAddr1_wlg=&RADIUSAddr2_wlg=&RADIUSAddr3_wlg=&RADIUSAddr4_wlg=&wpa_en_radius_port_wlg=1812&wpa_en_radius_ss_wlg=&tempSetting=0&tempRegion=5&setRegion=11&wds_enable=0&wds_enable_an=0&only_mode=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&gui_security_type_5G=&init_security_type_2G=WPA2-PSK&init_security_type_5G=WPA2-PSK&initChannel=0&initAuthType=automatic&initDefaultKey=0&initChannel_an=153&initAuthType_an=automatic&initDefaultKey_an=0&telec_dfs_ch_enable=1&ce_dfs_ch_enable=&fcc_dfs_ch_enable=&auto_channel_5G=1&support_ac_mode=1&board_id=U12H270T20_NETGEAR&fw_sku=SKU_WW&fw_sku=SKU_NA&wla_radius_ipaddr=0.0.0.0&wlg_radius_ipaddr=0.0.0.0&wla_ent_secu_type=WPA-AUTO&wlg_ent_secu_type=WPA-AUTO&wan_ipaddr=10.0.0.245&wan_netmask=255.255.255.0&select_2g_tpc=1&select_5g_tpc=1&wifi_2g_enable=Enable&wifi_5g_enable=Enable'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('WLG_wireless_dual_band_r10.htm')
    log.info( 'Step-3: Set wpa_en_gk_int_wlg(Type:NUM, MaxLen:5) = 65536')
    post_url = host  + 'wireless.cgi' + token
    post_data = 'Apply=Apply&ssid_bc=ssid_24G_bc&enable_coexistence=enable_coexistence&ssid=ttxs2018&w_channel=0&opmode=300Mbps&enable_tpc=1&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=12345678&encryptmode=1&wpa_en_gk_int=3600&RADIUSAddr1_wla=&RADIUSAddr2_wla=&RADIUSAddr3_wla=&RADIUSAddr4_wla=&wpa_en_radius_port=1812&wpa_en_radius_ss=&ssid_bc_an=ssid_5G_bc&ssid_an=ttxs2018-5g&w_channel_an=153&opmode_an=HT80&enable_tpc_an=1&security_type_an=WPA2-PSK&authAlgm_an=automatic&wepenc_an=1&wep_key_no_an=1&KEY1_an=&KEY2_an=&KEY3_an=&KEY4_an=&passphrase_an=12345678&encryptmode_an=1&wpa_en_gk_int_wlg=65536&RADIUSAddr1_wlg=&RADIUSAddr2_wlg=&RADIUSAddr3_wlg=&RADIUSAddr4_wlg=&wpa_en_radius_port_wlg=1812&wpa_en_radius_ss_wlg=&tempSetting=0&tempRegion=5&setRegion=11&wds_enable=0&wds_enable_an=0&only_mode=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&gui_security_type_5G=&init_security_type_2G=WPA2-PSK&init_security_type_5G=WPA2-PSK&initChannel=0&initAuthType=automatic&initDefaultKey=0&initChannel_an=153&initAuthType_an=automatic&initDefaultKey_an=0&telec_dfs_ch_enable=1&ce_dfs_ch_enable=&fcc_dfs_ch_enable=&auto_channel_5G=1&support_ac_mode=1&board_id=U12H270T20_NETGEAR&fw_sku=SKU_WW&fw_sku=SKU_NA&wla_radius_ipaddr=0.0.0.0&wlg_radius_ipaddr=0.0.0.0&wla_ent_secu_type=WPA-AUTO&wlg_ent_secu_type=WPA-AUTO&wan_ipaddr=10.0.0.245&wan_netmask=255.255.255.0&select_2g_tpc=1&select_5g_tpc=1&wifi_2g_enable=Enable&wifi_5g_enable=Enable'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    
    assert tmpHTML.status_code == 400, "This action should work." 
    
def test_Step_4():
    token = getIDToken('WLG_wireless_dual_band_r10.htm')
    log.info( 'Step-4: Set wpa_en_gk_int_wlg(Type:NUM, MaxLen:5) = 123456')
    post_url = host  + 'wireless.cgi' + token
    post_data = 'Apply=Apply&ssid_bc=ssid_24G_bc&enable_coexistence=enable_coexistence&ssid=ttxs2018&w_channel=0&opmode=300Mbps&enable_tpc=1&security_type=WPA2-PSK&authAlgm=automatic&wepenc=1&wep_key_no=1&KEY1=&KEY2=&KEY3=&KEY4=&passphrase=12345678&encryptmode=1&wpa_en_gk_int=3600&RADIUSAddr1_wla=&RADIUSAddr2_wla=&RADIUSAddr3_wla=&RADIUSAddr4_wla=&wpa_en_radius_port=1812&wpa_en_radius_ss=&ssid_bc_an=ssid_5G_bc&ssid_an=ttxs2018-5g&w_channel_an=153&opmode_an=HT80&enable_tpc_an=1&security_type_an=WPA2-PSK&authAlgm_an=automatic&wepenc_an=1&wep_key_no_an=1&KEY1_an=&KEY2_an=&KEY3_an=&KEY4_an=&passphrase_an=12345678&encryptmode_an=1&wpa_en_gk_int_wlg=123456&RADIUSAddr1_wlg=&RADIUSAddr2_wlg=&RADIUSAddr3_wlg=&RADIUSAddr4_wlg=&wpa_en_radius_port_wlg=1812&wpa_en_radius_ss_wlg=&tempSetting=0&tempRegion=5&setRegion=11&wds_enable=0&wds_enable_an=0&only_mode=0&show_wps_alert=0&security_type_2G=WPA2-PSK&security_type_5G=WPA2-PSK&gui_security_type_5G=&init_security_type_2G=WPA2-PSK&init_security_type_5G=WPA2-PSK&initChannel=0&initAuthType=automatic&initDefaultKey=0&initChannel_an=153&initAuthType_an=automatic&initDefaultKey_an=0&telec_dfs_ch_enable=1&ce_dfs_ch_enable=&fcc_dfs_ch_enable=&auto_channel_5G=1&support_ac_mode=1&board_id=U12H270T20_NETGEAR&fw_sku=SKU_WW&fw_sku=SKU_NA&wla_radius_ipaddr=0.0.0.0&wlg_radius_ipaddr=0.0.0.0&wla_ent_secu_type=WPA-AUTO&wlg_ent_secu_type=WPA-AUTO&wan_ipaddr=10.0.0.245&wan_netmask=255.255.255.0&select_2g_tpc=1&select_5g_tpc=1&wifi_2g_enable=Enable&wifi_5g_enable=Enable'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    
    assert tmpHTML.status_code == 400, "This action should work." 