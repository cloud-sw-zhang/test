'''Validation test'''
'''[PSV-2017-2015] RCE:stack overflow in /pppoe2_port.cgi through "Port_1" parameter'''
from API._API import *

def test_Step_1():
    token = getIDToken('pppoe2_port_edit.htm')
    log.info( 'Step-1: Set Port_1(Type:NUM, MaxLen:5) as empty')
    post_url = host  + 'pppoe2_port.cgi' + token
    post_data = {
        'trigger': 'Port',
        'Port_1': '',  
        'Port_2': '2',
        'Protocol': 'TCP/UDP',
        'accept': ' Apply ',
        'policyIndex': ''
    }
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('pppoe2_port_edit.htm')
    log.info( 'Step-2: Set Port_1(Type:NUM, MaxLen:5) = 12345')
    post_url = host  + 'pppoe2_port.cgi' + token
    post_data = {
        'trigger': 'Port',
        'Port_1': '12345',  
        'Port_2': '2',
        'Protocol': 'TCP/UDP',
        'accept': ' Apply ',
        'policyIndex': ''
    }
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work."

def test_Step_3():
    token = getIDToken('pppoe2_port_edit.htm')
    log.info( 'Step-3: Set Port_1(Type:NUM, MaxLen:5) = 123456')
    post_url = host  + 'pppoe2_port.cgi' + token
    post_data = {
        'trigger': 'Port',
        'Port_1': '123456',  
        'Port_2': '2',
        'Protocol': 'TCP/UDP',
        'accept': ' Apply ',
        'policyIndex': ''
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
