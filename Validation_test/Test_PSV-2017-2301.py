'''Validation test'''
'''[PSV-2017-2294] Post-auth RCE: Stack overflow in /usbDetation.cgi through "select" parameter'''

from API._API import *

def test_Step_1():
    token = getIDToken('RU_BSW_fail.htm')
    log.info( 'Step-1: Set select(Type:INDEX, MaxLen:1, Range:0~2) = 0')
    post_url = host  + 'blkDetWan.cgi' + token
    post_data = 'select=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('RU_BSW_fail.htm')
    log.info( 'Step-2: Set select(Type:INDEX, MaxLen:1, Range:0~2) = 1')
    post_url = host  + 'blkDetWan.cgi' + token
    post_data = 'select=1'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    
    assert tmpHTML.status_code == 200, "This action should work." 
    
def test_Step_3():
    token = getIDToken('RU_BSW_fail.htm')
    log.info( 'Step-3: Set select(Type:INDEX, MaxLen:1, Range:0~2) = 2')
    post_url = host  + 'blkDetWan.cgi' + token
    post_data = 'select=2'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    
    assert tmpHTML.status_code == 200, "This action should work." 
    
def test_Step_4():
    token = getIDToken('RU_BSW_fail.htm')
    log.info( 'Step-4: Set select(Type:INDEX, MaxLen:1, Range:0~2) = 3')
    post_url = host  + 'blkDetWan.cgi' + token
    post_data = 'select=3'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  

