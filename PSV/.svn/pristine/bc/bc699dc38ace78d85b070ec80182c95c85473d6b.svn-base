'''Validation test'''
'''[PSV-2017-2019]  RCE:stack overflow in /vlan_rule.cgi through "vlan_name" parameter'''

from API._API import *

def test_Step_1():
    token = getIDToken('VLAN_IPTV_add.htm')
    log.info( 'Step-1: Set vlan_name(Type:STRING, MaxLen:10) = 12345A')
    post_url = host  + 'vlan_rule.cgi' + token
    post_data = 'apply=Add&vlan_name=12345A&vlan_id=5&vlan_prio=0&vlan_ports_3=on&vlan_ports_5=on&vlan_rule_name=Internet&vlan_mode=add&wifi_dual_5g_band='
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('VLAN_IPTV_add.htm')
    log.info( 'Step-2: Set vlan_name(Type:STRING, MaxLen:10) = 0123456789A')
    post_url = host  + 'vlan_rule.cgi' + token
    post_data = 'apply=Add&vlan_name=0123456789A&vlan_id=5&vlan_prio=0&vlan_ports_3=on&vlan_ports_5=on&vlan_rule_name=Internet&vlan_mode=add&wifi_dual_5g_band='
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  
