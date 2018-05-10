''' [PSV-2016-0061] Issue3 lind Command Execution with DNS Lookup '''
''' anthor Cloud 2017-12-07'''
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
    log.info('step-1 Command Execution with Ping')
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
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    }
    data = 'hostname=|/usr/sbin/telnetd -p 90 -l /bin/sh&lookup=Lookup'
    post_url = host + 'dnslookup.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        if r.status_code == 404 or r.status_code == 401:
            log.info(r)
            log.info( "The function or page should not exist in DUT-pass")
            time.sleep(3)
        else:
            log.info(r)
            log.info( "The function or page should not exist in DUT-fail")
            judje_dutReboot(r.text)
        if console_type == 'cable':
            assert r.status_code == 401, "The function or page should not exist in DUT." 
        else:
            assert r.status_code == 404, "The function or page should not exist in DUT." 
    else:
        assert r == '', "The function or page should not exist in DUT."  

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
