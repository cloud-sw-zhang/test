'''[PSV-2017-2227] Post-Auth RCE via workGroup parameter in USB-basic.htm  '''
''' anthor Cloud 2017-12-12'''
'''v1.0 '''
from API._API import *

#def test_step_0():
    #log.info( 'step-0-0 dut loaddrfault wait 160s')
    #aploaddefault()
    #log.info( "step-0-1 AP Genie over leap done")
    #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info("step-1 Httpd shouldn't be down or DUT shouldn't be telnet")
    url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd)
    payload = "a" * 0x1c
    payload += 'dead' # R4
    payload += 'dead' # R5
    payload += 'dead' # R6
    payload += 'dead' # R7
    payload += struct.pack("I", 0x94dc0)
    data = {
        'deviceName': payload,
        'workGroup': '123',
        'enable_samba': 'enable_samba',
        'enable_http': 'enable_http',
        'http_via_port': '443',
        'ftp_via_port': '21',
        'Availabe_USB_sel': 'Availabe_USB_sel',
        'no_usb_device': '0',
        'sharefolderNum': '1',
        'usb_num': '1',
        'select': '0',
        'action': 'advanced',
        'umountsucc': '0',
        'enable_apmode': '0',
        'enable_stamode': '0',
        'is_https': '1',
        'router_smb_link_style': 'others',
        'no_dlna': ''
    }
    headers = {
        'Host': hostip,
        'Cache-Control': 'max-age=0',
        'Authorization': Authorization,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    }
    if console_type == 'cable':
        if ProjectName == 'C6300':
            post_url = host + 'cgi-bin/USBAdvRetail.cgi' + token
        else:
            post_url = host + 'goform/USBAdvRetail' + token
        data = 'Apply=Apply&deviceName=' + payload + '&workGroup=Mick321&enable_samba=true&enable_http=true&http_via_port=443&enable_wan_http_protect=true&ftp_via_port=21&enable_wan_ftp_protect=true&no_usb_device=1&sharefolderNum=0&usb_num=1&select=-1&action=advance&umountsucc=0&enable_apmode=0&is_https=1&router_smb_link_style=others&no_dlna=&add_edit_page=0&folderIdx=-1&UUID=-1'
    else:
        post_url = host + 'usb_adv.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        log.info(r.status_code)

def test_Step_2():
    log.info( 'step-2 check telnet dut')
    str2 = judjeduttelnet()
    if str2 == 'pass':
        log.info(str2)
        log.info( "check telnet dut pass")
        time.sleep(1)
    else:
        log.info(str2)
        log.info( "check telnet dut fail")
    assert str2 == 'pass', "This action should work." 

def test_Step_3():
    log.info( 'step-3 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 