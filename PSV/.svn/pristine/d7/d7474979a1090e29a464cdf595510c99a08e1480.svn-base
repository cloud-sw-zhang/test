from API._API import *

def test_Step_1():
    token = getIDToken('BAS_pppoe_flet.htm')
    log.info( 'Step-1: Set FletType(Type:INDEX, MaxLen:1, Range:0~2) = 0')
    post_data = "apply=Apply&login_type=PPPoE&pppoe_username=guest&pppoe_passwd=&pppoe_servicename=&pppoe_dod=1&pppoe_idletime=5&WANAssign=Dynamic&DNSAssign=0&FletSel=fletenable&session_type=NTT East&pppoe2_username=guest@flets&pppoe2_passwd=guest&pppoe2_servicename=&WANAssign2=Dynamic&DNSAssign2=0&NTT_EAST=on&runtest=no&wan_ipaddr=0.0.0.0&wan2_ipaddr=0.0.0.0&pppoe_localip=0.0.0.0&wan_dns_sel=0&wan_dns1_pri=...&wan_dns1_sec=...&pppoe2_localip=0.0.0.0&wan2_dns_sel=0&wan_dns2_pri=...&wan_dns2_sec=...&FletType=0&ToDisable=&whichTest=&pppoe_temp=4"
    post_url = host  + 'pppoe2.cgi' + token
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
        time.sleep(60)
        
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('BAS_pppoe_flet.htm')
    log.info( 'Step-2: Set FletType(Type:INDEX, MaxLen:1, Range:0~2) = 2')
    post_url = host  + 'pppoe2.cgi' + token
    post_data = "apply=Apply&login_type=PPPoE&pppoe_username=guest&pppoe_passwd=&pppoe_servicename=&pppoe_dod=1&pppoe_idletime=5&WANAssign=Dynamic&DNSAssign=0&FletSel=fletenable&session_type=NTT East&pppoe2_username=guest@flets&pppoe2_passwd=guest&pppoe2_servicename=&WANAssign2=Dynamic&DNSAssign2=0&NTT_EAST=on&runtest=no&wan_ipaddr=0.0.0.0&wan2_ipaddr=0.0.0.0&pppoe_localip=0.0.0.0&wan_dns_sel=0&wan_dns1_pri=...&wan_dns1_sec=...&pppoe2_localip=0.0.0.0&wan2_dns_sel=0&wan_dns2_pri=...&wan_dns2_sec=...&FletType=2&ToDisable=&whichTest=&pppoe_temp=4"
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
        time.sleep(60)
        
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('BAS_pppoe_flet.htm')
    log.info( 'Step-3: Set FletType(Type:INDEX, MaxLen:1, Range:0~2) = 3')
    post_url = host  + 'pppoe2.cgi' + token
    post_data = "apply=Apply&login_type=PPPoE&pppoe_username=guest&pppoe_passwd=&pppoe_servicename=&pppoe_dod=1&pppoe_idletime=5&WANAssign=Dynamic&DNSAssign=0&FletSel=fletenable&session_type=NTT East&pppoe2_username=guest@flets&pppoe2_passwd=guest&pppoe2_servicename=&WANAssign2=Dynamic&DNSAssign2=0&NTT_EAST=on&runtest=no&wan_ipaddr=0.0.0.0&wan2_ipaddr=0.0.0.0&pppoe_localip=0.0.0.0&wan_dns_sel=0&wan_dns1_pri=...&wan_dns1_sec=...&pppoe2_localip=0.0.0.0&wan2_dns_sel=0&wan_dns2_pri=...&wan_dns2_sec=...&FletType=3&ToDisable=&whichTest=&pppoe_temp=4"
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        time.sleep(3)
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
        time.sleep(60)
        
    assert tmpHTML.status_code == 400, "This action should not work."
