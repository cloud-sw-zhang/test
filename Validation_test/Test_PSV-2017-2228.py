'''Validation test'''
'''[PSV-2017-2228] Post-Auth RCE via workGroup parameter in USB-basic.htm'''

from API._API import *

def test_Step_1():
    token = getIDToken('USB_adv_tab.htm')
    log.info( 'Step-1: Set workGroup(Type:STRING, MaxLen:15) as empty')
    post_url = host  + 'usb_adv.cgi' + token
    post_data = 'Apply=Apply&workGroup=&enable_samba=enable_samba&enable_http=enable_http&http_via_port=443&enable_wan_http_protect=enable_wan_http_protect&ftp_via_port=21&enable_wan_ftp_protect=enable_wan_ftp_protect&Availabe_USB_sel=Availabe_USB_sel&no_usb_device=0&sharefolderNum=1&usb_num=1&select=0&action=advance&umountsucc=0&enable_apmode=0&enable_stamode=0&is_https=1&router_smb_link_style=others&no_dlna='
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_2():
    token = getIDToken('USB_adv_tab.htm')
    log.info( 'Step-2: Set workGroup(Type:STRING, MaxLen:15) = Workgroup')
    post_url = host  + 'usb_adv.cgi' + token
    post_data = 'Apply=Apply&workGroup=Workgroup&enable_samba=enable_samba&enable_http=enable_http&http_via_port=443&enable_wan_http_protect=enable_wan_http_protect&ftp_via_port=21&enable_wan_ftp_protect=enable_wan_ftp_protect&Availabe_USB_sel=Availabe_USB_sel&no_usb_device=0&sharefolderNum=1&usb_num=1&select=0&action=advance&umountsucc=0&enable_apmode=0&enable_stamode=0&is_https=1&router_smb_link_style=others&no_dlna='
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
        judje_dutReboot(tmpHTML.text)
    assert tmpHTML.status_code == 200, "This action should work." 
    
def test_Step_3():
    token = getIDToken('USB_adv_tab.htm')
    log.info( 'Step-3: Set workGroup(Type:STRING, MaxLen:15) = WorkgroupWorkgroup')
    post_url = host  + 'usb_adv.cgi' + token
    post_data = 'Apply=Apply&workGroup=WorkgroupWorkgroup&enable_samba=enable_samba&enable_http=enable_http&http_via_port=443&enable_wan_http_protect=enable_wan_http_protect&ftp_via_port=21&enable_wan_ftp_protect=enable_wan_ftp_protect&Availabe_USB_sel=Availabe_USB_sel&no_usb_device=0&sharefolderNum=1&usb_num=1&select=0&action=advance&umountsucc=0&enable_apmode=0&enable_stamode=0&is_https=1&router_smb_link_style=others&no_dlna='
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    else:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 60s")
        judje_dutReboot(tmpHTML.text)

    assert tmpHTML.status_code == 400, "This action should not work."  
