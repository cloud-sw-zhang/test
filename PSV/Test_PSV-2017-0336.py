''' [PSV-2017-0336] CSRF - Router reboot using /newgui_adv_home.cgi '''
''' anthor Cloud 2017-12-08'''
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
    log.info('step-1 CSRF-Router reboot using/newgui_adv_home.cgi----DUT should prevent the CSRF attack')
    if console_type == 'cable':
        print 'This case NA'
        result = 'fail'
        assert result == 'pass', "The function should not work." 
    else:
        url = host + urlLogs
        token = getIDToken(url)
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
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
        data = 'buttonSelect=2&wantype=dhcp&enable_apmode=0'
        if console_type == 'cable':
            post_url = host + 'goform/newgui_adv_home'
        else:
            post_url = host + 'newgui_adv_home.cgi?id=1432613806'
        r = requests.post(post_url, headers=headers, data=data,timeout=5) 
        log.info(r.status_code)
    assert r.status_code == 200, "The function should not work." 

def test_Step_2():
    log.info( 'step-2 check telnet dut')
    if console_type == 'cable':
        print 'This case NA'
        str2 = 'fail'
    else:
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
    if console_type == 'cable':
        print 'This case NA'
        str = 'fail'
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
        str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work."