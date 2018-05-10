'''Validation test'''
'''[PSV-2017-0308] Stack overflow in fwLog.cgi through "log_refresh" parameter and others (RCE)'''
from API._API import *

def test_Step_1():
    token = getIDToken('BKS_service_add.htm')
    log.info( 'Step-1: Set userdefined(Type:STRING, MaxLen:30) as empty')
    post_url = host  + 'fw_serv_add.cgi' + token
    post_data = 'apply=Add&service_type=User+Defined&protocol=TCP&portstart=5000&portend=5000&userdefined=&f_pcip1=192&f_pcip2=168&f_pcip3=1&f_pcip4=&f_startip1=192&f_startip2=168&f_startip3=1&f_startip4=&f_endip1=192&f_endip2=168&f_endip3=1&f_endip4=&iptype=all&which_mode=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('BKS_service_add.htm')
    log.info( 'Step-2: Set userdefined(Type:STRING, MaxLen:30) = 11111111112222222222ABCDEFGHIJ')
    post_url = host  + 'fw_serv_add.cgi' + token
    post_data = 'apply=Add&service_type=User+Defined&protocol=TCP&portstart=5000&portend=5000&userdefined=111111111122222222223333333333&f_pcip1=192&f_pcip2=168&f_pcip3=1&f_pcip4=&f_startip1=192&f_startip2=168&f_startip3=1&f_startip4=&f_endip1=192&f_endip2=168&f_endip3=1&f_endip4=&iptype=all&which_mode=0'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('BKS_service_add.htm')
    log.info( 'Step-3: Set userdefined(Type:STRING, MaxLen:30) = 11111111112222222222ABCDEFGHIJK')
    post_url = host  + 'fw_serv_add.cgi' + token
    post_data = 'apply=Add&service_type=User+Defined&protocol=TCP&portstart=5000&portend=5000&userdefined=11111111112222222222ABCDEFGHIJK&f_pcip1=192&f_pcip2=168&f_pcip3=1&f_pcip4=&f_startip1=192&f_startip2=168&f_startip3=1&f_startip4=&f_endip1=192&f_endip2=168&f_endip3=1&f_endip4=&iptype=all&which_mode=0'
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
