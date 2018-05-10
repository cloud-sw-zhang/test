''' [PSV-2017-0793] Stack overflow in LANG_check_brslang.htm  '''
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
    log.info('step-1 Stack overflow in LANG_check_brslang.htm')
    if console_type == 'cable':
        print 'This case NA'
    else:
        url = host + urlLogs
        token = getIDToken(url)
        Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
        headers = {
            'Host': hostip,
            'Authorization':Authorization,
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        }
        data = {
            'brslanguage': '',
            'version': '',
            'browser': 'a'*500 # the browser element trigger this stack overflow
        }
        if console_type == 'cable':
            post_url = host + 'goform/langbrscheck' + token
        else:
            post_url = host + 'langbrscheck.cgi' + token
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        log.info(r.text)

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    if console_type == 'cable':
        print 'This case NA'
        str = 'fail'
    else:
        url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
        str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 