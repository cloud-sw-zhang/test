'''[PSV-2017-0308] Stack overflow in fwLog.cgi through "log_refresh" parameter and others (RCE)  '''
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
    log.info("step-1 DUT shouldn't crash.")
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
    if console_type == 'cable':
        data = 'action_Refresh=Refresh&log_cat_1=1&log_cat_2=1&log_cat_3=1&log_cat_4=1&log_cat_5=1&log_cat_6=1&log_cat_7=1&log_cat_8=1&email_on=0&log_refresh='+'A'*3000+'&log_send=0&log_clear=0&log_enable=111&log_filter=255'
        if ProjectName == ' C6300-100NAS':
            post_url = host + 'cgi-bin/Logs.cgi' + token
        else:
            post_url = host + 'goform/Logs' + token
    else:
        payload = ''
        payload += 'A' * 1820
        data = {
            'log_refresh': payload
        }
        post_url = host + 'fwlog.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data)
    except:
        time.sleep(1)
    if r != '': 
        log.info(r.status_code)
    else:
        log.info('post get nothing')

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 
