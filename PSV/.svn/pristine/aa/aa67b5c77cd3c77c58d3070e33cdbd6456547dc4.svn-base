'''Validation test'''
'''[PSV-2017-2227] Post-Auth RCE via workGroup parameter in USB-basic.htm'''
from API._API import *

def test_Step_0():
    token = getIDToken('DEV_name.htm')
    log.info( 'Step-1: Set device_name(Type:DEVICE_NAME, MaxLen:16) = R7000')
    post_url = host  + 'devname_consolidation.cgi' + token
    post_data = 'buttonHit=&buttonValue=&device_name=R8000&dev_name_nv=&devname2readyshare=0&change_readyshare=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        judje_dutReboot(tmpHTML.text)
        time.sleep(60)

def test_Step_1():
    token = getIDToken('DEV_name.htm')
    log.info( 'Step-1: Set device_name(Type:DEVICE_NAME, MaxLen:16) = R8000')
    post_url = host  + 'devname_consolidation.cgi' + token
    post_data = 'buttonHit=&buttonValue=&device_name=R8000&dev_name_nv=&devname2readyshare=0&change_readyshare=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        judje_dutReboot(tmpHTML.text)
        time.sleep(60)
        
    assert tmpHTML.status_code == 200, "This action should work." 
    
def test_Step_2():
    token = getIDToken('DEV_name.htm')
    log.info( 'Step-2: Set device_name(Type:DEVICE_NAME, MaxLen:16) = 0123456789ABCDEF')
    post_url = host  + 'devname_consolidation.cgi' + token
    post_data = 'buttonHit=&buttonValue=&device_name=0123456789ABCDEF&dev_name_nv=&devname2readyshare=0&change_readyshare=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        judje_dutReboot(tmpHTML.text)
        time.sleep(60)
        
    assert tmpHTML.status_code == 200, "This action should work." 
    
def test_Step_3():
    token = getIDToken('DEV_name.htm')
    log.info( 'Step-3: Set device_name(Type:DEVICE_NAME, MaxLen:16) = 0123456789ABCDEFG')
    post_url = host  + 'devname_consolidation.cgi' + token
    post_data = 'buttonHit=&buttonValue=&device_name=0123456789ABCDEFG&dev_name_nv=&devname2readyshare=0&change_readyshare=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        judje_dutReboot(tmpHTML.text)
        time.sleep(60)
        
    assert tmpHTML.status_code == 400, "This action should not work."  

