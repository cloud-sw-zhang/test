'''Validation test'''
'''[PSV-2017-2294] Post-auth RCE: Stack overflow in /usbDetation.cgi through "select" parameter'''

from API._API import *

def test_Step_1():
    token = getIDToken('Adv_USB.htm')
    log.info( 'Step-1: Set addSN1(Type:STRING, MaxLen:200) as empty')
    post_url = host  + 'usb_approve.cgi' + token
    post_data = 'Add=Add&addNum=0&addSN0=0904160801033550234808&addVolume0=Security_Only&addName0=General UDisk &addCap0=7.6GB&addSN1=&addVolume1=NEW VOLUME&addName1=SanDisk Cruzer Micro &addCap1=1.9GB'
    post_data = 'Add=Add&addNum=0&addSN0=&addVolume0=Security_Only&addName0=General++UDisk+++++++++++&addCap0=7.6GB'
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
    token = getIDToken('Adv_USB.htm')
    log.info( 'Step-2: Set addSN1(Type:STRING, MaxLen:200) as 200 characters')
    post_url = host  + 'usb_approve.cgi' + token
    a = 'a' * 200
    post_data = 'Add=Add&addNum=0&addSN0=0904160801033550234808&addVolume0=Security_Only&addName0=General UDisk &addCap0=7.6GB&addSN1=' + a + '&addVolume1=NEW VOLUME&addName1=SanDisk Cruzer Micro &addCap1=1.9GB'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('Adv_USB.htm')
    log.info( 'Step-3: Set addSN1(Type:STRING, MaxLen:200) as 201 characters')
    post_url = host  + 'usb_approve.cgi' + token
    a = 'a' * 201
    post_data = 'Add=Add&addNum=0&addSN0=0904160801033550234808&addVolume0=Security_Only&addName0=General UDisk &addCap0=7.6GB&addSN1=' + a + '&addVolume1=NEW VOLUME&addName1=SanDisk Cruzer Micro &addCap1=1.9GB'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  

