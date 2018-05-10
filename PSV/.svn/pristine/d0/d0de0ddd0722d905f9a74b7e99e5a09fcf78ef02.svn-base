''' [PSV-2016-0254] Disclose Pass    '''
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
    log.info('step-1 User should NOT pass two security questions to get password for admin')
    url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd) 
    if console_type == 'cable':
        headers = {
            'Host': hostip,
            'Content-Length': '160',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': host + 'goform/PwdRec_checkseria'+ token,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            'Connection': 'close'
        }
        data = 'Continue=Continue'
        post_url = host + 'goform/PwdRec_AskQuestion' + token
    else:
        data = ' '
        headers = { }
        post_url = host + 'passwordrecovered.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '': 
        log.info(r.text)
        if r.text.find('admin') == -1 and r.text.find('Password!') == -1:
            case = 'pass'
        else:
            case = 'fail'
    else:
        case = 'pass'
    assert case == 'pass', "The function should not work." 
