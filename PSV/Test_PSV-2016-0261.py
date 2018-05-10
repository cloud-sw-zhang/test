''' [PSV-2016-0074] Buffer overflow issue   '''
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
    log.info('step-1 Buffer overflow in the URL timestamp parameter')
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
        if ProjectName == 'CM700':
            post_url = host + "goform/OidSubmit?id=" + "A"*600
            data = 'action_Clear=Clear+Log'
        elif ProjectName == 'CM500':
            post_url = host + "goform/eventLog?id=" + "A"*600
            data = 'docsDevEvControl.0=1'
        else:
            post_url = host + "goform/PwdRec_checkserial?id=" + "A"*600
    else:
        post_url = host + "unauth.cgi?id=" + "A"*600
    if  ProjectName == 'CM700' or ProjectName == 'CM500':
        r = ''
        try:
            r = requests.post(post_url, headers=headers, data=data,timeout=5)
            log.info(r.text)
        except:
            time.sleep(1)
    else:
        try:
            r = requests.get(post_url)
            log.info(r.text)
        except:
            time.sleep(1)

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 