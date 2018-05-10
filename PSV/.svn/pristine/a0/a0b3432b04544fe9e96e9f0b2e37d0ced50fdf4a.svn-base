''' [PSV-2017-0428] OS directory lists and logs are leaked without authentication   '''
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
    log.info('step-1 OS directory lists and logs are leaked without authentication')
    log.info('enable access control')
    url = host + urlLogs
    token = getIDToken(url)
    Authorization = 'Basic ' + base64.b64encode(user + ':' + passwd)
    headers = {
        'Host': hostip,
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    }
    if console_type == 'cable':
        if ProjectName == 'C6300':
            post_url = host + 'cgi-bin/USBBrowse.htm?'+'UUID=4098-E724&currentPath=..%2F..%2F..%2Fetc%2F?geine'
        else:
            post_url = host + 'USBBrowse.htm?'+'UUID=4098-E724&currentPath=..%2F..%2F..%2Fetc%2F?geine'
        try:
            r = requests.get(post_url, headers=headers)
        except:
            time.sleep(1)
    else:
        data ='submit_flag=browser&currentpath=/../tmp/'
        post_url = host + 'usb_browse.cgi' + token + '?genie'
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
    try:
        log.info(r.text)
    except:
        time.sleep(1)
    time.sleep(10)
    log.info('Send it again')
    r = ''
    if console_type == 'cable':
        try:
            r = requests.get(post_url, headers=headers)
            log.info(r.text)
        except:
            time.sleep(1)
    else:
        r = requests.post(post_url, headers=headers, data=data,timeout=5)
        log.info(r.text)
    if r != '':
        assert r.status_code == 401,'This is should not work'
    else:
        assert r == '','This is should not work'
