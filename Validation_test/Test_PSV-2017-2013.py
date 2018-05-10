'''Validation test'''
'''[PSV-2017-2013] RCE:stack overflow in /pppoe2_ip.cgi through "tempIP" parameter'''
from API._API import *

def test_Step_1():
    token = getIDToken('pppoe2_ip_edit.htm')
    log.info( 'Step-1: Set tempIP(Type:IP, MaxLen:15) as empty')
    post_url = host  + 'pppoe2_ip.cgi' + token
    post_data = {
        'trigger': 'IP Address',
        'Addr1': '1',
        'Addr2': '1',
        'Addr3': '1',
        'Addr4': '1',
        'Addr5': '123',
        'Protocol': 'TCP/UDP',
        'accept': ' Apply ',
        'startIP': '',
        'policyIndex': '',
        'tempIP': '', 
        'endIP4': ''
    }
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

def test_Step_2():
    token = getIDToken('pppoe2_ip_edit.htm')
    log.info( 'Step-2: Set tempIP(Type:IP, MaxLen:15) = 192.168.100.100')
    post_url = host  + 'pppoe2_ip.cgi' + token
    post_data = {
        'trigger': 'IP Address',
        'Addr1': '1',
        'Addr2': '1',
        'Addr3': '1',
        'Addr4': '1',
        'Addr5': '123',
        'Protocol': 'TCP/UDP',
        'accept': ' Apply ',
        'startIP': '',
        'policyIndex': '',
        'tempIP': '192.168.100.100',
        'endIP4': ''
    }
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work."
    
def test_Step_3():
    token = getIDToken('pppoe2_ip_edit.htm')
    log.info( 'Step-3: Set tempIP(Type:IP, MaxLen:15) = 192.168.100.256')
    post_url = host  + 'pppoe2_ip.cgi' + token
    post_data = {
        'trigger': 'IP Address',
        'Addr1': '1',
        'Addr2': '1',
        'Addr3': '1',
        'Addr4': '1',
        'Addr5': '123',
        'Protocol': 'TCP/UDP',
        'accept': ' Apply ',
        'startIP': '',
        'policyIndex': '',
        'tempIP': '192.168.100.256',
        'endIP4': ''
    }
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
    
def test_Step_4():
    token = getIDToken('pppoe2_ip_edit.htm')
    log.info( 'Step-4: Set tempIP(Type:IP, MaxLen:15) = 192.168.100.1000')
    post_url = host  + 'pppoe2_ip.cgi' + token
    post_data = {
        'trigger': 'IP Address',
        'Addr1': '1',
        'Addr2': '1',
        'Addr3': '1',
        'Addr4': '1',
        'Addr5': '123',
        'Protocol': 'TCP/UDP',
        'accept': ' Apply ',
        'startIP': '',
        'policyIndex': '',
        'tempIP': '192.168.100.1000',
        'endIP4': ''
    }
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
