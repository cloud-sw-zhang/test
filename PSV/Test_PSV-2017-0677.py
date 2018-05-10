''' [PSV-2017-0677] Authentication byPass     '''
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
    headers = {
        'Host': hostip,
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    }
    data1 = token + '&next_file=MNU_accessPassword_recovered.htm'
    post_url = host + 'genie_restoring.cgi?' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data1,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        log.info('Get 1 r.text')
        log.info(r.text)
        if r.text.find('admin') == -1 and r.text.find('Password!') == -1:
            case1 = 'pass'
        else:
            case1 = 'fail'
    else:
        case1 = 'pass'
    data2 = token + '&next_file=cgi-bin/../../../../etc/passwd'
    post_url = host + 'genie_restoring.cgi?' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data2,timeout=5)
    except:
        time.sleep(1)
    log.info('Get 2 r.text')
    if r != '':
        log.info(r.text)
        if r.text.find('admin:Password!') == -1:
            case2 = 'pass'
        else:
            case2 = 'fail'
    else:
        case2 = 'pass'
    log.info('User should NOT get the CSRF ID without authentication to access "http://192.168.1.1/MNU_top.htm"')
    get_url = "http://" + hostip + "/MNU_top.htm"
    r = ''
    try:
        r = requests.get(get_url,auth=('',''))
        log.info(r.status_code)
    except:
        time.sleep(1)
    log.info('Get 3 r.status_code')
    if r != '':
        if r.status_code == 401:
            case3 = 'pass'
        else:
            case3 = 'fail'
    else:
        case3 = 'pass'
    if case1 =='pass' and case2 == 'pass' and case3 == 'pass':
        case = 'pass'
    else:
        case = 'fail'
    assert case == 'pass', "The function should not work." 
