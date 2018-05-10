'''Validation test'''
'''[PSV-2017-0804] Post-auth RCE: Stack overflow in /ddns.cgi through " wan_ping_to_lan " parameter'''
from API._API import *

def test_Step_1():
    log.info('Get id token from debug.htm page')
    get_url = host+'debug.htm'
    tmpHTML = requests.get(get_url,auth=(user,passwd),verify=False)
    tmpToken = re.findall('\?id=[0-9a-z]+',tmpHTML.text)
    token = tmpToken[4]
    print token
    log.info( 'Step-1: Set wan_ping_to_lan(Type:STRING, MaxLen:15) = 192.168.100.111')
    post_url = host  + 'advanced_control.cgi' + token
    post_data = 'wan_ping_to_lan=192.168.100.111&Allow_external_IPv6_hosts_ping_internal_IPv6_hosts=Off'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    log.info('Get id token from debug.htm page')
    get_url = host+'debug.htm'
    tmpHTML = requests.get(get_url,auth=(user,passwd),verify=False)
    tmpToken = re.findall('\?id=[0-9a-z]+',tmpHTML.text)
    token = tmpToken[4]
    print token
    log.info( 'Step-2: Set wan_ping_to_lan(Type:STRING, MaxLen:15) = NetgearShanghai')
    post_url = host  + 'advanced_control.cgi' + token
    post_data = 'wan_ping_to_lan=NetgearShanghai&Allow_external_IPv6_hosts_ping_internal_IPv6_hosts=Off'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    log.info('Get id token from debug.htm page')
    get_url = host+'debug.htm'
    tmpHTML = requests.get(get_url,auth=(user,passwd),verify=False)
    tmpToken = re.findall('\?id=[0-9a-z]+',tmpHTML.text)
    token = tmpToken[4]
    print token
    log.info( 'Step-3: Set wan_ping_to_lan(Type:STRING, MaxLen:15) = NetgearShanghaiATE')
    post_url = host  + 'advanced_control.cgi' + token
    post_data = 'wan_ping_to_lan=NetgearShanghaiATE&Allow_external_IPv6_hosts_ping_internal_IPv6_hosts=Off'
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