'''Validation test'''
'''[PSV-2017-0806] Post-auth RCE: Stack overflow in /upnp.cgi through "hiddenTurnUPnPOn" parameter'''
from API._API import *

def test_Step_1():
    token = getIDToken('UPNP_upnp.htm')
    log.info( 'Step-1: Set hiddenTurnUPnPOn(Type:BOOL, MaxLen:1) = 0')
    post_url = host  + 'upnp.cgi' + token
    post_data = 'apply=Apply&UPnP=UPnP&AdverTime=30&TimeToLive=4&hiddenTurnUPnPOn=0&hiddenAdverTime=30&hiddenTimeToLive=4'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('UPNP_upnp.htm')
    log.info( 'Step-2: Set hiddenTurnUPnPOn(Type:BOOL, MaxLen:1) = 1')
    post_url = host  + 'upnp.cgi' + token
    post_data = 'apply=Apply&UPnP=UPnP&AdverTime=30&TimeToLive=4&hiddenTurnUPnPOn=1&hiddenAdverTime=30&hiddenTimeToLive=4'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('UPNP_upnp.htm')
    log.info( 'Step-3: Set hiddenTurnUPnPOn(Type:BOOL, MaxLen:1) = 2')
    post_url = host  + 'upnp.cgi' + token
    post_data = 'apply=Apply&UPnP=UPnP&AdverTime=30&TimeToLive=4&hiddenTurnUPnPOn=2&hiddenAdverTime=30&hiddenTimeToLive=4'
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
    token = getIDToken('UPNP_upnp.htm')
    log.info( 'Step-4: Set hiddenTurnUPnPOn(Type:BOOL, MaxLen:1) = -1')
    post_url = host  + 'upnp.cgi' + token
    post_data = 'apply=Apply&UPnP=UPnP&AdverTime=30&TimeToLive=4&hiddenTurnUPnPOn=-1&hiddenAdverTime=30&hiddenTimeToLive=4'
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
