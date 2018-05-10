'''[PSV-2017-0794] Directory Traversal Vulnerability  '''
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
    log.info('step-1 User should NOT get the system files')
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
    data = 'buttonHit=&buttonValue=&submit_flag=browser_close&nodenumber=1&currentpath=/tmp/mnt/usb0/part1/../../../../../&nodevalue=0*foo*0*bar*1&BT_path=x'
    if console_type == 'cable':
        post_url = host + 'goform/USBBrowse' + token
    else:
        post_url = host + 'usb_browse.cgi' + token
    r = ''
    try:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    except:
        time.sleep(1)
    if r != '':
        if r.text.find('401') != -1 or r.text.find('/tmp/mnt/usb0/part1') == -1:
            case = 'pass'
        else:
            case = 'fail'
        assert case == 'pass', "The function should not work." 
    else:
        assert r == '', "The function should not work." 
