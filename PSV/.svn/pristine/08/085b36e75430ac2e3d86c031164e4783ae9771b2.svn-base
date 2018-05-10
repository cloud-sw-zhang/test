'''Validation test'''
'''[PSV-2017-0308] Stack overflow in fwLog.cgi through "log_refresh" parameter and others (RCE)'''
from API._API import *

def test_Step_1():
    token = getIDToken('pppoe2_domain_edit.htm')
    log.info( 'Step-1: Set policyIndex(Type:NUM, MaxLen:7) as empty')
    post_url = host  + 'pppoe2_domain.cgi' + token
    post_data = {
        'trigger': 'Domain Name',
        'domain': 'test',
        'accept': 'Apply',
        'policyIndex': ''
    }
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work."

def test_Step_2():
    token = getIDToken('pppoe2_domain_edit.htm')
    log.info( 'Step-2: Set policyIndex(Type:NUM, MaxLen:7) = 1234567')
    post_url = host  + 'pppoe2_domain.cgi' + token
    post_data = {
        'trigger': 'Domain Name',
        'domain': 'test',
        'accept': 'Apply',
        'policyIndex': '1234567'
    }
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work."

def test_Step_3():
    token = getIDToken('pppoe2_domain_edit.htm')
    log.info( 'Step-3: Set policyIndex(Type:NUM, MaxLen:7) = 12345678')
    post_url = host  + 'pppoe2_domain.cgi' + token
    post_data = {
        'trigger': 'Domain Name',
        'domain': 'test',
        'accept': 'Apply',
        'policyIndex': '12345678'
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
