'''Validation test'''
'''[PSV-2017-0803] Post-auth RCE: Stack overflow in /ddns.cgi through "sysDNSProviderlist" parameter'''
from API._API import *

def test_Step_1():
    token = getIDToken('DNS_ddns.htm')
    log.info( 'Step-1: Set sysDNSProviderlist(Type:INDEX, MaxLen:1, Range:0~4) = 0')
    post_url = host  + 'ddns.cgi' + token
    post_data = 'cfAlert_Apply=Apply&sysDNSActive=dnsEnable&sysDNSProviderlist=0&sysDNSHost=1&sysDNSUser=123@123.com&sysDNSPassword=12345678&account=no&sysDNSHost_Netgear=&sysDNSEmail_Netgear=&sysDNSPassword_Netgear=&sysDNSHost_Netgear_account=123&sysDNSEmail_Netgear_account=123@123.com&sysDNSPassword_Netgear_account=12345678&host_graycheck=-1&email_graycheck=-1&password_graycheck=-1&success_status=-1'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('DNS_ddns.htm')
    log.info( 'Step-2: Set sysDNSProviderlist(Type:INDEX, MaxLen:1, Range:0~4) = 4')
    post_url = host  + 'ddns.cgi' + token
    post_data = 'cfAlert_Apply=Apply&sysDNSActive=dnsEnable&sysDNSProviderlist=4&sysDNSHost=1&sysDNSUser=123@123.com&sysDNSPassword=12345678&account=no&sysDNSHost_Netgear=&sysDNSEmail_Netgear=&sysDNSPassword_Netgear=&sysDNSHost_Netgear_account=123&sysDNSEmail_Netgear_account=123@123.com&sysDNSPassword_Netgear_account=12345678&host_graycheck=-1&email_graycheck=-1&password_graycheck=-1&success_status=-1'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work."

def test_Step_3():
    token = getIDToken('DNS_ddns.htm')
    log.info( 'Step-3: Set sysDNSProviderlist(Type:INDEX, MaxLen:1, Range:0~4) = 5')
    post_url = host  + 'ddns.cgi' + token
    post_data = 'cfAlert_Apply=Apply&sysDNSActive=dnsEnable&sysDNSProviderlist=5&sysDNSHost=1&sysDNSUser=123@123.com&sysDNSPassword=12345678&account=no&sysDNSHost_Netgear=&sysDNSEmail_Netgear=&sysDNSPassword_Netgear=&sysDNSHost_Netgear_account=123&sysDNSEmail_Netgear_account=123@123.com&sysDNSPassword_Netgear_account=12345678&host_graycheck=-1&email_graycheck=-1&password_graycheck=-1&success_status=-1'
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
    token = getIDToken('DNS_ddns.htm')
    log.info( 'Step-4: Set sysDNSProviderlist(Type:INDEX, MaxLen:1, Range:0~4) = -1')
    post_url = host  + 'ddns.cgi' + token
    post_data = 'cfAlert_Apply=Apply&sysDNSActive=dnsEnable&sysDNSProviderlist=-1&sysDNSHost=1&sysDNSUser=123@123.com&sysDNSPassword=12345678&account=no&sysDNSHost_Netgear=&sysDNSEmail_Netgear=&sysDNSPassword_Netgear=&sysDNSHost_Netgear_account=123&sysDNSEmail_Netgear_account=123@123.com&sysDNSPassword_Netgear_account=12345678&host_graycheck=-1&email_graycheck=-1&password_graycheck=-1&success_status=-1'
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
