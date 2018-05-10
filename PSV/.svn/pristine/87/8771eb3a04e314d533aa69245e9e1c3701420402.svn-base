'''Validation test'''
'''[PSV-2017-2294] Post-auth RCE: Stack overflow in /usbDetation.cgi through "select" parameter'''

from API._API import *

def test_Step_1():
    token = getIDToken('WLG_ap_dual_band.htm')
    log.info('Step-1: Set apmode_netmask(Type:IP, MaxLen:15) as empty')
    post_url = host  + 'ap_mode.cgi' + token
    a = ''
    post_data = 'Cancel=Cancel&enable_fixed_ip_setting=enable_dynamic_ip_setting&WPethr1=0&WPethr2=0&WPethr3=0&WPethr4=0&WMask1=0&WMask2=0&WMask3=0&WMask4=0&WGateway1=0&WGateway2=0&WGateway3=0&WGateway4=0&DAddr1=0&DAddr2=0&DAddr3=0&DAddr4=0&PDAddr1=&PDAddr2=&PDAddr3=&PDAddr4=&apmode_ipaddr=0.0.0.0&apmode_netmask=' + a + '&apmode_gateway=0.0.0.0&apmode_dns_sel=&apmode_dns1_pri=0.0.0.0&apmode_dns1_sec=&apmode_page=1'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  
    
def test_Step_2():
    token = getIDToken('WLG_ap_dual_band.htm')
    log.info('Step-2: Set apmode_netmask(Type:IP, MaxLen:15) = 192.168.100.100')
    post_url = host  + 'ap_mode.cgi' + token
    a = '192.168.100.100'
    post_data = 'Cancel=Cancel&enable_fixed_ip_setting=enable_dynamic_ip_setting&WPethr1=0&WPethr2=0&WPethr3=0&WPethr4=0&WMask1=0&WMask2=0&WMask3=0&WMask4=0&WGateway1=0&WGateway2=0&WGateway3=0&WGateway4=0&DAddr1=0&DAddr2=0&DAddr3=0&DAddr4=0&PDAddr1=&PDAddr2=&PDAddr3=&PDAddr4=&apmode_ipaddr=0.0.0.0&apmode_netmask=' + a + '&apmode_gateway=0.0.0.0&apmode_dns_sel=&apmode_dns1_pri=0.0.0.0&apmode_dns1_sec=&apmode_page=1'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('WLG_ap_dual_band.htm')
    log.info('Step-3: Set apmode_netmask(Type:IP, MaxLen:15) = 192.168.100.1000')
    post_url = host  + 'ap_mode.cgi' + token
    a = '192.168.100.1000'
    post_data = 'Cancel=Cancel&enable_fixed_ip_setting=enable_dynamic_ip_setting&WPethr1=0&WPethr2=0&WPethr3=0&WPethr4=0&WMask1=0&WMask2=0&WMask3=0&WMask4=0&WGateway1=0&WGateway2=0&WGateway3=0&WGateway4=0&DAddr1=0&DAddr2=0&DAddr3=0&DAddr4=0&PDAddr1=&PDAddr2=&PDAddr3=&PDAddr4=&apmode_ipaddr=0.0.0.0&apmode_netmask=' + a + '&apmode_gateway=0.0.0.0&apmode_dns_sel=&apmode_dns1_pri=0.0.0.0&apmode_dns1_sec=&apmode_page=1'
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
    log.info('Step-4: DUT loaddefault')
    aploaddefault()
    Genie_overleap()
    Disable_changedToken()