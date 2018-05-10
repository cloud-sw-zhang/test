'''Validation test'''
'''[PSV-2017-2254] Post-Auth RCe via stamode_netmask on WLG_adv_dual_band2.htm'''

from API._API import *

def test_Step_1():
    token = getIDToken('WLG_adv_dual_band2.htm')
    log.info( 'step-1:set normal value. stamode_netmask=0.0.0.0')
    post_url = host  + 'wlg_adv.cgi' + token
    post_data = 'Apply=Apply&enable_ap=enable_ap&frag=2346&rts=2347&enable_shortpreamble=&enable_ap_an=w_5g_enable_ap&frag_an=2346&rts_an=2347&enable_shortpreamble_an=&pin_disable=1&prevent_pin_compromise=1&pin_attack_count=3&wsc_config=on&wsc_config_an=on&enable_implicit_beamforming=enable&enable_atf=enable&enable_mu_mimo=enable&wps_enable=enabled&show_wps_alert=0&wifi_2g_state=Enable&wifi_5g_state=Enable&wifi_2g_sche=&wifi_2g_sche_onoff=0&wifi_5g_sche=&wifi_5g_sche_onoff=0&wifi_2g_sche_num=0&wifi_5g_sche_num=0&ntp_synced_flag=1&select_2g_sche=-1&select_5g_sche=-1&ssid_2g=ttxs2018&ssid_5g=ttxs2018-5g&secu_type_2g=WPA2-PSK&secu_type_5g=WPA2-PSK&passphrase_2g=12345678&passphrase_5g=12345678&apmode_ipaddr=0.0.0.0&apmode_netmask=0.0.0.0&apmode_gateway=0.0.0.0&apmode_dns_sel=&apmode_dns1_pri=0.0.0.0&apmode_dns1_sec=&sta_mode=0&ap_mode=0&stamode_ipaddr=0.0.0.0&stamode_netmask=0.0.0.0&stamode_gateway=0.0.0.0&stamode_dns1_pri=0.0.0.0&stamode_dns1_sec=&wifi_button=1&enable_band_steering=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('WLG_adv_dual_band2.htm')
    log.info( 'step-2:set overflow. stamode_netmask=255.255.255.1024')
    post_url = host  + 'wlg_adv.cgi' + token
    post_data = 'Apply=Apply&enable_ap=enable_ap&frag=2346&rts=2347&enable_shortpreamble=&enable_ap_an=w_5g_enable_ap&frag_an=2346&rts_an=2347&enable_shortpreamble_an=&pin_disable=1&prevent_pin_compromise=1&pin_attack_count=3&wsc_config=on&wsc_config_an=on&enable_implicit_beamforming=enable&enable_atf=enable&enable_mu_mimo=enable&wps_enable=enabled&show_wps_alert=0&wifi_2g_state=Enable&wifi_5g_state=Enable&wifi_2g_sche=&wifi_2g_sche_onoff=0&wifi_5g_sche=&wifi_5g_sche_onoff=0&wifi_2g_sche_num=0&wifi_5g_sche_num=0&ntp_synced_flag=1&select_2g_sche=-1&select_5g_sche=-1&ssid_2g=ttxs2018&ssid_5g=ttxs2018-5g&secu_type_2g=WPA2-PSK&secu_type_5g=WPA2-PSK&passphrase_2g=12345678&passphrase_5g=12345678&apmode_ipaddr=0.0.0.0&apmode_netmask=0.0.0.0&apmode_gateway=0.0.0.0&apmode_dns_sel=&apmode_dns1_pri=0.0.0.0&apmode_dns1_sec=&sta_mode=0&ap_mode=0&stamode_ipaddr=0.0.0.0&stamode_netmask=255.255.255.1024&stamode_gateway=0.0.0.0&stamode_dns1_pri=0.0.0.0&stamode_dns1_sec=&wifi_button=1&enable_band_steering=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  
