'''Validation test'''
'''[PSV-2017-2294] Post-auth RCE: Stack overflow in /usbDetation.cgi through "select" parameter'''

from API._API import *

def test_Step_1():
    token = getIDToken('USB_basic_readycloud_msg.htm')
    log.info( 'Step-1: Set password(Type:USERNAME, MaxLen:64) as empty')
    post_url = host  + 'usb_remote_invite.cgi' + token
    post_data = 'yes_admin=Yes&username=&password=&Register=do_register'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should not work."  
    
def test_Step_2():
    token = getIDToken('USB_basic_readycloud_msg.htm')
    log.info( 'Step-2: Set password(Type:USERNAME, MaxLen:64) as 64 characters')
    post_url = host  + 'usb_remote_invite.cgi' + token
    a = 'x' * 64
    post_data = 'yes_admin=Yes&username=&password=' + a + '&Register=do_register'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('USB_basic_readycloud_msg.htm')
    log.info( 'Step-3: Set password(Type:USERNAME, MaxLen:64) as 65 characters')
    post_url = host  + 'usb_remote_invite.cgi' + token
    a = 'x' * 65
    post_data = 'yes_admin=Yes&username=&password=' + a + '&Register=do_register'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work." 


