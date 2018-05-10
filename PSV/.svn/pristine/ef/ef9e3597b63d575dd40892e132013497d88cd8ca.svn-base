'''  [PSV-2017-0648] Denial of Service     '''
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
    if ProjectName == 'CM700' or ProjectName == 'C7000-100NAS':
        username = 'A'*9999
        password = 'B'*3333
    elif ProjectName == 'CM400':
        username = 'A'*1999
        password = 'B'*3333
    else:
        username = 'A'*30000
        password = 'B'*1000
    Authorization = 'Basic ' + base64.b64encode(username + ':' + password) 
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
    if console_type == 'cable':
        post_url = host + 'DashBoard.htm'
    else:
        post_url = host + 'start.htm'
    r = ''
    try:
        r = requests.get(post_url, headers=headers)
        log.info(r.status_code)
    except:
        time.sleep(1)
    time.sleep(5)
    if r != '':
        assert r.status_code == 401, "This action should not  work."
    else:
        assert r == '', "This action should not  work."

def test_Step_2():
    log.info( 'step-2 Make sure the Web GUI should not crash')
    url = "http://" + user + ':' + passwd + "@" + hostip + '/' + urlDevicecontrol
    str = check_DUTnocrash(url)
    assert str == 'pass', "This action should work." 