'''Validation test'''
'''[PSV-2017-2294] Post-auth RCE: Stack overflow in /usbDetation.cgi through "select" parameter'''

from API._API import *
def test_Step_1():
    token = getIDToken('Modem_connecting.htm')
    log.info( 'Step-1: Set pgbarcount(Type:NUM, MaxLen:2) = 0')
    post_url = host  + 'usbConnecting.cgi' + token

    post_data = 'progress=%7C%7C%7C%7C%7C%7C%7C&Abort=+++Cancel++&pgbarcount=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work."  
    
def test_Step_2():
    token = getIDToken('Modem_connecting.htm')
    log.info( 'Step-2: Set pgbarcount(Type:NUM, MaxLen:2) = 99')
    post_url = host  + 'usbConnecting.cgi' + token
    post_data = 'progress=%7C%7C%7C%7C%7C%7C%7C&Abort=+++Cancel++&pgbarcount=12'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('Modem_connecting.htm')
    log.info( 'Step-3: Set pgbarcount(Type:NUM, MaxLen:2) = 100')
    post_url = host  + 'usbConnecting.cgi' + token
    post_data = 'progress=%7C%7C%7C%7C%7C%7C%7C&Abort=+++Cancel++&pgbarcount=123'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  


