'''Validation test'''
'''[PSV-2017-0810] Post-auth RCE: Stack overflow in /openvpn_hidden.cgi through "openvpn_iface_type" parameter'''
from API._API import *

def test_Step_1():
    token = getIDToken('OPENVPN_hidden.htm')
    log.info( 'Step-1: Set openvpn_iface_type(Type:STRING, MaxLen:3) as empty')
    post_url = host  + 'openvpn_hidden.cgi' + token
    post_data = {
        'cfAlert_Apply': 'Apply',
        'openvpnActive': 'openvpnEnable',
        'openvpn_iface_type': '',
        'openvpn_protocol': 'tcp',
        'openvpn_service_port': '12974',
        'openvpn_br_ip_start': '',
        'openvpn_br_ip_end': '',
        'openvpn_server_ip': '',
        'openvpn_ca': '',
        'openvpn_server_ca': '',
        'openvpn_server_key': '',
        'openvpn_server_dh': '',
        'openvpn_push1': '',
        'openvpn_push2': '',
    }
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('OPENVPN_hidden.htm')
    log.info( 'Step-2: Set openvpn_iface_type(Type:STRING, MaxLen:3) = ATE')
    post_url = host  + 'openvpn_hidden.cgi' + token
    post_data = {
        'cfAlert_Apply': 'Apply',
        'openvpnActive': 'openvpnEnable',
        'openvpn_iface_type': 'ATE',
        'openvpn_protocol': 'tcp',
        'openvpn_service_port': '12974',
        'openvpn_br_ip_start': '',
        'openvpn_br_ip_end': '',
        'openvpn_server_ip': '',
        'openvpn_ca': '',
        'openvpn_server_ca': '',
        'openvpn_server_key': '',
        'openvpn_server_dh': '',
        'openvpn_push1': '',
        'openvpn_push2': '',
    }
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work."

def test_Step_3():
    token = getIDToken('OPENVPN_hidden.htm')
    log.info( 'Step-3: Set openvpn_iface_type(Type:STRING, MaxLen:3) = ATE1')
    post_url = host  + 'openvpn_hidden.cgi' + token
    post_data = {
        'cfAlert_Apply': 'Apply',
        'openvpnActive': 'openvpnEnable',
        'openvpn_iface_type': 'ATE1',
        'openvpn_protocol': 'tcp',
        'openvpn_service_port': '12974',
        'openvpn_br_ip_start': '',
        'openvpn_br_ip_end': '',
        'openvpn_server_ip': '',
        'openvpn_ca': '',
        'openvpn_server_ca': '',
        'openvpn_server_key': '',
        'openvpn_server_dh': '',
        'openvpn_push1': '',
        'openvpn_push2': '',
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
