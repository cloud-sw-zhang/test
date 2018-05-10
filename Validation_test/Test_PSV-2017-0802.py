'''Validation test'''
'''[PSV-2017-0802] Post-auth RCE: Stack overflow in /security.cgi through "dmz_ip" parameter'''
from API._API import *

def test_Step_1():
    token = getIDToken('WAN_wan.htm')
    log.info( 'Step-1: Set dmz_ip(Type:IP, MaxLen:15) = 192.168.100.111')
    post_url = host  + 'security.cgi' + token
    post_data = 'apply=Apply&dmz_enable=dmz_enable&dmzip1=192&dmzip2=168&dmzip3=100&dmzip4=111&disable_gproxy=disable_gproxy&wan_mtu=1500&NatInboundFiltering=Secured&wan_way=1500&nat_inbound_filtering=1&wan_proto=dhcp&nvram_mtu=1500&dmz_ip=192.168.100.111'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work."

def test_Step_2():
    token = getIDToken('WAN_wan.htm')
    log.info( 'Step-2: Set dmz_ip(Type:IP, MaxLen:15) = 192.168.100.257')
    post_url = host  + 'security.cgi' + token
    post_data = 'apply=Apply&dmz_enable=dmz_enable&dmzip1=192&dmzip2=168&dmzip3=100&dmzip4=1111&disable_gproxy=disable_gproxy&wan_mtu=1500&NatInboundFiltering=Secured&wan_way=1500&nat_inbound_filtering=1&wan_proto=dhcp&nvram_mtu=1500&dmz_ip=192.168.100.257'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        time.sleep(3)
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 400, "This action should not work."
    
def test_Step_3():
    token = getIDToken('WAN_wan.htm')
    log.info( 'Step-3: Set dmz_ip(Type:IP, MaxLen:15) = 192.168.100.1000')
    post_url = host  + 'security.cgi' + token
    post_data = 'apply=Apply&dmz_enable=dmz_enable&dmzip1=192&dmzip2=168&dmzip3=100&dmzip4=1111&disable_gproxy=disable_gproxy&wan_mtu=1500&NatInboundFiltering=Secured&wan_way=1500&nat_inbound_filtering=1&wan_proto=dhcp&nvram_mtu=1500&dmz_ip=192.168.100.1000'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        time.sleep(3)
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 400, "This action should not work." 
