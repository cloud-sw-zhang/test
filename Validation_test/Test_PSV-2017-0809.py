'''Validation test'''
'''[PSV-2017-0809] Post-auth RCE: Stack overflow in /keyword.cgi through "bs_enable" parameter'''
from API._API import *

def test_Step_1():
    token = getIDToken('BKS_keyword.htm')
    log.info( 'Step-1: Set bs_enable(Type:INDEX, MaxLen:1, Range=0~2) = 0')
    post_url = host  + 'keyword.cgi' + token
    post_data = 'wzWAN_IPFinish=Apply&skeyword=perschedule&cfKeyWord_Domain=&bs_enable=0&bs_trustedip_enable=0&bs_trustedip=192.168.1.0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('BKS_keyword.htm')
    log.info( 'Step-2: Set bs_enable(Type:INDEX, MaxLen:1, Range=0~2) = 2')
    post_url = host  + 'keyword.cgi' + token
    post_data = 'wzWAN_IPFinish=Apply&skeyword=perschedule&cfKeyWord_Domain=&bs_enable=2&bs_trustedip_enable=0&bs_trustedip=192.168.1.0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('BKS_keyword.htm')
    log.info( 'Step-3: Set bs_enable(Type:INDEX, MaxLen:1, Range=0~2) = -1')
    post_url = host  + 'keyword.cgi' + token
    post_data = 'wzWAN_IPFinish=Apply&skeyword=perschedule&cfKeyWord_Domain=&bs_enable=-1&bs_trustedip_enable=0&bs_trustedip=192.168.1.0'
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
    token = getIDToken('BKS_keyword.htm')
    log.info( 'Step-4: Set bs_enable(Type:INDEX, MaxLen:1, Range=0~2) = 3')
    post_url = host  + 'keyword.cgi' + token
    post_data = 'wzWAN_IPFinish=Apply&skeyword=perschedule&cfKeyWord_Domain=&bs_enable=3&bs_trustedip_enable=0&bs_trustedip=192.168.1.0'
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