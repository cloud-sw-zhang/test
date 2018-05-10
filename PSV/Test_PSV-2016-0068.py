''' 	[PSV-2016-0068] Password Recovery    '''
''' anthor Cloud 2017-12-13'''
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
    log.info('step-1 RCE via device_name parameter ')
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
    data = 'Continue=Continue'
    if console_type == 'cable':
        post_url = host + 'goform/PwdRec_AskQuestion' + token
    else:
        post_url = host + 'passwordrecovered.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    print 'r=',r
    if r != '': 
        log.info(r.text)
        assert r.text.find('admin') == -1, "The function should not work." 
    else:
        assert r == '', "This action should not  work."

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not reboot')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 