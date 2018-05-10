'''Validation test'''
'''[PSV-2017-2294] Post-auth RCE: Stack overflow in /usbDetation.cgi through "select" parameter'''

from API._API import *

def test_Step_1():
    token = getIDToken('Modem_pin.htm')
    log.info( 'Step-1: Set reboot_options(Type:STRING, MaxLen:3) as empty')
    post_url = host  + 'usbPIN_edit.cgi' + token
    post_data = 'Back=+++Back+++&Next=+++Next+++&reboot_options='
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
    token = getIDToken('Modem_pin.htm')
    log.info( 'Step-2: Set length normal reboot_options = ATE')
    post_url = host  + 'usbPIN_edit.cgi' + token
    post_data = 'Back=+++Back+++&Next=+++Next+++&reboot_options=ATE'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('Modem_pin.htm')
    log.info( 'Step-3: Set length overflow reboot_options = ABCD')
    post_url = host  + 'usbPIN_edit.cgi' + token
    post_data = 'Back=+++Back+++&Next=+++Next+++&reboot_options=ABCD'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  


