'''Validation test'''
'''[PSV-2017-2294] Post-auth RCE: Stack overflow in /usbDetation.cgi through "select" parameter'''

from API._API import *

def test_Step_1():
    token = getIDToken('Modem_welcome.htm')
    log.info( 'Step-1: Set select(Type:INDEX, MaxLen:16) = 0')
    post_url = host  + 'usbDetation.cgi' + token
    post_data = 'next=+++Next+++&select=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('Modem_welcome.htm')
    log.info( 'Step-2: Set select(Type:INDEX, MaxLen:16) = 4')
    post_url = host  + 'usbDetation.cgi' + token
    post_data = 'next=+++Next+++&select=4'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work."  

def test_Step_3():
    token = getIDToken('Modem_welcome.htm')
    log.info( 'Step-3: Set select(Type:INDEX, MaxLen:16) = -1')
    post_url = host  + 'usbDetation.cgi' + token
    post_data = 'next=+++Next+++&select=-1'
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
    token = getIDToken('Modem_welcome.htm')
    log.info( 'Step-4: Set select(Type:INDEX, MaxLen:1, Range:0~4) = 5')
    post_url = host  + 'usbDetation.cgi' + token
    post_data = 'next=+++Next+++&select=5'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  
